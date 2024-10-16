from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class RuntimeComment(BlockBase):
    comment_text = models.TextField(null=True)  # noqa:DJ001
    wait_for_user_confirmation = models.CharField(max_length=100, blank=True, null=True)  # noqa:DJ001)

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
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
            _field_name="comment_text",
            _field_type=str,
        )

        definition.add_parameter(
            label="Wait For User Confirmation",
            advanced=True,
            default_value="Yes",
            dropdown_items="Yes",
            free_text=False,
            _field_name="wait_for_user_confirmation",
            _field_type=str,
        )

        return definition
