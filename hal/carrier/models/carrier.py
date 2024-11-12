from django.db import models
from polymorphic.models import PolymorphicModel

from hal.deck.models import Deck


class Carrier(PolymorphicModel):
    identifier = models.CharField(max_length=255, unique=True, editable=False)

    deck = models.ForeignKey(
        to=Deck,
        on_delete=models.CASCADE,
        help_text="Which deck is this carrier assigned to?",
    )

    deck_position = models.SmallIntegerField(
        help_text="Typically the starting carrier number. But for decks without a positions this is flexible (NOTE: from left to right).",
    )

    def save(self, *args, **kwargs):
        self.identifier = f"{self.deck}_Carrier{self.deck_position}"
        # Identifier is automatically determined

        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["identifier"]

    def __str__(self) -> str:
        return self.identifier
