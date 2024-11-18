from __future__ import annotations

from django.db import models

from hal.transport.models import (
    TransportBase,
    TransportPickupOptionsBase,
    TransportPlaceOptionsBase,
)

from .carrier_location_base import CarrierLocationBase


class TransportableCarrierLocationConfig(models.Model):
    transport_device = models.ForeignKey(to=TransportBase, on_delete=models.CASCADE)
    pickup_options = models.ForeignKey(
        to=TransportPickupOptionsBase,
        on_delete=models.CASCADE,
    )
    place_options = models.ForeignKey(
        to=TransportPlaceOptionsBase,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ("transport_device", "pickup_options", "place_options")

    def __str__(self) -> str:
        return f"({self.pk}) {self.transport_device.identifier.replace(" ","")} | PickupOptions:{self.pickup_options} | PlaceOptions:{self.place_options}"

    def test_config_equality(
        self: TransportableCarrierLocationConfig,
        value: object,
    ) -> bool:
        if not isinstance(value, TransportableCarrierLocationConfig):
            return False

        return (
            self.transport_device == value.transport_device
            and self.pickup_options == value.pickup_options
        )

    # Only pickup options matter because the pickup options determine the orientation of the labware


class TransportableCarrierLocation(CarrierLocationBase):
    transport_configs: models.ManyToManyField[
        TransportableCarrierLocationConfig,
        TransportableCarrierLocation,
    ] = models.ManyToManyField(to=TransportableCarrierLocationConfig)

    @classmethod
    def get_compatible_transport_configs(
        cls,
        source: CarrierLocationBase,
        destination: CarrierLocationBase,
    ) -> list[
        tuple[TransportableCarrierLocationConfig, TransportableCarrierLocationConfig]
    ]:
        if not isinstance(source, TransportableCarrierLocation):
            return []

        if not isinstance(destination, TransportableCarrierLocation):
            return []

        return [
            (source_config, destination_config)
            for source_config in source.transport_configs
            for destination_config in destination.transport_configs
            if source_config == destination_config
        ]
        # __eq__ is defined for transport config so we just iterate through and collect the ones that are equal.
