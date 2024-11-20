from __future__ import annotations

from django.db import models

from .layout_item_base import LayoutItemBase


class LoadedLayoutItem(models.Model):
    layout_item = models.ForeignKey(to=LayoutItemBase, on_delete=models.CASCADE)

    top: models.ForeignKey[LoadedLayoutItem | None] = models.ForeignKey(
        to="LoadedLayoutItem",
        on_delete=models.CASCADE,
        null=True,
        related_name="+",
    )

    bottom: models.ForeignKey[LoadedLayoutItem | None] = models.ForeignKey(
        to="LoadedLayoutItem",
        on_delete=models.CASCADE,
        null=True,
        related_name="+",
    )

    def __str__(self) -> str:
        bottom_labware: list[str] = []
        bottom = self.bottom
        while bottom is not None:
            bottom_labware.append(bottom.layout_item.labware.identifier)
            bottom = bottom.bottom

        top_labware: list[str] = []
        top = self.top
        while top is not None:
            top_labware.append(top.layout_item.labware.identifier)
            top = top.top

        bottom_labware.reverse()
        # reverse because we are assembling from bottom up.

        return f"{' | '.join(bottom_labware)} * {self.layout_item.identifier} * {' | '.join(top_labware)}"
