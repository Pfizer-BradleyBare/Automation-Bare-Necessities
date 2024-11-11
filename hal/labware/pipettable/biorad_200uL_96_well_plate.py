from __future__ import annotations

from hal.container import Biorad200uLWell, ContainerBase

from ..labware_base import LabwareBase, PipettableLabware
from ..layout import AlphanumericLayout, Layout


class Biorad200uL96WellPlate(PipettableLabware):
    @classmethod
    def x_y_z_dimensions(
        cls,
    ) -> list[tuple[float, float, float]]:
        return [(124.5, 82.5, 0)]  # TODO: CHECK IS CORRECT

    @classmethod
    def covered_z_height_change(cls) -> dict[type[LabwareBase], float]:
        return {}

    @classmethod
    def short_side_z_grip_regions(cls) -> list[float]:
        return [6]

    @classmethod
    def long_side_z_grip_regions(cls) -> list[float]:
        return [6]

    @classmethod
    def layout(cls) -> Layout:
        return AlphanumericLayout(rows=8, columns=12, direction="Column-wise")

    @classmethod
    def container(cls) -> type[ContainerBase]:
        return Biorad200uLWell
