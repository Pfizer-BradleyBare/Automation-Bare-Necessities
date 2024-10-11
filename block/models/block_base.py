from __future__ import annotations

from abc import abstractmethod
from typing import ClassVar
from typing import TypeAlias

from django.db import models
from polymorphic.models import PolymorphicModel

from excel.definitions import BlockDefinitionExcelDefinition
from method.models import MethodWorkbookBase
from plh_config.labware.models import LabwareBase

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


def DROPDOWN_LABWARE_NAMES() -> str:
    return ",".join([labware.identifier for labware in LabwareBase.objects.all()])


BlockBaseType: TypeAlias = "BlockBase"

class BlockBase(PolymorphicModel):
    block_subclasses: ClassVar[dict[str, type[BlockBase]]] = {}

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
    right_parent= models.ForeignKey(
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

    @abstractmethod
    def assign_parameters(self,parameters:dict):
        self.row = parameters["row"]
        self.column = parameters["column"]
        self.method = parameters["method"]

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
