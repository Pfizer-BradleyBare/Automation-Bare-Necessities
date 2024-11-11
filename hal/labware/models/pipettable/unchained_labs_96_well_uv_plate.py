from __future__ import annotations

from ...layout import AlphanumericLayout, Layout
from ..labware_base import LabwareBase, PipettableLabwareMixin
from ..non_pipettable.agilent_lid_black import AgilentLidBlack


class UnchainedLabs96WellUVPlate(LabwareBase,PipettableLabwareMixin):
    @property
    def compatible_covers(self:UnchainedLabs96WellUVPlate) -> list[type[LabwareBase]]:
        return [AgilentLidBlack]

    @property
    def x_y_z_dimensions(self:UnchainedLabs96WellUVPlate) -> list[tuple[float, float, float]]:
        return [(124.5, 82, 0)]  # TODO: CHECK IS CORRECT

    @property
    def nesting_z_height_change(self:UnchainedLabs96WellUVPlate) -> float:
        return 0  # TODO: CHECK CORRECT

    @property
    def covered_z_height_change(self:UnchainedLabs96WellUVPlate) -> dict[type[LabwareBase], float]:
        return {}

    @property
    def stacked_z_height_change(self:UnchainedLabs96WellUVPlate) -> dict[type[LabwareBase], float]:
        return {}

    @property
    def short_side_z_grip_regions(self:UnchainedLabs96WellUVPlate) -> list[float]:
        return [4]

    @property
    def long_side_z_grip_regions(self:UnchainedLabs96WellUVPlate) -> list[float]:
        return [4]

    @property
    def layout(self:UnchainedLabs96WellUVPlate) -> Layout:
        return AlphanumericLayout(rows=8, columns=12, direction="Column-wise")

    @property
    def simultaneous_tips(self:UnchainedLabs96WellUVPlate) -> int:
        return 1

    @property
    def max_volume(self:UnchainedLabs96WellUVPlate) -> float:
        return 2

    @property
    def dead_volume(self:UnchainedLabs96WellUVPlate) -> float:
        return 0

    @property
    def well_definition(self:UnchainedLabs96WellUVPlate) -> list[tuple[float, float]]:
        return [(9.42e-05, 0.001), (0.0340182, 0.121), (0.0772432, 0.251), (1.9683132, 1.201), (5.0696632, 1.901)]
