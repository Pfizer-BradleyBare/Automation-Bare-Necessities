from django.db import models
from polymorphic.models import PolymorphicModel


class DeckBase(PolymorphicModel):
    identifier = models.CharField(
        max_length=255,
        unique=True,
        help_text="Unique name to distinguish this deck from other decks.",
    )

    class Meta:
        ordering = ["identifier"]

    def __str__(self) -> str:
        return self.identifier
