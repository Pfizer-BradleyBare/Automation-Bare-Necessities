from django.db import models
from polymorphic.models import PolymorphicModel

from hal.deck.models import Deck, SubDeck


class CarrierBase(PolymorphicModel):
    identifier = models.CharField(max_length=255, editable=False)
    # Only here to enable ordering

    deck = models.ForeignKey(
        to=Deck,
        on_delete=models.CASCADE,
        help_text="Which deck is this carrier assigned to?",
    )

    deck_position = models.SmallIntegerField(
        help_text="Typically the starting carrier number. But for decks without a positions this is flexible (NOTE: from left to right).",
    )

    def save(self, *args, **kwargs):
        deck = self.deck

        if isinstance(deck, SubDeck):
            self.identifier = f"{deck.identifier}Sub_{deck.parent_deck.identifier}_Deck_Carrier{self.deck_position}"
        else:
            self.identifier = f"{deck.identifier}Deck_Carrier{self.deck_position}"
        # Identifier is automatically determined

        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["identifier"]
        unique_together = ("deck", "deck_position")

    def __str__(self) -> str:
        return self.identifier
