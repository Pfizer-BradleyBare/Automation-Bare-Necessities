from django.db import models
from polymorphic.models import PolymorphicModel

from hal.deck_location.models import DeckLocationBase
from hal.labware.models import LabwareBase


class LayoutItemBase(PolymorphicModel):
    identifier = models.CharField(max_length=255, editable=False)
    # Only here to enable ordering

    deck_location = models.ForeignKey(
        to=DeckLocationBase,
        on_delete=models.CASCADE,
        help_text="Which deck location is this layout item located?",
    )
    labware = models.ForeignKey(
        to=LabwareBase,
        on_delete=models.CASCADE,
        help_text="What is the labware of this layout item?",
    )

    class Meta:
        ordering = ["identifier"]
        unique_together = ("deck_location", "labware")

    def save(self, *args, **kwargs):
        self.identifier = f"{self.deck_location.identifier.replace(" ","")}_{self.labware.identifier.replace(" ","")}"

        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.identifier
