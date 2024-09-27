from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class SilentComment(BlockBase):

    comment_text = models.TextField()

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Silent Comment",
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

        return definition
