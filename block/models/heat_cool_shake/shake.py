from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class Shake(BlockBase):

    time = models.CharField(max_length=255)
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
            label="Time (min)",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
        )

        definition.add_parameter(
            label="Shaking Speed (RPM)",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
        )

        return definition

    def assign_parameters(self, parameters: dict):
        self.time = parameters["Time (min)"]
        self.shaking_rpm = parameters["Shaking Speed (RPM)"]
        
        return super().assign_parameters(parameters)