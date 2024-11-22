from __future__ import annotations

from abc import abstractmethod

from django.db import models
from polymorphic.models import PolymorphicModel

from hal.carrier_location.models import CarrierLocationBase
from hal.labware.models import LabwareBase


class LayoutItemBase(PolymorphicModel):
    identifier = models.CharField(max_length=255, editable=False)
    # Only here to enable ordering

    carrier_location = models.ForeignKey(
        to=CarrierLocationBase,
        on_delete=models.CASCADE,
        help_text="Which deck location is this layout item located?",
    )
    labware = models.ForeignKey(
        to=LabwareBase,
        on_delete=models.CASCADE,
        help_text="What is the labware of this layout item?",
    )

    def __str__(self) -> str:
        return f"{self.identifier} ({self.pk})"

    class Meta:
        ordering = ["identifier"]
        unique_together = ("carrier_location", "labware")

    @abstractmethod
    def initialize(self):
        raise NotImplementedError

    @abstractmethod
    def deinitialize(self):
        raise NotImplementedError

    def save(self, *args, **kwargs):
        self.identifier = f"{self.carrier_location.identifier.replace(" ","")}_{self.labware.identifier.replace(" ","")}"

        return super().save(*args, **kwargs)
