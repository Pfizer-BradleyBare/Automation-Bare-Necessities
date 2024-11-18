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
        unique_together = ("transport_device","pickup_options","place_options")

    def __str__(self) -> str:
        return f"({self.pk}) {self.transport_device.identifier.replace(" ","")} | PickupOptions:{self.pickup_options} | PlaceOptions:{self.place_options}"

class TransportableCarrierLocation(CarrierLocationBase):
    transport_configs = models.ManyToManyField(to=TransportableCarrierLocationConfig)
