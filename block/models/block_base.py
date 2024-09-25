from __future__ import annotations

from abc import abstractmethod
from typing import Any, ClassVar

from django.db import models
from polymorphic.models import PolymorphicModel

from method.models import UserMethodBase


def default_none() -> Any:
    return None


class BlockBase(PolymorphicModel):
    block_subclasses: ClassVar[dict[str, type[BlockBase]]] = {}
    block_name: str = "BlockBase"
    block_category: str = "__IGNORE__"

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
    def validate(self):
        raise NotImplementedError

    @abstractmethod
    def execute(self):
        raise NotImplementedError

    def __init_subclass__(cls: type[BlockBase]) -> None:
        cls.block_subclasses[cls.block_name] = cls

    def __str__(self) -> str:
        return f"{self.method}: {self.row}|{self.column} -> {self.block_name} "
