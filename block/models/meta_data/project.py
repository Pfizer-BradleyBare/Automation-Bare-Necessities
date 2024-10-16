from django.db import models

from ...definition import BlockDefinition
from ...validators import free_text_validator
from ..block_base import BlockBase


class Project(BlockBase):
    meta_data_text = models.TextField(null=True)  # noqa:DJ001

    @classmethod
    def get_definition(cls) -> BlockDefinition:
        definition = BlockDefinition(
            name="Project",
            category="Meta Data",
            hexidecimal_color="B085B7",
            text_hexidecimal_color="000000",
        )

        definition.add_parameter(
            label="Project",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
            block_field_name="meta_data_text",
            block_field_validators=[free_text_validator],
        )

        return definition
