from django.db import models

from ...definition import BlockDefinition
from ..block_base import BlockBase


class Author(BlockBase):
    meta_data_text = models.TextField(null=True)  # noqa:DJ001

    @classmethod
    def get_definition(cls) -> BlockDefinition:
        definition = BlockDefinition(
            name="Author",
            category="Meta Data",
            hexidecimal_color="B085B7",
            text_hexidecimal_color="000000",
        )

        definition.add_parameter(
            label="Author",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
            block_field_name="meta_data_text",
            block_field_type=str,
        )

        return definition
