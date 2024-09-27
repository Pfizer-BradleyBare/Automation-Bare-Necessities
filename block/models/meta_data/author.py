from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class Author(BlockBase):

    meta_data_text = models.TextField()

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Author",
            category="Meta Data",
            hexidecimal_color="66cf22",
        )

        definition.add_parameter(
            label="Author",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
        )

        return definition
