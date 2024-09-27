from __future__ import annotations

from abc import abstractmethod

from django.db import models

from excel.definitions import SolutionDefinitionExcelDefinition


class SolutionBase(models.Model):
    name = models.CharField(max_length=255, unique=True)
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
        blank=True,
    )
    component_1_amount = models.FloatField(blank=True, null=True)
    component_1_unit = models.CharField(
        max_length=5,
        choices=(("uL", "uL"), ("mg", "mg"), ("units", "units")),
        blank=True,
    )

    component_2_name = models.CharField(
        max_length=255,
        blank=True,
    )
    component_2_amount = models.FloatField(blank=True, null=True)
    component_2_unit = models.CharField(
        max_length=5,
        choices=(("uL", "uL"), ("mg", "mg"), ("units", "units")),
        blank=True,
    )

    component_3_name = models.CharField(
        max_length=255,
        blank=True,
    )
    component_3_amount = models.FloatField(blank=True, null=True)
    component_3_unit = models.CharField(
        max_length=5,
        choices=(("uL", "uL"), ("mg", "mg"), ("units", "units")),
        blank=True,
    )

    component_4_name = models.CharField(
        max_length=255,
        blank=True,
    )
    component_4_amount = models.FloatField(blank=True, null=True)
    component_4_unit = models.CharField(
        max_length=5,
        choices=(("uL", "uL"), ("mg", "mg"), ("units", "units")),
        blank=True,
    )

    component_5_name = models.CharField(
        max_length=255,
        blank=True,
    )
    component_5_amount = models.FloatField(blank=True, null=True)
    component_5_unit = models.CharField(
        max_length=5,
        choices=(("uL", "uL"), ("mg", "mg"), ("units", "units")),
        blank=True,
    )

    component_6_name = models.CharField(
        max_length=255,
        blank=True,
    )
    component_6_amount = models.FloatField(blank=True, null=True)
    component_6_unit = models.CharField(
        max_length=5,
        choices=(("uL", "uL"), ("mg", "mg"), ("units", "units")),
        blank=True,
    )

    component_7_name = models.CharField(
        max_length=255,
        blank=True,
    )
    component_7_amount = models.FloatField(blank=True, null=True)
    component_7_unit = models.CharField(
        max_length=5,
        choices=(("uL", "uL"), ("mg", "mg"), ("units", "units")),
        blank=True,
    )

    component_8_name = models.CharField(
        max_length=255,
        blank=True,
    )
    component_8_amount = models.FloatField(blank=True, null=True)
    component_8_unit = models.CharField(
        max_length=5,
        choices=(("uL", "uL"), ("mg", "mg"), ("units", "units")),
        blank=True,
    )

    component_9_name = models.CharField(
        max_length=255,
        blank=True,
    )
    component_9_amount = models.FloatField(blank=True, null=True)
    component_9_unit = models.CharField(
        max_length=5,
        choices=(("uL", "uL"), ("mg", "mg"), ("units", "units")),
        blank=True,
    )

    class Meta:
        abstract = True

    @abstractmethod
    def get_excel_definition(self) -> SolutionDefinitionExcelDefinition:
        definition = SolutionDefinitionExcelDefinition(
            name=self.name,
            liquid_type=self.liquid_type,
            volatility=self.volatility,
            viscosity=self.viscosity,
            homogeneity=self.homogeneity,
            storage_condition=self.storage_condition,
        )

        if (
            self.component_1_name != ""
            and self.component_1_unit != ""
            and self.component_1_amount is not None
        ):
            definition.add_component(
                name=self.component_1_name,
                amount=self.component_1_amount,
                unit=self.component_1_unit,  # type: ignore[reportArgumentType]
            )

        if (
            self.component_2_name != ""
            and self.component_2_unit != ""
            and self.component_2_amount is not None
        ):
            definition.add_component(
                name=self.component_2_name,
                amount=self.component_2_amount,
                unit=self.component_2_unit,  # type: ignore[reportArgumentType]
            )

        if (
            self.component_3_name != ""
            and self.component_3_unit != ""
            and self.component_3_amount is not None
        ):
            definition.add_component(
                name=self.component_3_name,
                amount=self.component_3_amount,
                unit=self.component_3_unit,  # type: ignore[reportArgumentType]
            )

        if (
            self.component_4_name != ""
            and self.component_4_unit != ""
            and self.component_4_amount is not None
        ):
            definition.add_component(
                name=self.component_4_name,
                amount=self.component_4_amount,
                unit=self.component_4_unit,  # type: ignore[reportArgumentType]
            )

        if (
            self.component_5_name != ""
            and self.component_5_unit != ""
            and self.component_5_amount is not None
        ):
            definition.add_component(
                name=self.component_5_name,
                amount=self.component_5_amount,
                unit=self.component_5_unit,  # type: ignore[reportArgumentType]
            )

        if (
            self.component_6_name != ""
            and self.component_6_unit != ""
            and self.component_6_amount is not None
        ):
            definition.add_component(
                name=self.component_6_name,
                amount=self.component_6_amount,
                unit=self.component_6_unit,  # type: ignore[reportArgumentType]
            )

        if (
            self.component_7_name != ""
            and self.component_7_unit != ""
            and self.component_7_amount is not None
        ):
            definition.add_component(
                name=self.component_7_name,
                amount=self.component_7_amount,
                unit=self.component_7_unit,  # type: ignore[reportArgumentType]
            )

        if (
            self.component_8_name != ""
            and self.component_8_unit != ""
            and self.component_8_amount is not None
        ):
            definition.add_component(
                name=self.component_8_name,
                amount=self.component_8_amount,
                unit=self.component_8_unit,  # type: ignore[reportArgumentType]
            )

        if (
            self.component_9_name != ""
            and self.component_9_unit != ""
            and self.component_9_amount is not None
        ):
            definition.add_component(
                name=self.component_9_name,
                amount=self.component_9_amount,
                unit=self.component_9_unit,  # type: ignore[reportArgumentType]
            )

        return definition

    def __str__(self) -> str:
        return self.name
