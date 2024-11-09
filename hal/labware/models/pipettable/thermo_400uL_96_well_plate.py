from __future__ import annotations

from ...layout import AlphanumericLayout, Layout
from ..labware_base import LabwareBase, PipettableLabwareMixin
from ..non_pipettable.agilent_lid_black import AgilentLidBlack


class Thermo400uL96WellPlate(LabwareBase,PipettableLabwareMixin):
    @property
    def compatible_covers(self:Thermo400uL96WellPlate) -> list[type[LabwareBase]]:
        return [AgilentLidBlack]

    @property
    def x_y_z_dimensions(self:Thermo400uL96WellPlate) -> list[tuple[float, float, float]]:
        return [(123.25, 84.75, 0)]  # TODO: CHECK IS CORRECT

    @property
    def nesting_z_height_change(self:Thermo400uL96WellPlate) -> float:
        return 0  # TODO: CHECK CORRECT

    @property
    def covered_z_height_change(self:Thermo400uL96WellPlate) -> dict[type[LabwareBase], float]:
        return {}

    @property
    def stacked_z_height_change(self:Thermo400uL96WellPlate) -> dict[type[LabwareBase], float]:
        return {}

    @property
    def short_side_z_grip_regions(self:Thermo400uL96WellPlate) -> list[float]:
        return [5]

    @property
    def long_side_z_grip_regions(self:Thermo400uL96WellPlate) -> list[float]:
        return [5]

    @property
    def layout(self:Thermo400uL96WellPlate) -> Layout:
        return AlphanumericLayout(rows=8, columns=12, direction="Column-wise")

    @property
    def simultaneous_tips(self:Thermo400uL96WellPlate) -> int:
        return 1

    @property
    def max_volume(self:Thermo400uL96WellPlate) -> float:
        return 400

    @property
    def dead_volume(self:Thermo400uL96WellPlate) -> float:
        return 10

    @property
    def well_definition(self:Thermo400uL96WellPlate) -> list[tuple[float, float]]:
        return [(56.745,3),(510.705,11)]
