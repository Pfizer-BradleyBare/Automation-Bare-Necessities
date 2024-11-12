from django.db import models

from .deck import Deck
from .deck_base import DeckBase


class SubDeck(DeckBase):
    parent_deck = models.ForeignKey(to=Deck, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.parent_deck.identifier} | {self.identifier}"
