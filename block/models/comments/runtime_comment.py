from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class RuntimeComment(BlockBase):

    comment_text = models.TextField()
    wait_for_user_confirmation = models.CharField(max_length=100, blank=True)

    def get_excel_definition(self) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Runtime Comment",
            category="Comments",
            hexidecimal_color="66cf22",
        )

        definition.add_parameter(
            label="Comment Text",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
        )

        definition.add_parameter(
            label="Wait For User Confirmation",
            advanced=True,
            default_value="Wait For User Confirmation",
            dropdown_items="Wait For User Confirmation",
            free_text=False,
        )

        return definition
