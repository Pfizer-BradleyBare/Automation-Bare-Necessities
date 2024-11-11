from __future__ import annotations

from itertools import pairwise

from django.core.exceptions import ValidationError
from django.db import models


class Container(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
    )

    simultaneous_tips = models.PositiveSmallIntegerField(
        help_text="How many tips can fit in the container at the same time",
    )

    max_volume = models.FloatField(help_text="Max volume of a container.")

    dead_volume = models.FloatField(
        help_text="Minimum volume required in a container for successful aspiration.",
    )

    shape_definition: models.JSONField[list[tuple[float, float]]] = models.JSONField(
        help_text="A list of [volume uL, height mm] pairs, in volume order, that define the shape of a container. Pipetting accurately in a container requires an accurate container shape definition.",
        default=[
            ("Volume 1", "Height 1"),
            ("Volume 2", "Height 2"),
            ("Volume ...", "Height ..."),
        ],
    )

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    def clean(self) -> None:
        defintion = self.shape_definition

        try:
            for index, (volume, height) in enumerate(defintion):
                if len(defintion[index]) != 2:
                    raise ValidationError(
                        "'Shape definition' can only contain pairwise number values in volume order. Ex: [[0,0],[1,1],[10,10]]",
                    )

                defintion[index] = (float(volume), float(height))
        except ValueError as e:
            raise ValidationError(
                "'Shape definition' can only contain pairwise number values in volume order. Ex: [[0,0],[1,1],[10,10]]",
            ) from e

        defintion = sorted(defintion, key=lambda x: x[0])

        volume, height = defintion[0]

        if volume != 0 and height != 0:
            defintion.insert(0, (0, 0))

        pairs = pairwise(defintion)

        self.shape_definition = defintion

        for index, ((v1, h1), (v2, h2)) in enumerate(pairs):
            if h1 > h2 or v1 > v2:
                raise ValidationError(
                    f"'Shape definition' does not make sense. Entry #{index+1} is has values greater than entry #{index+2}",
                )
            if h1 == h2 or v1 == v2:
                raise ValidationError(
                    f"'Shape definition' does not make sense. Entry #{index+1} is has values equal to entry #{index+2}",
                )

    def interpolate_volume(self: Container, volume: float) -> float:
        """Calculate height at a given volume."""
        if volume <= 0:
            return 0

        definition = self.shape_definition
        definition.append((0.0, 0.0))
        definition = sorted(definition, key=lambda x: x[0])
        # Add a zero case assuming it does not exist then sort. Should not make a huge difference performance wise.

        interpolation_points = list(pairwise(definition))

        points = interpolation_points[-1]
        # edge case where we may not find points to interpolate. This will extrapolate past the last two points on the curve.

        for p1, p2 in interpolation_points:
            v1, _ = p1
            v2, _ = p2

            if v1 <= volume <= v2:
                points = (p1, p2)
        # Find the points where our volume falls if it does

        p1, p2 = points

        # NOTE: height is our rise or Y and volume is our run or X

        v1, h1 = p1
        v2, h2 = p2

        rise = h2 - h1
        run = v2 - v1

        if rise == 0 or run == 0:
            return h1

        m = rise / run
        x = volume - v1
        b = h1

        return m * x + b

    def interpolate_height(self: Container, height: float) -> float:
        """Calculate volume at a given height."""
        if height <= 0:
            return 0

        definition = self.shape_definition
        definition.append((0.0, 0.0))
        definition = sorted(definition, key=lambda x: x[0])
        # Add a zero case assuming it does not exist then sort. Should not make a huge difference performance wise.

        interpolation_points = list(pairwise(definition))

        points = interpolation_points[-1]
        # edge case where we may not find points to interpolate. This will extrapolate past the last two points on the curve.

        for p1, p2 in interpolation_points:
            _, h1 = p1
            _, h2 = p2

            if h1 <= height <= h2:
                points = (p1, p2)
        # Find the points where our height falls if it does

        p1, p2 = points

        # NOTE: height is our run or X and volume is our rise or Y

        v1, h1 = p1
        v2, h2 = p2

        rise = v2 - v1
        run = h2 - h1

        if rise == 0 or run == 0:
            return v1

        m = rise / run
        x = height - h1
        b = v1

        return m * x + b
