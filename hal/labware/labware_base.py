from __future__ import annotations

from abc import abstractmethod

from polymorphic.models import PolymorphicModel

from hal.container import ContainerBase
from hal.labware.layout import Layout


class LabwareBase(PolymorphicModel):
    def __init__(self, *args, **kwargs):
        raise TypeError("LabwareBase classes are not meant to be instantiated.")

    @classmethod
    @abstractmethod
    def x_y_z_dimensions(cls) -> list[tuple[float, float, float]]:
        """Plates are not inheritantly a cube. This property defined how the rectangular shape of the plate changes across z heights."""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def covered_z_height_change(cls) -> dict[type[LabwareBase], float]:
        """How the z height changes with a cover of some kind (any lid or plate labware).
        Ex: <total height of labware with cover> - <total height of labware>
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def short_side_z_grip_regions(cls) -> list[float]:
        """Which regions are acceptable to be gripped on the short side when transported. Relative to bottom."""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def long_side_z_grip_regions(cls) -> list[float]:
        """Which regions are acceptable to be gripped on the long side when transported. Relative to bottom."""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    # TODO update the return type!!
    def layout(cls) -> Layout:
        """Each labware has a addressing scheme associated with the underlying labware definition in the vendor software.
        This should match that addressing scheme.
        """
        raise NotImplementedError


class NonPipettableLabware(LabwareBase): ...


class PipettableLabware(LabwareBase):
    @classmethod
    @abstractmethod
    def container(cls) -> type[ContainerBase]:
        """Pipettable labware has an associated container where liquids are present. The labware itself is just a 'rack' that houses containers."""
        raise NotImplementedError
