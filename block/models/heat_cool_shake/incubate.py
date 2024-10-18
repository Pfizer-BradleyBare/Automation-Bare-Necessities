from django.db import models

from ...definition import BlockDefinition
from ...validators import number_validator
from ..block_base import BlockBase


class Incubate(BlockBase):
    time = models.CharField(max_length=255, null=True)  # noqa: DJ001
    temperature = models.CharField(max_length=255, null=True)  # noqa: DJ001

    @classmethod
    def get_definition(cls) -> BlockDefinition:
        definition = BlockDefinition(
            name="Incubate",
            category="Heat Cool Shake",
            hexidecimal_color="7F8FBE",
            text_hexidecimal_color="000000",
        )

        definition.add_parameter(
            label="Time (min)",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
            block_field_name="time",
            block_field_validators=[number_validator],
        )

        definition.add_parameter(
            label="Temperature (C)",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
            block_field_name="temperature",
            block_field_validators=[number_validator],
        )

        return definition
