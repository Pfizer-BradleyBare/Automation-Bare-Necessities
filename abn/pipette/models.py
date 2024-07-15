from backend.models import BackendBase
from django.db import models
from labware.models import LabwareBase
from multiselectfield import MultiSelectField
from polymorphic.models import PolymorphicModel
from tip.models import TipBase


class LiquidClass(models.Model):

    liquid_class_name = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        blank=False,
        null=False,
        help_text="Liquid class name as defined in the Hamilton liquid class editor.",
    )
    min_volume = models.FloatField()
    max_volume = models.FloatField()

    def __str__(self) -> str:
        return self.liquid_class_name

    class Meta:
        ordering = ["liquid_class_name"]


class LiquidClassCategory(models.Model):
    identifier = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        blank=False,
        null=False,
    )
    category = models.CharField(
        max_length=81,
        choices=[
            (
                "Viscosity:Low; Volatility:Low; Homogeneity:Homogenous; Polarity:Non_Polar",
                "Viscosity:Low; Volatility:Low; Homogeneity:Homogenous; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Low; Volatility:Low; Homogeneity:Homogenous; Polarity:Polar",
                "Viscosity:Low; Volatility:Low; Homogeneity:Homogenous; Polarity:Polar",
            ),
            (
                "Viscosity:Low; Volatility:Low; Homogeneity:Emulsion; Polarity:Non_Polar",
                "Viscosity:Low; Volatility:Low; Homogeneity:Emulsion; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Low; Volatility:Low; Homogeneity:Emulsion; Polarity:Polar",
                "Viscosity:Low; Volatility:Low; Homogeneity:Emulsion; Polarity:Polar",
            ),
            (
                "Viscosity:Low; Volatility:Low; Homogeneity:Suspension; Polarity:Non_Polar",
                "Viscosity:Low; Volatility:Low; Homogeneity:Suspension; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Low; Volatility:Low; Homogeneity:Suspension; Polarity:Polar",
                "Viscosity:Low; Volatility:Low; Homogeneity:Suspension; Polarity:Polar",
            ),
            (
                "Viscosity:Low; Volatility:Low; Homogeneity:Heterogenous; Polarity:Non_Polar",
                "Viscosity:Low; Volatility:Low; Homogeneity:Heterogenous; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Low; Volatility:Low; Homogeneity:Heterogenous; Polarity:Polar",
                "Viscosity:Low; Volatility:Low; Homogeneity:Heterogenous; Polarity:Polar",
            ),
            (
                "Viscosity:Low; Volatility:Medium; Homogeneity:Homogenous; Polarity:Non_Polar",
                "Viscosity:Low; Volatility:Medium; Homogeneity:Homogenous; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Low; Volatility:Medium; Homogeneity:Homogenous; Polarity:Polar",
                "Viscosity:Low; Volatility:Medium; Homogeneity:Homogenous; Polarity:Polar",
            ),
            (
                "Viscosity:Low; Volatility:Medium; Homogeneity:Emulsion; Polarity:Non_Polar",
                "Viscosity:Low; Volatility:Medium; Homogeneity:Emulsion; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Low; Volatility:Medium; Homogeneity:Emulsion; Polarity:Polar",
                "Viscosity:Low; Volatility:Medium; Homogeneity:Emulsion; Polarity:Polar",
            ),
            (
                "Viscosity:Low; Volatility:Medium; Homogeneity:Suspension; Polarity:Non_Polar",
                "Viscosity:Low; Volatility:Medium; Homogeneity:Suspension; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Low; Volatility:Medium; Homogeneity:Suspension; Polarity:Polar",
                "Viscosity:Low; Volatility:Medium; Homogeneity:Suspension; Polarity:Polar",
            ),
            (
                "Viscosity:Low; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Non_Polar",
                "Viscosity:Low; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Low; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Polar",
                "Viscosity:Low; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Polar",
            ),
            (
                "Viscosity:Low; Volatility:High; Homogeneity:Homogenous; Polarity:Non_Polar",
                "Viscosity:Low; Volatility:High; Homogeneity:Homogenous; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Low; Volatility:High; Homogeneity:Homogenous; Polarity:Polar",
                "Viscosity:Low; Volatility:High; Homogeneity:Homogenous; Polarity:Polar",
            ),
            (
                "Viscosity:Low; Volatility:High; Homogeneity:Emulsion; Polarity:Non_Polar",
                "Viscosity:Low; Volatility:High; Homogeneity:Emulsion; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Low; Volatility:High; Homogeneity:Emulsion; Polarity:Polar",
                "Viscosity:Low; Volatility:High; Homogeneity:Emulsion; Polarity:Polar",
            ),
            (
                "Viscosity:Low; Volatility:High; Homogeneity:Suspension; Polarity:Non_Polar",
                "Viscosity:Low; Volatility:High; Homogeneity:Suspension; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Low; Volatility:High; Homogeneity:Suspension; Polarity:Polar",
                "Viscosity:Low; Volatility:High; Homogeneity:Suspension; Polarity:Polar",
            ),
            (
                "Viscosity:Low; Volatility:High; Homogeneity:Heterogenous; Polarity:Non_Polar",
                "Viscosity:Low; Volatility:High; Homogeneity:Heterogenous; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Low; Volatility:High; Homogeneity:Heterogenous; Polarity:Polar",
                "Viscosity:Low; Volatility:High; Homogeneity:Heterogenous; Polarity:Polar",
            ),
            (
                "Viscosity:Medium; Volatility:Low; Homogeneity:Homogenous; Polarity:Non_Polar",
                "Viscosity:Medium; Volatility:Low; Homogeneity:Homogenous; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Medium; Volatility:Low; Homogeneity:Homogenous; Polarity:Polar",
                "Viscosity:Medium; Volatility:Low; Homogeneity:Homogenous; Polarity:Polar",
            ),
            (
                "Viscosity:Medium; Volatility:Low; Homogeneity:Emulsion; Polarity:Non_Polar",
                "Viscosity:Medium; Volatility:Low; Homogeneity:Emulsion; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Medium; Volatility:Low; Homogeneity:Emulsion; Polarity:Polar",
                "Viscosity:Medium; Volatility:Low; Homogeneity:Emulsion; Polarity:Polar",
            ),
            (
                "Viscosity:Medium; Volatility:Low; Homogeneity:Suspension; Polarity:Non_Polar",
                "Viscosity:Medium; Volatility:Low; Homogeneity:Suspension; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Medium; Volatility:Low; Homogeneity:Suspension; Polarity:Polar",
                "Viscosity:Medium; Volatility:Low; Homogeneity:Suspension; Polarity:Polar",
            ),
            (
                "Viscosity:Medium; Volatility:Low; Homogeneity:Heterogenous; Polarity:Non_Polar",
                "Viscosity:Medium; Volatility:Low; Homogeneity:Heterogenous; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Medium; Volatility:Low; Homogeneity:Heterogenous; Polarity:Polar",
                "Viscosity:Medium; Volatility:Low; Homogeneity:Heterogenous; Polarity:Polar",
            ),
            (
                "Viscosity:Medium; Volatility:Medium; Homogeneity:Homogenous; Polarity:Non_Polar",
                "Viscosity:Medium; Volatility:Medium; Homogeneity:Homogenous; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Medium; Volatility:Medium; Homogeneity:Homogenous; Polarity:Polar",
                "Viscosity:Medium; Volatility:Medium; Homogeneity:Homogenous; Polarity:Polar",
            ),
            (
                "Viscosity:Medium; Volatility:Medium; Homogeneity:Emulsion; Polarity:Non_Polar",
                "Viscosity:Medium; Volatility:Medium; Homogeneity:Emulsion; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Medium; Volatility:Medium; Homogeneity:Emulsion; Polarity:Polar",
                "Viscosity:Medium; Volatility:Medium; Homogeneity:Emulsion; Polarity:Polar",
            ),
            (
                "Viscosity:Medium; Volatility:Medium; Homogeneity:Suspension; Polarity:Non_Polar",
                "Viscosity:Medium; Volatility:Medium; Homogeneity:Suspension; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Medium; Volatility:Medium; Homogeneity:Suspension; Polarity:Polar",
                "Viscosity:Medium; Volatility:Medium; Homogeneity:Suspension; Polarity:Polar",
            ),
            (
                "Viscosity:Medium; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Non_Polar",
                "Viscosity:Medium; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Medium; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Polar",
                "Viscosity:Medium; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Polar",
            ),
            (
                "Viscosity:Medium; Volatility:High; Homogeneity:Homogenous; Polarity:Non_Polar",
                "Viscosity:Medium; Volatility:High; Homogeneity:Homogenous; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Medium; Volatility:High; Homogeneity:Homogenous; Polarity:Polar",
                "Viscosity:Medium; Volatility:High; Homogeneity:Homogenous; Polarity:Polar",
            ),
            (
                "Viscosity:Medium; Volatility:High; Homogeneity:Emulsion; Polarity:Non_Polar",
                "Viscosity:Medium; Volatility:High; Homogeneity:Emulsion; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Medium; Volatility:High; Homogeneity:Emulsion; Polarity:Polar",
                "Viscosity:Medium; Volatility:High; Homogeneity:Emulsion; Polarity:Polar",
            ),
            (
                "Viscosity:Medium; Volatility:High; Homogeneity:Suspension; Polarity:Non_Polar",
                "Viscosity:Medium; Volatility:High; Homogeneity:Suspension; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Medium; Volatility:High; Homogeneity:Suspension; Polarity:Polar",
                "Viscosity:Medium; Volatility:High; Homogeneity:Suspension; Polarity:Polar",
            ),
            (
                "Viscosity:Medium; Volatility:High; Homogeneity:Heterogenous; Polarity:Non_Polar",
                "Viscosity:Medium; Volatility:High; Homogeneity:Heterogenous; Polarity:Non-Polar",
            ),
            (
                "Viscosity:Medium; Volatility:High; Homogeneity:Heterogenous; Polarity:Polar",
                "Viscosity:Medium; Volatility:High; Homogeneity:Heterogenous; Polarity:Polar",
            ),
            (
                "Viscosity:High; Volatility:Low; Homogeneity:Homogenous; Polarity:Non_Polar",
                "Viscosity:High; Volatility:Low; Homogeneity:Homogenous; Polarity:Non-Polar",
            ),
            (
                "Viscosity:High; Volatility:Low; Homogeneity:Homogenous; Polarity:Polar",
                "Viscosity:High; Volatility:Low; Homogeneity:Homogenous; Polarity:Polar",
            ),
            (
                "Viscosity:High; Volatility:Low; Homogeneity:Emulsion; Polarity:Non_Polar",
                "Viscosity:High; Volatility:Low; Homogeneity:Emulsion; Polarity:Non-Polar",
            ),
            (
                "Viscosity:High; Volatility:Low; Homogeneity:Emulsion; Polarity:Polar",
                "Viscosity:High; Volatility:Low; Homogeneity:Emulsion; Polarity:Polar",
            ),
            (
                "Viscosity:High; Volatility:Low; Homogeneity:Suspension; Polarity:Non_Polar",
                "Viscosity:High; Volatility:Low; Homogeneity:Suspension; Polarity:Non-Polar",
            ),
            (
                "Viscosity:High; Volatility:Low; Homogeneity:Suspension; Polarity:Polar",
                "Viscosity:High; Volatility:Low; Homogeneity:Suspension; Polarity:Polar",
            ),
            (
                "Viscosity:High; Volatility:Low; Homogeneity:Heterogenous; Polarity:Non_Polar",
                "Viscosity:High; Volatility:Low; Homogeneity:Heterogenous; Polarity:Non-Polar",
            ),
            (
                "Viscosity:High; Volatility:Low; Homogeneity:Heterogenous; Polarity:Polar",
                "Viscosity:High; Volatility:Low; Homogeneity:Heterogenous; Polarity:Polar",
            ),
            (
                "Viscosity:High; Volatility:Medium; Homogeneity:Homogenous; Polarity:Non_Polar",
                "Viscosity:High; Volatility:Medium; Homogeneity:Homogenous; Polarity:Non-Polar",
            ),
            (
                "Viscosity:High; Volatility:Medium; Homogeneity:Homogenous; Polarity:Polar",
                "Viscosity:High; Volatility:Medium; Homogeneity:Homogenous; Polarity:Polar",
            ),
            (
                "Viscosity:High; Volatility:Medium; Homogeneity:Emulsion; Polarity:Non_Polar",
                "Viscosity:High; Volatility:Medium; Homogeneity:Emulsion; Polarity:Non-Polar",
            ),
            (
                "Viscosity:High; Volatility:Medium; Homogeneity:Emulsion; Polarity:Polar",
                "Viscosity:High; Volatility:Medium; Homogeneity:Emulsion; Polarity:Polar",
            ),
            (
                "Viscosity:High; Volatility:Medium; Homogeneity:Suspension; Polarity:Non_Polar",
                "Viscosity:High; Volatility:Medium; Homogeneity:Suspension; Polarity:Non-Polar",
            ),
            (
                "Viscosity:High; Volatility:Medium; Homogeneity:Suspension; Polarity:Polar",
                "Viscosity:High; Volatility:Medium; Homogeneity:Suspension; Polarity:Polar",
            ),
            (
                "Viscosity:High; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Non_Polar",
                "Viscosity:High; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Non-Polar",
            ),
            (
                "Viscosity:High; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Polar",
                "Viscosity:High; Volatility:Medium; Homogeneity:Heterogenous; Polarity:Polar",
            ),
            (
                "Viscosity:High; Volatility:High; Homogeneity:Homogenous; Polarity:Non_Polar",
                "Viscosity:High; Volatility:High; Homogeneity:Homogenous; Polarity:Non-Polar",
            ),
            (
                "Viscosity:High; Volatility:High; Homogeneity:Homogenous; Polarity:Polar",
                "Viscosity:High; Volatility:High; Homogeneity:Homogenous; Polarity:Polar",
            ),
            (
                "Viscosity:High; Volatility:High; Homogeneity:Emulsion; Polarity:Non_Polar",
                "Viscosity:High; Volatility:High; Homogeneity:Emulsion; Polarity:Non-Polar",
            ),
            (
                "Viscosity:High; Volatility:High; Homogeneity:Emulsion; Polarity:Polar",
                "Viscosity:High; Volatility:High; Homogeneity:Emulsion; Polarity:Polar",
            ),
            (
                "Viscosity:High; Volatility:High; Homogeneity:Suspension; Polarity:Non_Polar",
                "Viscosity:High; Volatility:High; Homogeneity:Suspension; Polarity:Non-Polar",
            ),
            (
                "Viscosity:High; Volatility:High; Homogeneity:Suspension; Polarity:Polar",
                "Viscosity:High; Volatility:High; Homogeneity:Suspension; Polarity:Polar",
            ),
            (
                "Viscosity:High; Volatility:High; Homogeneity:Heterogenous; Polarity:Non_Polar",
                "Viscosity:High; Volatility:High; Homogeneity:Heterogenous; Polarity:Non-Polar",
            ),
            (
                "Viscosity:High; Volatility:High; Homogeneity:Heterogenous; Polarity:Polar",
                "Viscosity:High; Volatility:High; Homogeneity:Heterogenous; Polarity:Polar",
            ),
        ],
    )
    liquid_classes = models.ManyToManyField(to=LiquidClass)

    def __str__(self) -> str:
        return self.identifier

    class Meta:
        ordering = ["identifier"]


