from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, ClassVar

from django.db import models
from django.utils.functional import classproperty
from polymorphic.models import PolymorphicModel

from hal.backend.models import BackendBase
from hal.labware.models import StackedLabwareZHeightChange
from hal.layout_item.models import LoadedLayoutItem

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

    last_transport_flag = models.BooleanField(editable=False, default=False)

    _max_grip_depth: ClassVar[float] = 0

    def __str__(self) -> str:
        return f"{self.identifier} ({self.pk})"

    class Meta:
        ordering = ["identifier"]

    @classproperty
    def max_grip_depth(cls) -> float:
        if cls._max_grip_depth == 0:
            raise NotImplementedError

        return cls._max_grip_depth

    def compute_grip_height(
        self,
        grip_item: LoadedLayoutItem,
    ) -> tuple[float | None, float | None]:
        stack_height = grip_item.height

        labware = grip_item.layout_item.labware

        if not grip_item.is_absolute_top_item:
            top = grip_item.top

            z_height_change = (
                StackedLabwareZHeightChange.objects.filter(
                    bottom_labware=grip_item,
                    top_labware=top,
                )
                .get()
                .z_height_change
            )
            max_acceptable_grip_height = labware.height + z_height_change
        else:
            max_acceptable_grip_height = labware.height

        long_side_grip_heights = labware.long_side_grip_heights
        long_side_grip_height = None

        for grip_height in long_side_grip_heights:
            if grip_height > max_acceptable_grip_height:
                break

            if stack_height - grip_height < self.max_grip_depth:
                long_side_grip_height = grip_height
                break
        # search bottom up because we want to grip as deeply as possible without exceeding our max depth.

        short_side_grip_heights = labware.short_side_grip_heights
        short_side_grip_height = None

        for grip_height in short_side_grip_heights:
            if grip_height > max_acceptable_grip_height:
                break

            if stack_height - grip_height < self.max_grip_depth:
                short_side_grip_height = grip_height
                break
        # search bottom up because we want to grip as deeply as possible without exceeding our max depth.

        return (short_side_grip_height, long_side_grip_height)

    @abstractmethod
    def assert_transport(self, source: LoadedLayoutItem, destination: LoadedLayoutItem):
        from hal.carrier_location.models import TransportableCarrierLocationConfig

        source.assert_supported_stack()

        if not destination.is_absolute_top_item:
            raise ValueError(
                "Destination is not the top of the stack. Cannot insert a stack into another stack.",
            )

        if not StackedLabwareZHeightChange.objects.filter(
            bottom_labware=destination.layout_item.labware,
            top_labware=source.layout_item.labware,
        ).exists():
            raise ValueError("Source and destination are not compatible stack pairs.")

        if not TransportableCarrierLocationConfig.objects.filter(
            transportablecarrierlocation=source,
            transport_device=self,
        ).exists():
            raise ValueError(
                f"Source can not be transported by the transport device '{self}'",
            )

        if not TransportableCarrierLocationConfig.objects.filter(
            transportablecarrierlocation=destination,
            transport_device=self,
        ).exists():
            raise ValueError(
                f"Destination can not be transported by the transport device '{self}'",
            )

    @staticmethod
    def get_compatible_transport_configs(
        source: LoadedLayoutItem,
        destination: LoadedLayoutItem,
    ) -> list[
        tuple[TransportableCarrierLocationConfig, TransportableCarrierLocationConfig]
    ]:
        """Return a list of transport configs. The list will be sorted ascending by transport_time."""
        from hal.carrier_location.models import TransportableCarrierLocation

        compatible_configs = (
            TransportableCarrierLocation.get_compatible_transport_configs(
                source.layout_item.carrier_location,
                destination.layout_item.carrier_location,
            )
        )

        transport_devices = [
            source_config.transport_device for source_config, _ in compatible_configs
        ]
        # Source and dest transport devices will always be the same so we can only pull one for our needs

        transport_times = [
            device.transport_time(source, destination) for device in transport_devices
        ]

        time_sorted_configs = sorted(
            zip(transport_times, compatible_configs, strict=False),
            key=lambda x: x[0],
        )

        return [config for _, config in time_sorted_configs]

    @abstractmethod
    def initialize(self):
        raise NotImplementedError

    @abstractmethod
    def deinitialize(self):
        raise NotImplementedError

    @abstractmethod
    def transport(self, source: LoadedLayoutItem, destination: LoadedLayoutItem):
        raise NotImplementedError

    @abstractmethod
    def transport_time(
        self,
        source: LoadedLayoutItem,
        destination: LoadedLayoutItem,
    ) -> float:
        raise NotImplementedError

    def save(self, *args, **kwargs):
        self.identifier = (
            f"{self.backend.identifier.replace(" ","")}_{type(self).__name__}"
        )

        return super().save(*args, **kwargs)


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
