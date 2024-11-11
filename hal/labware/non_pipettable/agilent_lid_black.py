from __future__ import annotations

from ..labware_base import LabwareBase, NonPipettableLabware
from ..layout import Layout, NumericLayout


class AgilentLidBlack(NonPipettableLabware):
    @classmethod
    def x_y_z_dimensions(cls) -> list[tuple[float, float, float]]:
        return [(127.5, 85, 9.5)]  # TODO: CHECK IS CORRECT

    @classmethod
    def compatible_covers(cls) -> list[type[LabwareBase]]:
        return []

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
        return NumericLayout(rows=1, columns=1, direction="Column-wise")
