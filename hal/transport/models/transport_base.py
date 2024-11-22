from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, ClassVar

from django.db import models
from django.utils.decorators import classproperty
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

    _max_grip_depth:ClassVar[float] = 0

    def __str__(self) -> str:
        return self.identifier

    class Meta:
        ordering = ["identifier"]

    @classproperty
    def max_grip_depth(cls) -> float:
        if cls._max_grip_depth == 0:
            raise NotImplementedError

        return cls._max_grip_depth

    def compute_short_side_grip_height(
        self,
        grip_item: LoadedLayoutItem,
    ) -> float:
        stack_z_dimension = grip_item.compute_stack_z_dimension(
            grip_item,
        )

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

        grip_heights = labware.short_side_z_grip_heights

        for grip_height in grip_heights:
            if grip_height > max_acceptable_grip_height:
                break

            if stack_z_dimension - grip_height < self.max_grip_depth:
                return grip_height
        # search bottom up because we want to grip as deeply as possible without exceeding our max depth.

        raise ValueError(
            "There are no compatible grip heights for your grip item",
        )

    def compute_long_side_grip_height(
        self,
        grip_item: LoadedLayoutItem,
    ) -> float:
        StackedLabwareZHeightChange.assert_supported_stack(grip_item)

        stack_z_dimension = StackedLabwareZHeightChange.compute_stack_z_dimension(
            grip_item,
        )

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

        grip_heights = labware.long_side_z_grip_heights

        for grip_height in grip_heights:
            if grip_height > max_acceptable_grip_height:
                break

            if stack_z_dimension - grip_height < self.max_grip_depth:
                return grip_height
        # search bottom up because we want to grip as deeply as possible without exceeding our max depth.

        raise ValueError(
            "There are no compatible grip heights for your grip item",
        )

    @staticmethod
    def assert_transport(source: LoadedLayoutItem, destination: LoadedLayoutItem):
        StackedLabwareZHeightChange.assert_supported_stack(source)

        if not destination.is_absolute_top_item:
            raise ValueError("Destination is not the top of the stack. Cannot insert a stack into another stack.")

        #need to do some assertions with the transport configs


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
        self, source: LoadedLayoutItem, destination: LoadedLayoutItem,
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
