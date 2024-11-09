from __future__ import annotations

from ...layout import AlphanumericLayout, Layout
from ..labware_base import LabwareBase, PipettableLabwareMixin
from ..non_pipettable.agilent_lid_black import AgilentLidBlack


class CorningCostar2000uL96WellPlate(LabwareBase,PipettableLabwareMixin):
    @property
    def compatible_covers(self:CorningCostar2000uL96WellPlate) -> list[type[LabwareBase]]:
        return [AgilentLidBlack]

    @property
    def x_y_z_dimensions(self:CorningCostar2000uL96WellPlate) -> list[tuple[float, float, float]]:
        return [(124.5, 82.5, 0)]  # TODO: CHECK IS CORRECT

    @property
    def nesting_z_height_change(self:CorningCostar2000uL96WellPlate) -> float:
        return 0  # TODO: CHECK CORRECT

    @property
    def covered_z_height_change(self:CorningCostar2000uL96WellPlate) -> dict[type[LabwareBase], float]:
        return {}

    @property
    def stacked_z_height_change(self:CorningCostar2000uL96WellPlate) -> dict[type[LabwareBase], float]:
        return {}

    @property
    def short_side_z_grip_regions(self:CorningCostar2000uL96WellPlate) -> list[float]:
        return [10]

    @property
    def long_side_z_grip_regions(self:CorningCostar2000uL96WellPlate) -> list[float]:
        return [10]

    @property
    def layout(self:CorningCostar2000uL96WellPlate) -> Layout:
        return AlphanumericLayout(rows=8, columns=12, direction="Column-wise")

    @property
    def simultaneous_tips(self:CorningCostar2000uL96WellPlate) -> int:
        return 1

    @property
    def max_volume(self:CorningCostar2000uL96WellPlate) -> float:
        return 2000

    @property
    def dead_volume(self:CorningCostar2000uL96WellPlate) -> float:
        return 10

    @property
    def well_definition(self:CorningCostar2000uL96WellPlate) -> list[tuple[float, float]]:
        return [(134.0416,4),(2566.0416,42)]
