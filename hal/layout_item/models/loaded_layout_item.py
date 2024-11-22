from __future__ import annotations

from itertools import pairwise

from django.db import models

from hal.labware.models import LabwareBase, StackedLabwareZHeightChange

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

    def assert_supported_stack(self):
        stack_pairs = list(
            pairwise([item.layout_item.labware for item in self.top_items]),
        )

        q_query = models.Q()

        for bottom, top in stack_pairs:
            q_query |= models.Q(bottom_labware=bottom, top_labware=top)
        # We do it this way first because a single query would be much faster.

        if StackedLabwareZHeightChange.objects.filter(q_query).count() != len(
            stack_pairs,
        ):
            failed_stack_pairs: list[tuple[LabwareBase, LabwareBase]] = []

            for bottom, top in stack_pairs:
                if not StackedLabwareZHeightChange.objects.filter(
                    bottom_labware=bottom,
                    top_labware=top,
                ).exists():
                    failed_stack_pairs.append((bottom, top))
            # If it fails we do it this way because throwing an error is not time sensitive.

            raise ValueError(
                f"The following labware stack pairs are not supported: {failed_stack_pairs}",
            )

    def compute_stack_z_dimension(self) -> float:
        labware_stack = [item.layout_item.labware for item in self.top_items]

        labware_z_dimensions = [labware.height for labware in labware_stack]

        nesting_z_heights = [
            StackedLabwareZHeightChange.objects.filter(
                bottom_labware=bottom,
                top_labware=top,
            )
            .get()
            .z_height_change
            for bottom, top in pairwise(labware_stack)
        ]

        return sum(labware_z_dimensions + nesting_z_heights)

    def compute_stack_x_dimension(self) -> float:
        labware_stack = [item.layout_item.labware for item in self.top_items]

        return max(
            [
                max([x for x, _, _ in labware.x_y_z_dimensions])
                for labware in labware_stack
            ],
        )

    def compute_stack_y_dimension(self) -> float:
        labware_stack = [item.layout_item.labware for item in self.top_items]

        return max(
            [
                max([y for y, _, _ in labware.x_y_z_dimensions])
                for labware in labware_stack
            ],
        )
