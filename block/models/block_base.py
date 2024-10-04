from __future__ import annotations

from abc import abstractmethod
from typing import ClassVar

from django.db import models
from polymorphic.models import PolymorphicModel

from excel.definitions import BlockDefinitionExcelDefinition
from method.models import UserMethodWorkbookBase

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


class BlockBase(PolymorphicModel):
    block_subclasses: ClassVar[dict[str, type[BlockBase]]] = {}

    method = models.ForeignKey(to=UserMethodWorkbookBase, on_delete=models.CASCADE)
    row = models.IntegerField()
    column = models.IntegerField()

    left_parent: models.ForeignKey[BlockBase | None] = models.ForeignKey(
        to="BlockBase",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="+",
    )
    middle_parent: models.ForeignKey[BlockBase | None] = models.ForeignKey(
        to="BlockBase",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="+",
    )
    right_parent: models.ForeignKey[BlockBase | None] = models.ForeignKey(
        to="BlockBase",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="+",
    )

    left_child: models.ForeignKey[BlockBase | None] = models.ForeignKey(
        to="BlockBase",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="+",
    )
    middle_child: models.ForeignKey[BlockBase | None] = models.ForeignKey(
        to="BlockBase",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="+",
    )
    right_child: models.ForeignKey[BlockBase | None] = models.ForeignKey(
        to="BlockBase",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="+",
    )

    @classmethod
    @abstractmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        raise NotImplementedError

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
