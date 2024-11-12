from django.db import models
from polymorphic.models import PolymorphicModel

from hal.carrier.models import Carrier


class DeckLocation(PolymorphicModel):
    identifier = models.CharField(max_length=255, editable=False)
    carrier = models.ForeignKey(
        to=Carrier,
        on_delete=models.CASCADE,
    )
    carrier_position = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["identifier"]
        unique_together = ("carrier", "carrier_position")

    def save(self, *args, **kwargs):
        self.identifier = f"{self.carrier.identifier}_Pos{self.carrier_position}"

        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.identifier
