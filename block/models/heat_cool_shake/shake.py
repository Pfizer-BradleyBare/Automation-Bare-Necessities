from __future__ import annotations

from django.db import models

from ...definition import BlockDefinition
from ...validators import a_number_validator
from ..block_base import BlockBase


class Shake(BlockBase):
    time = models.CharField(max_length=255, null=True)  # noqa: DJ001
    shaking_rpm = models.CharField(max_length=255, null=True)  # noqa: DJ001

    @classmethod
    def get_definition(cls) -> BlockDefinition:
        definition = BlockDefinition(
            name="Shake",
            category="Heat Cool Shake",
            hexidecimal_color="C5CB57",
            text_hexidecimal_color="000000",
        )

        definition.add_parameter(
            label="Time (min)",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
            block_field_name="time",
            block_field_validators=[a_number_validator],
        )

        definition.add_parameter(
            label="Shaking Speed (RPM)",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
            block_field_name="shaking_rpm",
            block_field_validators=[a_number_validator],
        )

        return definition
