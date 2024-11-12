from django.db import models
from polymorphic.models import PolymorphicModel

from hal.deck_location.models import DeckLocation
from hal.labware.models import Labware


class LayoutItem(PolymorphicModel):
    identifier = models.CharField(max_length=255, editable=False)
    # Only here to enable ordering

    deck_location = models.ForeignKey(
        to=DeckLocation,
        on_delete=models.CASCADE,
    )
    labware = models.ForeignKey(
        to=Labware,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["identifier"]
        unique_together = ("deck_location", "labware")

    def save(self, *args, **kwargs):
        self.identifier = f"{self.deck_location.identifier}_{self.labware.identifier}"

        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.identifier
