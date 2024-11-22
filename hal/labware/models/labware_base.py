from __future__ import annotations

from typing import cast

from django.core.exceptions import ValidationError
from django.db import models
from polymorphic.models import PolymorphicModel


def _grip_regions_default() -> list[float]:
    return [0, 3, 10]


def _x_y_z_dimensions_default() -> list[tuple[float, float, float]]:
    return [(127.5, 82, 0), (128, 83, 10)]


class LabwareBase(PolymorphicModel):
    identifier = models.CharField(max_length=255, unique=True, primary_key=True)

    width_depth_height_dimensions: models.JSONField[
        list[tuple[float, float, float]]
    ] = models.JSONField(
        help_text="Plates are not inheritantly a cube. This property defines how the rectangular shape of the plate changes across heights. Labware is assumed to be landscape such that long side is width (ex. 127mm) and short side is depth (ex. 82mm).",
        default=_x_y_z_dimensions_default,
        verbose_name="X Y Z dimensions",
    )

    short_side_grip_heights: models.JSONField[list[float]] = models.JSONField(
        help_text="Which Z heights are acceptable to be gripped on the short side when transported. Relative to bottom. If not transportable then empty brackets.",
        default=_grip_regions_default,
        verbose_name="Short side Z grip heights",
    )

    long_side_grip_heights: models.JSONField[list[float]] = models.JSONField(
        help_text="Which Z heights are acceptable to be gripped on the long side when transported. Relative to bottom. If not transportable then empty brackets.",
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

    def __str__(self) -> str:
        return f"{self.identifier} ({self.pk})"

    class Meta:
        ordering = ["identifier"]

    @property
    def max_width(self) -> float:
        return max([width for width, _, _ in self.width_depth_height_dimensions])

    def get_width_at_height(self, height: float) -> float:
        for width_dimension, _, height_dimension in self.width_depth_height_dimensions:
            if height >= height_dimension:
                return width_dimension

        raise ValueError(
            "Cannot get width at height. It does not fall within the labware.",
        )

    @property
    def max_depth(self) -> float:
        return max([depth for _, depth, _ in self.width_depth_height_dimensions])

    def get_depth_at_height(self, height: float) -> float:
        for _, depth_dimension, height_dimension in self.width_depth_height_dimensions:
            if height >= height_dimension:
                return depth_dimension

        raise ValueError(
            "Cannot get depth at height. It does not fall within the labware.",
        )

    @property
    def height(self) -> float:
        return sum([height for _, _, height in self.width_depth_height_dimensions])

    def clean(self) -> None:
        dimensions = cast(
            list[tuple[float, float, float]],
            self.width_depth_height_dimensions,
        )

        try:
            for index, (width, depth, height) in enumerate(dimensions):
                if len(dimensions[index]) != 3:
                    raise ValueError  # noqa:TRY301

                dimensions[index] = (float(width), float(depth), float(height))

        except ValueError as e:
            raise ValidationError(
                "'width_depth_height_dimensions' is incorrect. Expected list of tuples. Ex: [(127,82,0),(127.5,82,5),(127.25,82.5,0)]",
            ) from e

        if len(dimensions) != len({height for _, _, height in dimensions}):
            raise ValidationError(
                "'width_depth_height_dimensions' is incorrect. Duplicate height values are present.",
            )

        self.width_depth_height_dimensions = sorted(dimensions, key=lambda x: x[0])

        regions = self.short_side_grip_heights

        try:
            for index, region in enumerate(regions):
                regions[index] = float(region)

        except ValueError as e:
            raise ValidationError(
                "'short_side_z_grip_heights' is incorrect. Expected list of numbers. Ex: [2,5,10]",
            ) from e

        self.short_side_grip_heights = sorted(regions)

        regions = self.long_side_grip_heights

        try:
            for index, region in enumerate(regions):
                regions[index] = float(region)

        except ValueError as e:
            raise ValidationError(
                "'long_side_z_grip_heights' is incorrect. Expected list of numbers. Ex: [2,5,10]",
            ) from e

        self.long_side_grip_heights = sorted(regions)

        if (
            self.addressing_direction != "Column-wise"
            and self.addressing_direction != "Row-wise"
        ):
            raise ValidationError(
                "'addressing_direction' is incorrect. Expected either 'Column-wise' or 'Row-wise'",
            )

        return super().clean()
