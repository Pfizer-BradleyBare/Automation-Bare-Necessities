from __future__ import annotations

from django.db import models

from ..definition import SolutionPropertyPresetDefinition


class SolutionPropertyPreset(models.Model):
    name = models.CharField(max_length=255, unique=True)
    liquid_type = models.CharField(
        max_length=14,
        choices=(
            ("Aqueous", "Aqueous"),
            ("Organic", "Organic"),
            ("Auto-determine", "Auto-determine"),
        ),
    )
    viscosity = models.CharField(
        max_length=14,
        choices=(
            ("Low", "Low"),
            ("Medium", "Medium"),
            ("High", "High"),
            ("Auto-determine", "Auto-determine"),
        ),
    )
    volatility = models.CharField(
        max_length=14,
        choices=(
            ("Low", "Low"),
            ("Medium", "Medium"),
            ("High", "High"),
            ("Auto-determine", "Auto-determine"),
        ),
    )
    homogeneity = models.CharField(
        max_length=14,
        choices=(
            ("Heterogenous", "Heterogenous"),
            ("Homogenous", "Homogenous"),
            ("Suspension", "Suspension"),
            ("Emulsion", "Emulsion"),
            ("Auto-determine", "Auto-determine"),
        ),
    )

    def get_definition(self) -> SolutionPropertyPresetDefinition:
        return SolutionPropertyPresetDefinition(
            name=self.name,
            liquid_type=self.liquid_type,
            volatility=self.volatility,
            viscosity=self.viscosity,
            homogeneity=self.homogeneity,
        )

    def __str__(self) -> str:
        return self.name
