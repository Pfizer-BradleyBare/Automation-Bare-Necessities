from __future__ import annotations

from django.db import models

from method.models.user_method import UserMethodWorkbookBase

from .component_base import ComponentBase


def NON_POLYMORPHIC_CASCADE(collector, field, sub_objs, using):
    return models.CASCADE(collector, field, sub_objs.non_polymorphic(), using)


class UserDefinedComponentBase(ComponentBase):
    name = models.CharField(max_length=255)
    method = models.ForeignKey(
        to=UserMethodWorkbookBase,
        on_delete=NON_POLYMORPHIC_CASCADE,
    )

    def get_name(self) -> str:
        return f"{self.method}:{self.name}"

    def __str__(self) -> str:
        return f"USER DEFINED: {self.method}:{self.name}"

    class Meta:
        unique_together = ["name", "method"]
