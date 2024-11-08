from __future__ import annotations

from abc import abstractmethod
from itertools import pairwise

from django.db import models
from polymorphic.models import PolymorphicModel

from hal.labware.layout import Layout


class LabwareBase(PolymorphicModel):
    class Meta:
        ordering = ["identifier"]

    identifier = models.CharField(
        max_length=50,
        unique=True,
        editable=False,
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        return self.identifier

    def save(self, *args, **kwargs):
        self.identifier = type(self).__name__
        # The identifier of a labware is ALWAYS the class name. ALWAYS.

        return super().save(*args, **kwargs)

    @property
    @abstractmethod
    def compatible_covers(self) -> list[type[LabwareBase]]:
        """Labware can be covered by many different objects."""
        raise NotImplementedError

    @property
    @abstractmethod
    def x_y_z_dimensions(self) -> list[tuple[float, float, float]]:
        """Plates are not inheritantly a cube. This property defined how the rectangular shape of the plate changes across z heights."""
        raise NotImplementedError

    @property
    @abstractmethod
    def nesting_z_height_change(self) -> float:
        """How the z height changes by stacking two unlidded labware of the same type.
        Ex: <total height of nested labware> - (2 * <total height of labware>)
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def covered_z_height_change(self) -> dict[type[LabwareBase], float]:
        """How the z height changes with a cover of some kind.
        Ex: <total height of labware with cover> - <total height of labware>
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def stacked_z_height_change(self) -> dict[type[LabwareBase], float]:
        """How the z height changes when uncovered labware is place atop covered labware of the same type.
        Ex. <Total height of uncovered labware atop covered labware> - (2 * <total height of labware>)
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def short_side_z_grip_regions(self) -> list[float]:
        """Which regions are acceptable to be gripped on the short side when transported. Relative to bottom."""
        raise NotImplementedError

    @property
    @abstractmethod
    def long_side_z_grip_regions(self) -> list[float]:
        """Which regions are acceptable to be gripped on the long side when transported. Relative to bottom."""
        raise NotImplementedError

    @property
    @abstractmethod
    # TODO update the return type!!
    def layout(self) -> Layout:
        """Each labware has a addressing scheme associated with the underlying labware definition in the vendor software.
        This should match that addressing scheme.
        """
        raise NotImplementedError


class PipettableLabwareMixin:
    @property
    @abstractmethod
    def simultaneous_tips(self) -> int:
        """How many tips can fit in the well position at a the same time"""
        raise NotImplementedError

    @property
    @abstractmethod
    def max_volume(self) -> float:
        """Max volume of a well."""
        raise NotImplementedError

    @property
    @abstractmethod
    def dead_volume(self) -> float:
        """Minimum volume required in a well for successful aspiration."""
        raise NotImplementedError

    @property
    @abstractmethod
    def well_definition(self) -> list[tuple[float, float]]:
        """A list of (volume uL, height mm) pairs that define the shape of a well. Pipetting accurately in a well requires an accurate well shape definition."""
        raise NotImplementedError

    def interpolate_volume(self: PipettableLabwareMixin, volume: float) -> float:
        """Calculate height at a given volume."""
        if volume <= 0:
            return 0

        definition = self.well_definition
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

    def interpolate_height(self: PipettableLabwareMixin, height: float) -> float:
        """Calculate volume at a given height."""
        if height <= 0:
            return 0

        definition = self.well_definition
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
