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
        bottom_labware_names = [
            item.layout_item.labware.identifier for item in self.bottom_items
        ]
        top_labware_names = [
            item.layout_item.labware.identifier for item in self.top_items
        ]

        return f"{' | '.join(bottom_labware_names)} * {self.layout_item.identifier} * {' | '.join(top_labware_names)}"

    @property
    def top_items(self) -> list[LoadedLayoutItem]:
        """Return items above the current loaded layout item in ascending order."""
        top_labware: list[LoadedLayoutItem] = []
        top = self.top
        while top is not None:
            top_labware.append(top)
            top = top.top

        return top_labware

    @property
    def absolute_top_item(self) -> LoadedLayoutItem:
        return self.top_items[-1]

    @property
    def is_absolute_top_item(self) -> bool:
        return self.top is None

    @property
    def bottom_items(self) -> list[LoadedLayoutItem]:
        """Return items below the current loaded layout item in ascending order."""
        bottom_labware: list[LoadedLayoutItem] = []
        bottom = self.bottom

        while bottom is not None:
            bottom_labware.append(bottom)
            bottom = bottom.bottom

        return bottom_labware[::-1]
        # reverse it so the order is ascending

    @property
    def absolute_bottom_item(self) -> LoadedLayoutItem:
        return self.top_items[0]

    @property
    def is_absolute_bottom_item(self) -> bool:
        return self.bottom is None
