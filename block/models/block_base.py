from __future__ import annotations

from abc import abstractmethod
from typing import ClassVar, TypeAlias, cast

from django.db import models
from loguru import logger
from polymorphic.models import PolymorphicModel

from excel.definitions import BlockDefinitionExcelDefinition
from method.models import MethodWorkbookBase

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
    is_valid = True

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
            field_name = parameter._field_name  # noqa: SLF001

            value = None
            try:
                value = kwargs.pop(key_name)
            except KeyError:
                bound_logger.critical(
                    f"{key_name} is missing from the block parameters",  # noqa: G004
                )

            setattr(self, field_name, value)

    @abstractmethod
    def validate(self):
        raise NotImplementedError

    @abstractmethod
    def execute(self):
        raise NotImplementedError

    def __init_subclass__(cls: type[BlockBase]) -> None:
        cls.block_subclasses[cls.__name__] = cls

    def __str__(self) -> str:
        return f"{self.method}: {self.row+1}|{self.column+3} -> {type(self).__name__} "
