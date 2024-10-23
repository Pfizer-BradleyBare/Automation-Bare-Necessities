from __future__ import annotations

import functools
import operator
from abc import abstractmethod
from typing import ClassVar, TypeAlias, cast

from django.db import models
from loguru import logger
from polymorphic.models import PolymorphicModel

from method.models import MethodWorkbookBase
from worklist.models import WorklistColumn, WorklistColumnValue

from ..definition import BlockDefinition
from ..validators import dropdown_validator, empty_validator, worklist_column_validator

PREFIX_CONTAINER_NAMES = "_CONTAINER: "
PREFIX_PREDEFINED_SOLUTION_NAMES = ""
PREFIX_USER_DEFINED_SOLUTION_NAMES = ""
PREFIX_WORKLIST_COLUMN_NAMES = "_WORKLIST: "
PREFIX_CONTAINER_LABWARE_NAMES = ""

DROPDOWN_CONTAINER_NAMES = "%%get_container_names_as_string"
DROPDOWN_PREFIXED_CONTAINER_NAMES = "%%get_prefixed_container_names_as_string"
DROPDOWN_PREDEFINED_SOLUTION_NAMES = "%%get_loaded_solution_names_as_string"
DROPDOWN_PREFIXED_PREDEFINED_SOLUTION_NAMES = (
    "%%get_prefixed_loaded_solution_names_as_string"
)
DROPDOWN_USER_DEFINED_SOLUTION_NAMES = "%%get_defined_solution_names_as_string"
DROPDOWN_PREFIXED_USER_DEFINED_SOLUTION_NAMES = (
    "%%get_prefixed_defined_solution_names_as_string"
)
DROPDOWN_WORKLIST_COLUMN_NAMES = "%%get_worklist_column_names_as_string"
DROPDOWN_PREFIXED_WORKLIST_COLUMN_NAMES = (
    "%%get_prefixed_worklist_column_names_as_string"
)
DROPDOWN_CONTAINER_LABWARE_NAMES = "%%get_container_labware_names_as_string"
DROPDOWN_PREFIXED_CONTAINER_LABWARE_NAMES = (
    "%%get_prefixed_container_labware_names_as_string"
)


BlockBaseType: TypeAlias = "BlockBase"


