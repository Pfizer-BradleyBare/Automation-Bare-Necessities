from __future__ import annotations

import random

from django.db import models


def get_solutions():
    return ((i, str(i)) for i in range(random.randint(1, 20)))


class SolutionBase(models.Model):
    name = models.CharField(max_length=255)
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

    component_1_name = models.CharField(
        max_length=255,
        choices=get_solutions,  # type:ignore This works in Django5.0 but Pylance does not think so
        blank=True,
        null=True,
    )
    component_1_volume = models.FloatField(blank=True, null=True)
    component_1_unit = models.CharField(
        max_length=5,
        choices=(("uL", "uL"), ("mg", "mg"), ("units", "units")),
        blank=True,
        null=True,
    )

    component_2_name = models.CharField(
        max_length=255,
        choices=get_solutions,  # type:ignore This works in Django5.0 but Pylance does not think so
        blank=True,
        null=True,
    )
    component_2_volume = models.FloatField(blank=True, null=True)
    component_2_unit = models.CharField(
        max_length=5,
        choices=(("uL", "uL"), ("mg", "mg"), ("units", "units")),
        blank=True,
        null=True,
    )

    component_3_name = models.CharField(
        max_length=255,
        choices=get_solutions,  # type:ignore This works in Django5.0 but Pylance does not think so
        blank=True,
        null=True,
    )
    component_3_volume = models.FloatField(blank=True, null=True)
    component_3_unit = models.CharField(
        max_length=5,
        choices=(("uL", "uL"), ("mg", "mg"), ("units", "units")),
        blank=True,
        null=True,
    )

    component_4_name = models.CharField(
        max_length=255,
        choices=get_solutions,  # type:ignore This works in Django5.0 but Pylance does not think so
        blank=True,
        null=True,
    )
    component_4_volume = models.FloatField(blank=True, null=True)
    component_4_unit = models.CharField(
        max_length=5,
        choices=(("uL", "uL"), ("mg", "mg"), ("units", "units")),
        blank=True,
        null=True,
    )

    component_5_name = models.CharField(
        max_length=255,
        choices=get_solutions,  # type:ignore This works in Django5.0 but Pylance does not think so
        blank=True,
        null=True,
    )
    component_5_volume = models.FloatField(blank=True, null=True)
    component_5_unit = models.CharField(
        max_length=5,
        choices=(("uL", "uL"), ("mg", "mg"), ("units", "units")),
        blank=True,
        null=True,
    )

    component_6_name = models.CharField(
        max_length=255,
        choices=get_solutions,  # type:ignore This works in Django5.0 but Pylance does not think so
        blank=True,
        null=True,
    )
    component_6_volume = models.FloatField(blank=True, null=True)
    component_6_unit = models.CharField(
        max_length=5,
        choices=(("uL", "uL"), ("mg", "mg"), ("units", "units")),
        blank=True,
        null=True,
    )

    component_7_name = models.CharField(
        max_length=255,
        choices=get_solutions,  # type:ignore This works in Django5.0 but Pylance does not think so
        blank=True,
        null=True,
    )
    component_7_volume = models.FloatField(blank=True, null=True)
    component_7_unit = models.CharField(
        max_length=5,
        choices=(("uL", "uL"), ("mg", "mg"), ("units", "units")),
        blank=True,
        null=True,
    )

    component_8_name = models.CharField(
        max_length=255,
        choices=get_solutions,  # type:ignore This works in Django5.0 but Pylance does not think so
        blank=True,
        null=True,
    )
    component_8_volume = models.FloatField(blank=True, null=True)
    component_8_unit = models.CharField(
        max_length=5,
        choices=(("uL", "uL"), ("mg", "mg"), ("units", "units")),
        blank=True,
        null=True,
    )

    component_9_name = models.CharField(
        max_length=255,
        choices=get_solutions,  # type:ignore This works in Django5.0 but Pylance does not think so
        blank=True,
        null=True,
    )
    component_9_volume = models.FloatField(blank=True, null=True)
    component_9_unit = models.CharField(
        max_length=5,
        choices=(("uL", "uL"), ("mg", "mg"), ("units", "units")),
        blank=True,
        null=True,
    )
