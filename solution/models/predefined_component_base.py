from __future__ import annotations

from django.db import models

from .component_base import ComponentBase


class PredefinedComponentBase(ComponentBase):
    name = models.CharField(max_length=255, unique=True)

    def get_name(self) -> str:
        return self.name

    def __str__(self) -> str:
        return f"PREDEFINED: {self.name}"