class BlockBase(PolymorphicModel):
    block_subclasses: ClassVar[dict[str, type[BlockBase]]] = {}
    is_valid = models.BooleanField(editable=False, default=False)

    method = models.ForeignKey(to=MethodWorkbookBase, on_delete=models.CASCADE)
    row = models.IntegerField()
    column = models.IntegerField()

    left_parent = models.ForeignKey(
        to=BlockBaseType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="+",
    )
    middle_parent = models.ForeignKey(
        to=BlockBaseType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="+",
    )
    right_parent = models.ForeignKey(
        to=BlockBaseType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="+",
    )

    left_child = models.ForeignKey(
        to=BlockBaseType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="+",
    )
    middle_child = models.ForeignKey(
        to=BlockBaseType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="+",
    )
    right_child = models.ForeignKey(
        to=BlockBaseType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="+",
    )

    @classmethod
    @abstractmethod
    def get_definition(cls) -> BlockDefinition:
        raise NotImplementedError

    def assign_parameters(
        self,
        **kwargs: float | str | MethodWorkbookBase,
    ):
        self.row = cast(int, kwargs.get("row"))
        self.column = cast(int, kwargs.get("column"))
        self.method = cast(MethodWorkbookBase, kwargs.get("method"))
        # Guarenteed to be there so no need to log before this step.

        bound_logger = logger.bind(
            source="ABN",
            method=str(self.method),
            row=self.row + 1,
            column=self.column + 2,
            block=type(self).__name__,
        )

        bound_logger.debug("assign_parameters")

        definition = self.get_definition()

        for parameter in definition.parameters:
            key_name = parameter.label
            field_name = parameter.block_field_name
            advanced = parameter.advanced

            bound_logger.debug(f"Assigning parameter '{key_name}'")

            try:
                value = kwargs.pop(key_name)

                if value is None:
                    setattr(self, field_name, None)

                    if advanced is False:
                        bound_logger.critical(
                            f"Required parameter '{key_name}' was provided but has no value",  # noqa: G004
                        )
                    else:
                        bound_logger.warning(
                            f"Advanced parameter '{key_name}' was provided but has no value. Will be ignored",  # noqa: G004
                        )
                else:
                    bound_logger.debug(
                        f"Value '{value}'",  # noqa: G004
                    )
                    setattr(self, field_name, str(value))

            except KeyError:
                setattr(self, field_name, None)
                if advanced is False:
                    bound_logger.critical(
                        f"Expected required parameter '{key_name}' was not found",  # noqa: G004
                    )
                else:
                    bound_logger.warning(
                        f"Advanced parameter '{key_name}' was not found. Will be ignored",  # noqa: G004
                    )

        bound_logger.info("Parameters assigned")

    def validate_parameters(self):
        bound_logger = logger.bind(
            source="ABN",
            method=str(self.method),
            row=self.row + 1,
            column=self.column + 2,
            block=type(self).__name__,
        )

        bound_logger.debug("validate_parameters")

        definition = self.get_definition()

        block_is_valid = True
        for parameter in definition.parameters:
            label = parameter.label
            block_field_validators = parameter.block_field_validators
            dropdown_items = parameter.dropdown_items
            validation_results: list[bool] = []
            validation_error_response_items: list[str] = []
            advanced = parameter.advanced

            bound_logger.debug(f"Validating parameter '{label}'")

            try:
                value = cast(str | None, getattr(self, parameter.block_field_name))
            except AttributeError:
                block_is_valid &= False
                continue

            if value is None:
                if advanced is False:
                    block_is_valid &= False
                continue
            # This is already handled when we assign parameters. Let's not do it twice.

            value = value.replace(PREFIX_WORKLIST_COLUMN_NAMES, "")
            # The only thing we care about is that the value can describe a worklist column. So let's remove that prefix now for easy handling.

            # Very simply, we are flattening the list of validators and removing the kwargs so that we can check if the worklist validator is present.
            if (
                DROPDOWN_WORKLIST_COLUMN_NAMES in dropdown_items
                or DROPDOWN_PREFIXED_WORKLIST_COLUMN_NAMES in dropdown_items
            ) and worklist_column_validator not in functools.reduce(
                operator.iadd,
                [
                    ([item] if not isinstance(item, tuple) else [item[0]])
                    if not isinstance(item, list)
                    else [
                        [sub_item] if not isinstance(sub_item, tuple) else [sub_item[0]]
                        for sub_item in item
                    ]
                    for item in block_field_validators
                ],
                [],
            ):
                column_query = WorklistColumn.objects.filter(
                    name=value,
                    method=self.method,
                )

                if column_query.exists():
                    is_worklist_column = True
                    column = column_query.get()

                    column_values = [
                        column_value.value
                        for column_value in WorklistColumnValue.objects.filter(
                            worklist_column=column,
                        )
                    ]
                else:
                    is_worklist_column = False
                    column_values = [value]

            else:
                is_worklist_column = False
                column_values = [value]
            # If value is a worklist column then we need to convert it.

            if is_worklist_column is True:
                bound_logger.debug(f"'{value}' is a worklist column")
            else:
                bound_logger.debug(f"'{value}' is NOT a worklist column")

            # attempt to run the validator
            for item in block_field_validators:
                validators = item if isinstance(item, list) else [item]

                sub_validation_results: list[bool] = []

                for validator in validators:
                    # There are kwargs included so we should search and replace as needed.
                    if isinstance(validator, tuple):
                        validation_function, kwargs = validator

                        updated_kwargs = {}
                        for kwarg_key, kwarg_value in kwargs.items():
                            if isinstance(kwarg_value, list):
                                updated_kwarg_list = []
                                for list_value in kwarg_value:
                                    if "%%" in str(list_value):
                                        try:
                                            updated_kwarg_list.append(
                                                getattr(
                                                    self,
                                                    str(list_value).replace("%%", ""),
                                                ),
                                            )
                                        except AttributeError:
                                            updated_kwarg_list.append(list_value)
                                    else:
                                        updated_kwarg_list.append(list_value)
                                updated_kwargs[kwarg_key] = updated_kwarg_list

                            elif isinstance(kwarg_value, str):
                                if "%%" in kwarg_value:
                                    try:
                                        updated_kwargs[kwarg_key] = getattr(
                                            self,
                                            str(kwarg_value).replace("%%", ""),
                                        )
                                    except AttributeError:
                                        updated_kwargs[kwarg_key] = kwarg_value

                        sub_validation_results += [
                            validation_function(
                                column_value,
                                self.method,
                                **updated_kwargs,
                            )
                            for column_value in column_values
                        ]

                        if validation_function is dropdown_validator:
                            acceptable_values = updated_kwargs["acceptable_values"]
                            validation_error_response_items += [
                                ", ".join(acceptable_values),
                            ]
                        else:
                            validation_error_response_items += [
                                validation_function.__name__,
                            ]

                    else:
                        sub_validation_results += [
                            validator(column_value, self.method)
                            for column_value in column_values
                        ]

                        validation_error_response_items += [validator.__name__]

                validation_results.append(
                    False if sum(sub_validation_results) < len(column_values) else True,  # noqa: SIM211
                )

            if bool(sum(validation_results)) is not True:
                block_is_valid &= False
                if is_worklist_column is False:
                    validation_error_response_items = [
                        item.replace("_validator", "").replace("_", " ").title()
                        for item in validation_error_response_items
                        if item != empty_validator.__name__
                    ]

                    validation_error_response_items = functools.reduce(
                        operator.iadd,
                        [item.split(",") for item in validation_error_response_items],
                        [],
                    )
                    bound_logger.critical(
                        f"Parameter '{label}' is not valid. Valid options include: \n*{'\n*'.join(validation_error_response_items)}",  # noqa:G004
                    )
                else:
                    validation_error_response_items = [
                        item.replace("_validator", "").replace("_", " ").title()
                        for item in validation_error_response_items
                    ]
                    for index, item in enumerate(validation_error_response_items):
                        if "," in item:
                            validation_error_response_items[index] = (
                                f"All rows are a combination of: '{item}'"
                            )
                        else:
                            validation_error_response_items[index] = (
                                f"All rows are '{item}'"
                            )
                    bound_logger.critical(
                        f"Worklist column '{value}' for Parameter '{label}' is not valid. Valid options include: \n*{'\n*'.join(validation_error_response_items)}",  # noqa:G004
                    )
            else:
                bound_logger.debug(f"Parameter '{label}' is valid")

        self.is_valid = block_is_valid
        bound_logger.info("Parameters validated")

    def __init_subclass__(cls: type[BlockBase]) -> None:
        cls.block_subclasses[cls.__name__] = cls

    def __str__(self) -> str:
        return f"{self.method}: {self.row+1}|{self.column+2} -> {type(self).__name__} "
