from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class Rest(BlockBase):

    time = models.CharField(max_length=255)

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Rest",
            category="Heat Cool Shake",
            hexidecimal_color="7F8FBE",
            text_hexidecimal_color="000000",
        )

        definition.add_parameter(
            label="Time (min)",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
        )

        return definition