class PipetteTip(models.Model):

    tip = models.ForeignKey(to=TipBase, on_delete=models.CASCADE)
    tip_support_dropoff_labware_id = models.CharField(max_length=100)
    tip_support_pickup_labware_id = models.CharField(max_length=100)

    supported_aspirate_liquid_class_categories = models.ManyToManyField(
        to=LiquidClassCategory,
        related_name="+",
    )
    supported_dispense_liquid_class_categories = models.ManyToManyField(
        to=LiquidClassCategory,
        related_name="+",
    )

    class Meta:
        ordering = ["tip"]


class PipetteBase(PolymorphicModel):
    class Meta:
        ordering = ["identifier"]

    identifier = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        blank=False,
        null=False,
    )

    enabled = models.BooleanField(default=True)

    backend = models.ForeignKey(to=BackendBase, on_delete=models.CASCADE)

    supported_tips = models.ManyToManyField(to=PipetteTip)
    supported_dispense_labware = models.ManyToManyField(
        to=LabwareBase,
        related_name="+",
    )
    supported_aspirate_labware = models.ManyToManyField(
        to=LabwareBase,
        related_name="+",
    )

    waste_labware_id = models.CharField(max_length=100)


class HamiltonPortraitCORE8(PipetteBase):
    active_channels = MultiSelectField(
        choices=(
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
            ("6", "6"),
            ("7", "7"),
            ("8", "8"),
            ("9", "9"),
            ("10", "10"),
            ("11", "11"),
            ("12", "12"),
            ("13", "13"),
            ("14", "14"),
            ("15", "15"),
            ("16", "16"),
        ),
    )


class HamiltonPortraitCORE8SimpleContentDispense(HamiltonPortraitCORE8): ...
