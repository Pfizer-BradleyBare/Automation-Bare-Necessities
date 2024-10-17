from __future__ import annotations

from abc import abstractmethod
from typing import ClassVar, TypeAlias, cast

from django.db import models
from loguru import logger
from polymorphic.models import PolymorphicModel

from method.models import MethodWorkbookBase
from plh_config.labware.models import PipettableLabware
from solution.models import PredefinedSolution, UserDefinedSolution
from worklist.models import WorklistColumn, WorklistColumnValue

from ..definition import BlockDefinition

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
    is_valid: bool = True

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
    def get_block_definition(cls) -> BlockDefinition:
        raise NotImplementedError

    def assign_parameters(
        self,
        **kwargs: float | str | MethodWorkbookBase,
    ):
        self.row = cast(int, kwargs.get("row"))
        self.column = cast(int, kwargs.get("column"))
        self.method = cast(MethodWorkbookBase, kwargs.get("method"))

        bound_logger = logger.bind(
            source="ABN",
            method=str(self.method),
            row=self.row,
            column=self.column,
            block=type(self).__name__,
        )

        definition = self.get_block_definition()

        for parameter in definition.parameters:
            key_name = parameter.label
            field_name = parameter.block_field_name
            advanced = parameter.advanced

            try:
                value = kwargs.pop(key_name)

                if value is None:
                    setattr(self, field_name, None)
                    self.is_valid = False
                    bound_logger.critical(
                        f"Parameter '{key_name}' has no value",  # noqa: G004
                    )
                else:
                    setattr(self, field_name, str(value))

            except KeyError:
                setattr(self, field_name, None)
                if advanced is False:
                    self.is_valid = False
                    bound_logger.critical(
                        f"Block is missing required parameter '{key_name}'",  # noqa: G004
                    )

    def validate_parameters(self):
        definition = self.get_block_definition()

        bound_logger = logger.bind(
            source="ABN",
            method=str(self.method),
            row=self.row,
            column=self.column,
            block=type(self).__name__,
        )

        for parameter in definition.parameters:
            label = parameter.label
            field_name = parameter.block_field_name
            field_type = parameter.block_field_type
            free_text = parameter.free_text
            dropdown_items = parameter.dropdown_items.split(",")

            value = cast(str | None, getattr(self, field_name))

            if value is None:
                continue
            # This is a missing parameter. User notification is performed when we assign parameters. Let's not repeat it.

            if (
                DROPDOWN_WORKLIST_COLUMN_NAMES in dropdown_items
                or DROPDOWN_PREFIXED_WORKLIST_COLUMN_NAMES in dropdown_items
            ):
                column_query = WorklistColumn.objects.filter(
                    method=self.method,
                    name=value.replace(PREFIX_WORKLIST_COLUMN_NAMES, ""),
                )

                if column_query.exists():
                    column = column_query.get()

                    values = [
                        column_value.value
                        for column_value in WorklistColumnValue.objects.filter(
                            worklist_column=column,
                        ).all()
                    ]

                    if None in values:
                        bound_logger.critical(
                            f"Worklist column '{value}' contains empty cells. Every cell must have a value.",  # noqa:G004
                        )
                        continue

                    is_worklist_column = True
                    values = cast(list[str], values)
                else:
                    is_worklist_column = False
                    values = [value]
            else:
                values = [value]

            for value in values:
                if value in dropdown_items:
                    continue

                if free_text is True:
                    if field_type is float:
                        try:
                            float(value)
                            continue
                        except ValueError:
                            ...
                    if field_type is str:
                        try:
                            str(value)
                            continue
                        except ValueError:
                            ...

                if (
                    DROPDOWN_CONTAINER_NAMES in dropdown_items
                    or DROPDOWN_PREFIXED_CONTAINER_NAMES in dropdown_items
                ):
                    from .pathways import ActivateContainer

                    if ActivateContainer.objects.filter(
                        method=self.method,
                        name=value.replace(PREFIX_CONTAINER_NAMES, ""),
                    ).exists():
                        continue

                if (
                    DROPDOWN_CONTAINER_LABWARE_NAMES in dropdown_items
                    or DROPDOWN_PREFIXED_CONTAINER_LABWARE_NAMES in dropdown_items
                ):
                    None

                    if PipettableLabware.objects.filter(
                        identifier=value.replace(PREFIX_CONTAINER_LABWARE_NAMES, ""),
                    ).exists():
                        continue

                if (
                    DROPDOWN_PREDEFINED_SOLUTION_NAMES in dropdown_items
                    or DROPDOWN_PREFIXED_PREDEFINED_SOLUTION_NAMES in dropdown_items
                ):
                    None

                    if PredefinedSolution.objects.filter(
                        name=value.replace(PREFIX_PREDEFINED_SOLUTION_NAMES, ""),
                    ).exists():
                        continue

                if (
                    DROPDOWN_USER_DEFINED_SOLUTION_NAMES in dropdown_items
                    or DROPDOWN_PREFIXED_USER_DEFINED_SOLUTION_NAMES in dropdown_items
                ):
                    None

                    if UserDefinedSolution.objects.filter(
                        name=value.replace(PREFIX_USER_DEFINED_SOLUTION_NAMES, ""),
                        method=self.method,
                    ).exists():
                        continue

                bound_logger.critical(f"{label} is not VALID.")

    def __init_subclass__(cls: type[BlockBase]) -> None:
        cls.block_subclasses[cls.__name__] = cls

    def __str__(self) -> str:
        return f"{self.method}: {self.row}|{self.column} -> {type(self).__name__} "
