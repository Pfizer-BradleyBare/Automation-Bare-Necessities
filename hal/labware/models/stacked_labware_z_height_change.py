from __future__ import annotations

from django.db import models

from .labware_base import LabwareBase


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
