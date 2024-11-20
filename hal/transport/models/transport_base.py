from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING

from django.db import models
from polymorphic.models import PolymorphicModel

from hal.backend.models import BackendBase
from hal.layout_item.models import LayoutItemBase, LoadedLayoutItem

if TYPE_CHECKING:
    from hal.carrier_location.models import (
        TransportableCarrierLocationConfig,
    )


class TransportBase(PolymorphicModel):
    identifier = models.CharField(
        max_length=255,
        editable=False,
    )

    enabled = models.BooleanField(default=True)

    backend = models.ForeignKey(
        to=BackendBase,
        on_delete=models.CASCADE,
    )

    last_transport_flag: bool = False

    @property
    @abstractmethod
    def max_grip_depth(self) -> float:
        raise NotImplementedError

    class Meta:
        ordering = ["identifier"]

    def _get_compatible_configs(
        self,
        source: LoadedLayoutItem,
        destination: LayoutItemBase,
    ) -> list[
        tuple[TransportableCarrierLocationConfig, TransportableCarrierLocationConfig]
    ]:
        from hal.carrier_location.models import TransportableCarrierLocation

        """Return a list of transport configs. The list will be sorted ascending by transport_time. The entries are guarenteed to be compatible with the source (including stacked items if applicable)."""

        compatible_configs = (
            TransportableCarrierLocation.get_compatible_transport_configs(
                source.layout_item.carrier_location,
                destination.carrier_location,
            )
        )

    @abstractmethod
    def initialize(self):
        raise NotImplementedError

    @abstractmethod
    def deinitialize(self):
        raise NotImplementedError

    @abstractmethod
    def transport(self, source: LoadedLayoutItem, destination: LayoutItemBase):
        raise NotImplementedError

    @abstractmethod
    def transport_time(self, source: LoadedLayoutItem, destination: LayoutItemBase):
        raise NotImplementedError

    def save(self, *args, **kwargs):
        self.identifier = (
            f"{self.backend.identifier.replace(" ","")}_{type(self).__name__}"
        )

        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.identifier


class TransportPickupOptionsBase(PolymorphicModel):
    transport_device = TransportBase.__name__

    @abstractmethod
    def test_options_equality(
        self: TransportPickupOptionsBase,
        value: object,
    ) -> bool:
        raise NotImplementedError


class TransportPlaceOptionsBase(PolymorphicModel):
    transport_device = TransportBase.__name__

    @abstractmethod
    def test_options_equality(
        self: TransportPlaceOptionsBase,
        value: object,
    ) -> bool:
        raise NotImplementedError
