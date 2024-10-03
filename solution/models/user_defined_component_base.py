from __future__ import annotations

from django.db import models

from method.models import UserMethodWorkbookBase

from .component_base import ComponentBase


class UserDefinedComponentBase(ComponentBase):
    name = models.CharField(max_length=255)
    method = models.ForeignKey(to=UserMethodWorkbookBase, on_delete=models.CASCADE)

    def get_name(self) -> str:
        return f"{self.method}:{self.name}"

    def __str__(self) -> str:
        return f"USER DEFINED: {self.method}:{self.name}"

    class Meta:
        unique_together = ["name", "method"]
