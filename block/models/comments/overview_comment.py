from django.db import models

from ...definition import BlockDefinition
from ..block_base import BlockBase


class OverviewComment(BlockBase):
    comment_text = models.TextField(null=True)  # noqa:DJ001

    @classmethod
    def get_definition(cls) -> BlockDefinition:
        definition = BlockDefinition(
            name="Overview Comment",
            category="Comments",
            hexidecimal_color="FFD02E",
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
