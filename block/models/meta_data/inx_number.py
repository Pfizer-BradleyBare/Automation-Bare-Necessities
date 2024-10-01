from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class INXNumber(BlockBase):

    meta_data_text = models.TextField()

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="INX Number",
            category="Meta Data",
            hexidecimal_color="B085B7",
            text_hexidecimal_color="000000",
        )

        definition.add_parameter(
            label="INX Number",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
        )

        return definition
