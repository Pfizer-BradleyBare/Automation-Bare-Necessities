from __future__ import annotations

from django.db import models

from hal.deck_location.models import DeckLocationBase
from hal.labware.models import LabwareBase


class LayoutItemStack(models.Model):
    deck_location = models.ForeignKey(
        to=DeckLocationBase,
        on_delete=models.CASCADE,
        help_text="Which deck location is this layout item located?",
    )
    layout_item = models.ForeignKey(
        to=LabwareBase,
        on_delete=models.CASCADE,
        help_text="What is the labware of this layout item?",
    )
    stack_position = models.PositiveIntegerField()

    class Meta:
        ordering = ["stack_position"]
        unique_together = ("deck_location", "layout_item", "stack_position")

    def __str__(self) -> str:
        return f"LayoutItemStack Pos({self.stack_position}) | {self.layout_item}"

    # TODO: add_to_stack and remove_from_stack methods
