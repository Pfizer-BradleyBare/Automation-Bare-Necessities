from __future__ import annotations

from hal.container import CentrifugeTube15mL, ContainerBase

from ..labware_base import LabwareBase, PipettableLabware
from ..layout import AlphanumericLayout, Layout


class CentrifugeTube15mLHamiltonCarrier(PipettableLabware):
    @classmethod
    def x_y_z_dimensions(
        cls,
    ) -> list[tuple[float, float, float]]:
        return [(0, 0, 0)]  # TODO: CHECK IS CORRECT

    @classmethod
    def compatible_covers(cls) -> list[type[LabwareBase]]:
        return []

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
        return CentrifugeTube15mL
