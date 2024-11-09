from __future__ import annotations

from ...layout import AlphanumericLayout, Layout
from ..labware_base import LabwareBase, PipettableLabwareMixin


class Hamilton1500uL24WellFliptubeRack(LabwareBase,PipettableLabwareMixin):
    @property
    def compatible_covers(self:Hamilton1500uL24WellFliptubeRack) -> list[type[LabwareBase]]:
        return []

    @property
    def x_y_z_dimensions(self:Hamilton1500uL24WellFliptubeRack) -> list[tuple[float, float, float]]:
        return [(128, 85.25, 0)]  # TODO: CHECK IS CORRECT

    @property
    def nesting_z_height_change(self:Hamilton1500uL24WellFliptubeRack) -> float:
        return 0  # TODO: CHECK CORRECT

    @property
    def covered_z_height_change(self:Hamilton1500uL24WellFliptubeRack) -> dict[type[LabwareBase], float]:
        return {}

    @property
    def stacked_z_height_change(self:Hamilton1500uL24WellFliptubeRack) -> dict[type[LabwareBase], float]:
        return {}

    @property
    def short_side_z_grip_regions(self:Hamilton1500uL24WellFliptubeRack) -> list[float]:
        return [5]

    @property
    def long_side_z_grip_regions(self:Hamilton1500uL24WellFliptubeRack) -> list[float]:
        return [5]

    @property
    def layout(self:Hamilton1500uL24WellFliptubeRack) -> Layout:
        return AlphanumericLayout(rows=8, columns=12, direction="Column-wise")

    @property
    def simultaneous_tips(self:Hamilton1500uL24WellFliptubeRack) -> int:
        return 1

    @property
    def max_volume(self:Hamilton1500uL24WellFliptubeRack) -> float:
        return 1500

    @property
    def dead_volume(self:Hamilton1500uL24WellFliptubeRack) -> float:
        return 10

    @property
    def well_definition(self:Hamilton1500uL24WellFliptubeRack) -> list[tuple[float, float]]:
        return [] #TODO: Add Correct defintiion curve
