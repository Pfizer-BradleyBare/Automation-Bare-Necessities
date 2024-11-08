from ...layout import Layout, NumericLayout
from ..labware_base import LabwareBase


class AgilentLidBlack(LabwareBase):
    @property
    def compatible_covers(self) -> list[type[LabwareBase]]:
        return []

    @property
    def x_y_z_dimensions(self) -> list[tuple[float, float, float]]:
        return [(127.5, 85, 9.5)]  # TODO: CHECK IS CORRECT

    @property
    def nesting_z_height_change(self) -> float:
        return 1  # TODO: CHECK CORRECT

    @property
    def covered_z_height_change(self) -> dict[type[LabwareBase], float]:
        return {}

    @property
    def stacked_z_height_change(self) -> dict[type[LabwareBase], float]:
        return {}

    @property
    def short_side_z_grip_regions(self) -> list[float]:
        return [4]

    @property
    def long_side_z_grip_regions(self) -> list[float]:
        return [4]

    @property
    def layout(self) -> Layout:
        return NumericLayout(rows=1, columns=1, direction="Column-wise")
