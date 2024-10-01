from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class OverviewComment(BlockBase):

    comment_text = models.TextField()

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
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
        )

        return definition
