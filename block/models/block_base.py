from __future__ import annotations

from abc import abstractmethod
from typing import ClassVar

from django.db import models
from polymorphic.models import PolymorphicModel

from excel.definitions import BlockDefinitionExcelDefinition
from method.models import UserMethodBase


class BlockBase(PolymorphicModel):
    block_subclasses: ClassVar[dict[str, type[BlockBase]]] = {}

    method = models.ForeignKey(to=UserMethodBase, on_delete=models.CASCADE)
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

    @abstractmethod
    def get_excel_definition(self) -> BlockDefinitionExcelDefinition:
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
        return f"{self.method}: {self.row}|{self.column} -> {type(self).__name__} "
