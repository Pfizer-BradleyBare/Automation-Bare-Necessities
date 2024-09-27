from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class Scale(BlockBase):

    meta_data_text = models.TextField()

    def get_excel_definition(self) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Scale",
            category="Meta Data",
            hexidecimal_color="66cf22",
        )

        definition.add_parameter(
            label="Scale",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
        )

        return definition
