from django.db import models

from .deck import Deck
from .deck_base import DeckBase


class SubDeck(DeckBase):
    parent_deck = models.ForeignKey(to=Deck, on_delete=models.CASCADE)
