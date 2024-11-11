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
        return [(20, 1.2), (40, 2.7), (60, 3.8), (80, 4.5), (100, 5.9), (120, 6.8), (140, 7.4), (160, 8.2), (180, 8.9), (200, 9.5), (220, 10.0), (240, 10.6), (260, 11.0), (280, 11.4), (300, 12.2), (320, 12.6), (340, 13.1), (360, 13.6), (380, 14.1), (400, 14.5), (420, 14.8), (440, 15.3), (460, 15.6), (480, 15.8), (500, 16.4), (520, 16.7), (540, 16.9), (560, 17.3), (580, 17.7), (600, 18.1), (620, 18.2), (640, 18.5), (660, 19.0), (680, 19.2), (700, 19.6), (720, 20.0), (740, 20.2), (760, 20.7), (780, 20.9), (800, 21.3), (820, 21.5), (840, 21.8), (860, 22.2), (880, 22.4), (900, 22.9), (920, 23.2), (940, 23.5), (960, 24.0), (980, 24.3), (1000, 24.7), (1020, 24.9), (1040, 25.3), (1060, 25.5), (1080, 25.8), (1100, 26.3), (1120, 26.6), (1140, 26.9), (1160, 27.2), (1180, 27.4), (1200, 27.9), (1220, 28.1), (1240, 28.3), (1260, 28.7), (1280, 28.9), (1300, 29.4), (1320, 29.6), (1340, 29.9), (1360, 30.2), (1380, 30.5), (1400, 30.9), (1420, 31.2), (1440, 31.4), (1460, 31.7), (1480, 31.9), (1500, 32.5), (1520, 32.8), (1540, 32.9), (1560, 33.3), (1580, 33.5), (1600, 33.9), (1620, 34.1), (1640, 34.5), (1660, 34.7), (1680, 34.9), (1700, 35.4), (1720, 35.7), (1740, 35.8), (1760, 36.3), (1780, 36.5), (1800, 36.9)]
