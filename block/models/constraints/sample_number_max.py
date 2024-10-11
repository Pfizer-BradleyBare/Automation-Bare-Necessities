from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class SampleNumberMax(BlockBase):

    constraint_text = models.TextField()

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Sample Number Max",
            category="Constraints",
            hexidecimal_color="FFA74F",
            text_hexidecimal_color="000000",
        )

        definition.add_parameter(
            label="Sample Number Max",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
        )

        return definition


    def assign_parameters(self, parameters: dict):
        self.constraint_text = parameters["Sample Number Max"]
        
        return super().assign_parameters(parameters)