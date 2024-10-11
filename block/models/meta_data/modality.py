from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class Modality(BlockBase):

    meta_data_text = models.TextField()

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Modality",
            category="Meta Data",
            hexidecimal_color="B085B7",
            text_hexidecimal_color="000000",
        )

        definition.add_parameter(
            label="Modality",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
        )

        return definition

    def assign_parameters(self, parameters: dict):
        
        self.meta_data_text = parameters["Modality"]

        return super().assign_parameters(parameters)