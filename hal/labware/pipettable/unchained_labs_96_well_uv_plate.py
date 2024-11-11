from __future__ import annotations

from hal.container import ContainerBase, UnchainedLabsUVReaderWell

from ..labware_base import LabwareBase, PipettableLabware
from ..layout import AlphanumericLayout, Layout
from ..non_pipettable.agilent_lid_black import AgilentLidBlack


class UnchainedLabs96WellUVPlate(PipettableLabware):
    @classmethod
    def x_y_z_dimensions(cls) -> list[tuple[float, float, float]]:
        return [(124.5, 82, 0)]  # TODO: CHECK IS CORRECT

    @classmethod
    def compatible_covers(cls) -> list[type[LabwareBase]]:
        return [AgilentLidBlack]

    @classmethod
    def covered_z_height_change(cls) -> dict[type[LabwareBase], float]:
        return {}

    @classmethod
    def short_side_z_grip_regions(cls) -> list[float]:
        return [4]

    @classmethod
    def long_side_z_grip_regions(cls) -> list[float]:
        return [4]

    @classmethod
    def layout(cls) -> Layout:
        return AlphanumericLayout(rows=8, columns=12, direction="Column-wise")

    @classmethod
    def container(self) -> type[ContainerBase]:
        return UnchainedLabsUVReaderWell
