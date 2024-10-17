from __future__ import annotations

from typing import Literal, cast

from django.db import models

from ..definition import SolutionDefinition
from .solution_component import SolutionComponent
from .user_defined_component_base import UserDefinedComponentBase


class UserDefinedSolution(UserDefinedComponentBase):
    storage_condition = models.CharField(
        max_length=8,
        choices=(("Ambient", "Ambient"), ("Cold", "Cold")),
    )
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
    components: models.ManyToManyField[SolutionComponent, UserDefinedSolution] = (
        models.ManyToManyField(to=SolutionComponent, blank=True)
    )

    def get_definition(self) -> SolutionDefinition:
        definition = SolutionDefinition(
            name=self.name,
            liquid_type=self.liquid_type,
            volatility=self.volatility,
            viscosity=self.viscosity,
            homogeneity=self.homogeneity,
            storage_condition=self.storage_condition,
        )

        for component in self.components.all():
            definition.add_component(
                name=component.component.get_name(),
                amount=component.amount,
                unit=cast(Literal["uL", "mg", "units"], component.unit),
            )

        return definition
