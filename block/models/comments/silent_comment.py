from django.db import models

from ...definition import BlockDefinition
from ..block_base import BlockBase


class SilentComment(BlockBase):
    comment_text = models.TextField(null=True)  # noqa:DJ001

    @classmethod
    def get_definition(cls) -> BlockDefinition:
        definition = BlockDefinition(
            name="Silent Comment",
            category="Comments",
            hexidecimal_color="FED877",
            text_hexidecimal_color="000000",
        )

        definition.add_parameter(
            label="Comment Text",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
            block_field_name="comment_text",
            block_field_type=str,
        )

        return definition
