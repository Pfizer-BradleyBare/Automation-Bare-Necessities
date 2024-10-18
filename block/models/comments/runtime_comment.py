from django.db import models

from ...definition import BlockDefinition
from ...validators import dropdown_validator, free_text_validator
from ..block_base import BlockBase


class RuntimeComment(BlockBase):
    comment_text = models.TextField(null=True)  # noqa:DJ001
    wait_for_user_confirmation = models.CharField(max_length=100, blank=True, null=True)  # noqa:DJ001)

    @classmethod
    def get_definition(cls) -> BlockDefinition:
        definition = BlockDefinition(
            name="Runtime Comment",
            category="Comments",
            hexidecimal_color="F7EF70",
            text_hexidecimal_color="000000",
        )

        definition.add_parameter(
            label="Comment Text",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
            block_field_name="comment_text",
            block_field_validators=[free_text_validator],
        )

        definition.add_parameter(
            label="Wait For User Confirmation",
            advanced=True,
            default_value="Yes",
            dropdown_items="Yes",
            free_text=False,
            block_field_name="wait_for_user_confirmation",
            block_field_validators=[
                (dropdown_validator, {"acceptable_values": ["Yes"]}),
            ],
        )

        return definition
