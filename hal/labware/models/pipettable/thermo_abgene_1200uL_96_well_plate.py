from __future__ import annotations

from ...layout import AlphanumericLayout, Layout
from ..labware_base import LabwareBase, PipettableLabwareMixin
from ..non_pipettable.agilent_lid_black import AgilentLidBlack


class ThermoAbgene1200uL96WellPlate(LabwareBase,PipettableLabwareMixin):
    @property
    def compatible_covers(self:ThermoAbgene1200uL96WellPlate) -> list[type[LabwareBase]]:
        return [AgilentLidBlack]

    @property
    def x_y_z_dimensions(self:ThermoAbgene1200uL96WellPlate) -> list[tuple[float, float, float]]:
        return [(124.75, 82, 0)]  # TODO: CHECK IS CORRECT

    @property
    def nesting_z_height_change(self:ThermoAbgene1200uL96WellPlate) -> float:
        return 0  # TODO: CHECK CORRECT

    @property
    def covered_z_height_change(self:ThermoAbgene1200uL96WellPlate) -> dict[type[LabwareBase], float]:
        return {}

    @property
    def stacked_z_height_change(self:ThermoAbgene1200uL96WellPlate) -> dict[type[LabwareBase], float]:
        return {}

    @property
    def short_side_z_grip_regions(self:ThermoAbgene1200uL96WellPlate) -> list[float]:
        return [10]

    @property
    def long_side_z_grip_regions(self:ThermoAbgene1200uL96WellPlate) -> list[float]:
        return [10]

    @property
    def layout(self:ThermoAbgene1200uL96WellPlate) -> Layout:
        return AlphanumericLayout(rows=8, columns=12, direction="Column-wise")

    @property
    def simultaneous_tips(self:ThermoAbgene1200uL96WellPlate) -> int:
        return 1

    @property
    def max_volume(self:ThermoAbgene1200uL96WellPlate) -> float:
        return 1200

    @property
    def dead_volume(self:ThermoAbgene1200uL96WellPlate) -> float:
        return 10

    @property
    def well_definition(self:ThermoAbgene1200uL96WellPlate) -> list[tuple[float, float]]:
        return [(83.1264,3),(1353.2064,21)]
