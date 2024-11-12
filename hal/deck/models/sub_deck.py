from django.db import models

from .deck import Deck
from .deck_base import DeckBase


class SubDeck(DeckBase):
    parent_deck = models.ForeignKey(
        to=Deck,
        on_delete=models.CASCADE,
        help_text="Deck on which this sub deck is located.",
    )

    def __str__(self) -> str:
        return f"{self.parent_deck.identifier} | {self.identifier}"
