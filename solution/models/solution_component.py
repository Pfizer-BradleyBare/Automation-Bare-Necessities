from __future__ import annotations

from django.db import models

from .component_base import ComponentBase


class SolutionComponent(models.Model):
    component = models.ForeignKey(to=ComponentBase, on_delete=models.CASCADE)
    amount = models.FloatField()
    unit = models.CharField(
        max_length=10,
        choices=(("uL", "uL"), ("mg", "mg"), ("units", "units")),
    )

    class Meta:
        unique_together = ["component", "amount", "unit"]

    def __str__(self) -> str:
        return f"{self.amount} {self.unit} {self.component.get_name()}"
