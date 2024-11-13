from django.db import models

from hal.transport.models import (
    TransportBase,
    TransportPickupOptionsBase,
    TransportPlaceOptionsBase,
)

from .deck_location_base import DeckLocationBase


class TransportableDeckLocationConfig(models.Model):
    transport_device = models.ForeignKey(to=TransportBase, on_delete=models.CASCADE)
    pickup_options = models.ForeignKey(
        to=TransportPickupOptionsBase,
        on_delete=models.CASCADE,
    )
    place_options = models.ForeignKey(
        to=TransportPlaceOptionsBase,
        on_delete=models.CASCADE,
    )


class TransportableDeckLocation(DeckLocationBase):
    transport_configs = models.ManyToManyField(to=TransportableDeckLocationConfig)
