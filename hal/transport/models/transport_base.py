from __future__ import annotations

from abc import abstractmethod

from django.db import models
from polymorphic.models import PolymorphicModel

from hal.backend.models import BackendBase
from hal.layout_item.models import LayoutItemBase


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

    class Meta:
        ordering = ["identifier"]

    @abstractmethod
    def initialize(self):
        raise NotImplementedError

    @abstractmethod
    def deinitialize(self):
        raise NotImplementedError

    @abstractmethod
    def transport(self, source: LayoutItemBase, destination: LayoutItemBase):
        raise NotImplementedError

    @abstractmethod
    def transport_time(self, source: LayoutItemBase, destination: LayoutItemBase):
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
