from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class Category(BlockBase):

    meta_data_text = models.TextField()

    def get_excel_definition(self) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Category",
            category="Meta Data",
            hexidecimal_color="66cf22",
        )

        definition.add_parameter(
            label="Category",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
        )

        return definition
