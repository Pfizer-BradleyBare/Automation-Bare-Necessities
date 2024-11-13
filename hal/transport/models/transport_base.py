from django.db import models
from polymorphic.models import PolymorphicModel

from hal.backend.models import BackendBase
from hal.labware.models import LabwareBase


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

    supported_labware = models.ManyToManyField(to=LabwareBase)

    class Meta:
        ordering = ["identifier"]

    def save(self, *args, **kwargs):
        self.identifier = (
            f"{self.backend.identifier.replace(" ","")}_{type(self).__name__}"
        )

        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.identifier


class TransportPickupOptionsBase(PolymorphicModel):
    transport_device = TransportBase.__name__


class TransportPlaceOptionsBase(PolymorphicModel):
    transport_device = TransportBase.__name__
