from __future__ import annotations

from ...layout import AlphanumericLayout, Layout
from ..labware_base import LabwareBase, PipettableLabwareMixin
from ..non_pipettable.agilent_lid_black import AgilentLidBlack


class Biorad200uL96WellPlate(LabwareBase,PipettableLabwareMixin):
    @property
    def compatible_covers(self:Biorad200uL96WellPlate) -> list[type[LabwareBase]]:
        return [AgilentLidBlack]

    @property
    def x_y_z_dimensions(self:Biorad200uL96WellPlate) -> list[tuple[float, float, float]]:
        return [(124.5, 82.5, 0)]  # TODO: CHECK IS CORRECT

    @property
    def nesting_z_height_change(self:Biorad200uL96WellPlate) -> float:
        return 0  # TODO: CHECK CORRECT

    @property
    def covered_z_height_change(self:Biorad200uL96WellPlate) -> dict[type[LabwareBase], float]:
        return {}

    @property
    def stacked_z_height_change(self:Biorad200uL96WellPlate) -> dict[type[LabwareBase], float]:
        return {}

    @property
    def short_side_z_grip_regions(self:Biorad200uL96WellPlate) -> list[float]:
        return [6]

    @property
    def long_side_z_grip_regions(self:Biorad200uL96WellPlate) -> list[float]:
        return [6]

    @property
    def layout(self:Biorad200uL96WellPlate) -> Layout:
        return AlphanumericLayout(rows=8, columns=12, direction="Column-wise")

    @property
    def simultaneous_tips(self:Biorad200uL96WellPlate) -> int:
        return 1

    @property
    def max_volume(self:Biorad200uL96WellPlate) -> float:
        return 200

    @property
    def dead_volume(self:Biorad200uL96WellPlate) -> float:
        return 10

    @property
    def well_definition(self:Biorad200uL96WellPlate) -> list[tuple[float, float]]:
        return [(242.1231,14.68)]
