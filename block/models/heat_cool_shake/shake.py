from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class Shake(BlockBase):

    shaking_rpm = models.CharField(max_length=255)

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Shake",
            category="Heat Cool Shake",
            hexidecimal_color="C5CB57",
            text_hexidecimal_color="000000",
        )

        definition.add_parameter(
            label="Shaking RPM",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
        )

        return definition
