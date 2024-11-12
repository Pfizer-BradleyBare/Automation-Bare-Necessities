from __future__ import annotations

from itertools import pairwise
from typing import cast

from django.core.exceptions import ValidationError
from django.db import models


class Container(models.Model):
    identifier = models.CharField(max_length=255, unique=True, primary_key=True)

    simultaneous_tips = models.SmallIntegerField(
        help_text="How many tips can fit in the container position at a the same time.",
    )

    max_volume = models.SmallIntegerField(help_text="Max volume of a container.")

    dead_volume = models.SmallIntegerField(
        help_text="Minimum volume required in a container for successful aspiration.",
    )

    shape_definition: models.JSONField[list[tuple[float, float]]] = models.JSONField(
        help_text="A list of (volume uL, height mm) pairs, volume ordered, that define the shape of a container. Pipetting accurately in a container requires an accurate container shape definition.",
    )

    class Meta:
        ordering = ["identifier"]

    def __str__(self) -> str:
        return self.identifier

    def clean(self) -> None:
        definition = cast(list[tuple[float, float]], self.shape_definition)

        if len(definition) != {volume for volume, _ in definition}:
            raise ValidationError(
                "'shape_definition' is incorrect. Duplicate volume values are present.",
            )

        if len(definition) != {height for _, height in definition}:
            raise ValidationError(
                "'shape_definition' is incorrect. Duplicate height values are present.",
            )

        try:
            for index, (volume, height) in enumerate(definition):
                if len(definition[index]) != 2:
                    raise ValueError  # noqa:TRY301

                definition[index] = (float(volume), float(height))

        except ValueError as e:
            raise ValidationError(
                "'shape_definition' is incorrect. Expected list of tuples. Ex: [(0,0),(100,10),(500,15)]",
            ) from e

        definition = sorted(definition, key=lambda x: x[0])

        initial_volume, initial_height = definition[0]

        if initial_volume != 0 and initial_height != 0:
            definition.insert(0, (0, 0))

        for (_, h1), (_, h2) in pairwise(definition):
            if h1 > h2:
                raise ValidationError(
                    "'shape_definition' is incorrect. When volume sorted, height is not in ascending order.",
                )

        self.shape_definition = definition

        return super().clean()

    def interpolate_volume(self, volume: float) -> float:
        """Calculate height at a given volume."""
        if volume <= 0:
            return 0

        definition = cast(list[tuple[float, float]], self.shape_definition)
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

    def interpolate_height(self, height: float) -> float:
        """Calculate volume at a given height."""
        if height <= 0:
            return 0

        definition = cast(list[tuple[float, float]], self.shape_definition)
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
