from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class IncubateAndShake(BlockBase):

    temperature = models.CharField(max_length=255)
    shaking_rpm = models.CharField(max_length=255)

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Incubate And Shake",
            category="Heat Cool Shake",
            hexidecimal_color="66cf22",
        )

        definition.add_parameter(
            label="Temperature",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
        )

        definition.add_parameter(
            label="Shaking RPM",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
        )

        return definition
