from __future__ import annotations

from hal.container import ContainerBase, Thermo400uLWell

from ..labware_base import LabwareBase, PipettableLabware
from ..layout import AlphanumericLayout, Layout
from ..non_pipettable.agilent_lid_black import AgilentLidBlack


class Thermo400uL96WellPlate(PipettableLabware):
    @classmethod
    def x_y_z_dimensions(cls) -> list[tuple[float, float, float]]:
        return [(123.25, 84.75, 0)]  # TODO: CHECK IS CORRECT

    @classmethod
    def compatible_covers(cls) -> list[type[LabwareBase]]:
        return [AgilentLidBlack]

    @classmethod
    def covered_z_height_change(cls) -> dict[type[LabwareBase], float]:
        return {}

    @classmethod
    def short_side_z_grip_regions(cls) -> list[float]:
        return [5]

    @classmethod
    def long_side_z_grip_regions(cls) -> list[float]:
        return [5]

    @classmethod
    def layout(cls) -> Layout:
        return AlphanumericLayout(rows=8, columns=12, direction="Column-wise")

    @classmethod
    def container(cls) -> type[ContainerBase]:
        return Thermo400uLWell
