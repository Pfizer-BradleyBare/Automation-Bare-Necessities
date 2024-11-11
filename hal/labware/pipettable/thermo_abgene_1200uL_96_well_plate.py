from __future__ import annotations

from hal.container import ContainerBase, ThermoAbgene1200uLWell

from ..labware_base import LabwareBase, PipettableLabware
from ..layout import AlphanumericLayout, Layout


class ThermoAbgene1200uL96WellPlate(PipettableLabware):
    @classmethod
    def x_y_z_dimensions(cls) -> list[tuple[float, float, float]]:
        return [(124.75, 82, 0)]  # TODO: CHECK IS CORRECT

    @classmethod
    def covered_z_height_change(cls) -> dict[type[LabwareBase], float]:
        return {}

    @classmethod
    def short_side_z_grip_regions(cls) -> list[float]:
        return [10]

    @classmethod
    def long_side_z_grip_regions(cls) -> list[float]:
        return [10]

    @classmethod
    def layout(cls) -> Layout:
        return AlphanumericLayout(rows=8, columns=12, direction="Column-wise")

    @classmethod
    def container(cls) -> type[ContainerBase]:
        return ThermoAbgene1200uLWell
