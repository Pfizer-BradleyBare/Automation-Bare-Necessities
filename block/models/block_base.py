from __future__ import annotations

from abc import abstractmethod
from typing import ClassVar, TypeAlias, cast

from django.db import models
from loguru import logger
from polymorphic.models import PolymorphicModel

from excel.definitions import BlockDefinitionExcelDefinition
from method.models import MethodWorkbookBase
from plh_config.labware.models import PipettableLabware

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
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
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

        definition = self.get_excel_definition()

        for parameter in definition.parameters:
            key_name = parameter.label
            field_name = parameter.block_field_name
            advanced = parameter.advanced

            value = None
            try:
                value = kwargs.pop(key_name)
            except KeyError:
                if advanced is False:
                    self.is_valid = False
                    bound_logger.critical(
                        f"{key_name} is missing from the block parameters",  # noqa: G004
                    )

            setattr(self, field_name, value)

    def validate_parameters(self):
        definition = self.get_excel_definition()

        bound_logger = logger.bind(
            source="ABN",
            method=str(self.method),
            row=self.row,
            column=self.column,
            block=type(self).__name__,
        )

        for parameter in definition.parameters:
            field_name = parameter.block_field_name
            field_type = parameter.block_field_type
            free_text = parameter.free_text
            dropdown_items = parameter.dropdown_items.split(",")

            value = getattr(self, field_name)

            if value is None:
                continue
            # This is a missing parameter. User notification is performed when we assign parameters. Let's not repeat it.

            for dropdown_item in dropdown_items:
                if dropdown_item in {
                    DROPDOWN_CONTAINER_NAMES,
                    DROPDOWN_PREFIXED_CONTAINER_NAMES,
                }:
                    from .pathways import ActivateContainer

                    prefix = "_CONTAINER: "
                    value = value.replace(prefix, "")

                    if ActivateContainer.objects.filter(
                        method=self.method,
                        name=value,
                    ).exists():
                        continue

                if dropdown_item in {
                    DROPDOWN_CONTAINER_LABWARE_NAMES,
                    DROPDOWN_PREFIXED_CONTAINER_LABWARE_NAMES,
                }:
                    prefix = ""
                    value = value.replace(prefix, "")

                    if PipettableLabware.objects.filter(identifier=value).exists():
                        continue

                if dropdown_item in {
                    DROPDOWN_PREDEFINED_SOLUTION_NAMES,
                    DROPDOWN_PREFIXED_PREDEFINED_SOLUTION_NAMES,
                }:
                    prefix = ""
                    value = value.replace(prefix, "")

                if dropdown_item in {
                    DROPDOWN_USER_DEFINED_SOLUTION_NAMES,
                    DROPDOWN_PREFIXED_USER_DEFINED_SOLUTION_NAMES,
                }:
                    prefix = ""
                    value = value.replace(prefix, "")

                if dropdown_item in {
                    DROPDOWN_WORKLIST_COLUMN_NAMES,
                    DROPDOWN_PREFIXED_WORKLIST_COLUMN_NAMES,
                }:
                    prefix = "_WORKLIST: "
                    value = value.replace(prefix, "")

    def __init_subclass__(cls: type[BlockBase]) -> None:
        cls.block_subclasses[cls.__name__] = cls

    def __str__(self) -> str:
        return f"{self.method}: {self.row}|{self.column} -> {type(self).__name__} "
