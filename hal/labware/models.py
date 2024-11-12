from __future__ import annotations

from typing import cast

from django.core.exceptions import ValidationError
from django.db import models
from polymorphic.models import PolymorphicModel

from hal.container.models import Container


def _grip_regions_default() -> list[float]:
    return [0, 3, 10]


def _x_y_z_dimensions_default() -> list[tuple[float, float, float]]:
    return [(127.5, 82, 0), (128, 83, 10)]


class Labware(PolymorphicModel):
    identifier = models.CharField(max_length=255, unique=True, primary_key=True)

    x_y_z_dimensions: models.JSONField[list[tuple[float, float, float]]] = (
        models.JSONField(
            help_text="Plates are not inheritantly a cube. This property defines how the rectangular shape of the plate changes across z heights. Labware is assumed to be landscape such that X is length of the long side (ex. 127mm) and Y is the length of the short side (ex. 82mm).",
            default=_x_y_z_dimensions_default,
            verbose_name="X Y Z dimensions",
        )
    )

    short_side_z_grip_heights: models.JSONField[list[float]] = models.JSONField(
        help_text="Which Z heights are acceptable to be gripped on the short side when transported. Relative to bottom.",
        default=_grip_regions_default,
        verbose_name="Short side Z grip heights",
    )

    long_side_z_grip_heights: models.JSONField[list[float]] = models.JSONField(
        help_text="Which Z heights are acceptable to be gripped on the long side when transported. Relative to bottom.",
        default=_grip_regions_default,
        verbose_name="Long side Z grip heights",
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
        help_text="How the container positions are ordered. Labware definition specific.",
    )

    def clean(self) -> None:
        dimensions = cast(list[tuple[float, float, float]], self.x_y_z_dimensions)

        try:
            for index, (x, y, z) in enumerate(dimensions):
                if len(dimensions[index]) != 3:
                    raise ValueError  # noqa:TRY301

                dimensions[index] = (float(y), float(x), float(z))

        except ValueError as e:
            raise ValidationError(
                "'x_y_z_dimensions' is incorrect. Expected list of tuples. Ex: [(127,82,0),(127.5,82,5),(127.25,82.5,0)]",
            ) from e

        if len(dimensions) != len({z for _, _, z in dimensions}):
            raise ValidationError(
                "'x_y_z_dimensions' is incorrect. Duplicate z values are present.",
            )

        self.x_y_z_dimensions = sorted(dimensions, key=lambda x: x[0])

        regions = self.short_side_z_grip_heights

        try:
            for index, region in enumerate(regions):
                regions[index] = float(region)

        except ValueError as e:
            raise ValidationError(
                "'short_side_z_grip_heights' is incorrect. Expected list of numbers. Ex: [2,5,10]",
            ) from e

        self.short_side_z_grip_heights = sorted(regions)

        regions = self.long_side_z_grip_heights

        try:
            for index, region in enumerate(regions):
                regions[index] = float(region)

        except ValueError as e:
            raise ValidationError(
                "'long_side_z_grip_heights' is incorrect. Expected list of numbers. Ex: [2,5,10]",
            ) from e

        self.long_side_z_grip_heights = sorted(regions)

        if (
            self.addressing_direction != "Column-wise"
            and self.addressing_direction != "Row-wise"
        ):
            raise ValidationError(
                "'addressing_direction' is incorrect. Expected either 'Column-wise' or 'Row-wise'",
            )

        return super().clean()

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
