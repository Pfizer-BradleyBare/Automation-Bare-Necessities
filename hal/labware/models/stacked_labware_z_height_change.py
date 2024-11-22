from __future__ import annotations

from itertools import pairwise
from typing import TYPE_CHECKING

from django.db import models

from .labware_base import LabwareBase

if TYPE_CHECKING:
    from hal.layout_item.models import LoadedLayoutItem


class StackedLabwareZHeightChange(models.Model):
    bottom_labware = models.ForeignKey(
        to=LabwareBase,
        on_delete=models.CASCADE,
        help_text="The bottom labware of the stack.",
        related_name="stackedlabwarezheightchangebottom_set",
    )
    top_labware = models.ForeignKey(
        to=LabwareBase,
        on_delete=models.CASCADE,
        help_text="The top labware of the stack.",
        related_name="stackedlabwarezheightchangetop_set",
    )
    z_height_change = models.FloatField(
        help_text="How much does the top labware nest into the bottom labware. Should always be equal to or less than 0. Ex. <stacked_labware_height> - (<top labware height> + <bottom labware height>)",
    )

    @classmethod
    def assert_supported_stack(cls, base: LoadedLayoutItem):
        stack_pairs = list(
            pairwise([item.layout_item.labware for item in base.top_items]),
        )

        q_query = models.Q()

        for bottom, top in stack_pairs:
            q_query |= models.Q(bottom_labware=bottom, top_labware=top)
        # We do it this way first because a single query would be much faster.

        if cls.objects.filter(q_query).count() != len(
            stack_pairs,
        ):
            failed_stack_pairs: list[tuple[LabwareBase, LabwareBase]] = []

            for bottom, top in stack_pairs:
                if not cls.objects.filter(
                    bottom_labware=bottom,
                    top_labware=top,
                ).exists():
                    failed_stack_pairs.append((bottom, top))
            # If it fails we do it this way because throwing an error is not time sensitive.

            raise ValueError(
                f"The following labware stack pairs are not supported: {failed_stack_pairs}",
            )

    @staticmethod
    def compute_stack_z_dimension(base: LoadedLayoutItem) -> float:
        labware_stack = [item.layout_item.labware for item in base.top_items]

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

    @staticmethod
    def compute_stack_x_dimension(base: LoadedLayoutItem) -> float:
        labware_stack = [item.layout_item.labware for item in base.top_items]

        return max(
            [
                max([x for x, _, _ in labware.x_y_z_dimensions])
                for labware in labware_stack
            ],
        )

    @staticmethod
    def compute_stack_y_dimension(base: LoadedLayoutItem) -> float:
        labware_stack = [item.layout_item.labware for item in base.top_items]

        return max(
            [
                max([y for y, _, _ in labware.x_y_z_dimensions])
                for labware in labware_stack
            ],
        )
