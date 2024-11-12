from __future__ import annotations

from django.db import models
from polymorphic.models import PolymorphicModel

from hal.container.models import Container


class Labware(PolymorphicModel):
    identifier = models.CharField(max_length=255, unique=True, primary_key=True)

    x_y_z_dimensions: models.JSONField[list[tuple[float, float, float]]] = (
        models.JSONField(
            help_text="Plates are not inheritantly a cube. This property defined how the rectangular shape of the plate changes across z heights.",
        )
    )

    short_side_z_grip_regions: models.JSONField[list[float]] = models.JSONField(
        help_text="Which regions are acceptable to be gripped on the short side when transported. Relative to bottom.",
    )

    long_side_z_grip_regions: models.JSONField[list[float]] = models.JSONField(
        help_text="Which regions are acceptable to be gripped on the long side when transported. Relative to bottom.",
    )

    addressable_rows = models.PositiveSmallIntegerField(
        help_text="How many container rows the labware item has. Labware definition specific.",
    )
    addressable_columns = models.PositiveSmallIntegerField(
        help_text="How many container columns the labware item has. Labware definition specific.",
    )
    addressing_direction = models.CharField(
        max_length=11,
        choices=(("Column-wise", "Column-wise"), ("Row-wise", "Row-wise")),
        help_text="How container positions are ordered. Labware definition specific.",
    )

    def __str__(self) -> str:
        return self.identifier

    class Meta:
        ordering = ["identifier"]


class NonPipettableLabware(Labware): ...


class PipettableLabware(Labware):
    container = models.ForeignKey(to=Container, on_delete=models.CASCADE)


class StackedLabwareZHeightChange(models.Model):
    bottom_labware = models.ForeignKey(
        to=Labware,
        on_delete=models.CASCADE,
        help_text="The bottom labware of the stack.",
        related_name="stackedlabwarezheightchangebottom_set",
    )
    top_labware = models.ForeignKey(
        to=Labware,
        on_delete=models.CASCADE,
        help_text="The top labware of the stack.",
        related_name="stackedlabwarezheightchangetop_set",
    )
    z_height_change = models.FloatField()
