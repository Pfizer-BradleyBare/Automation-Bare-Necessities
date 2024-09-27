from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class SampleNumberMax(BlockBase):

    constraint_text = models.TextField()

    def get_excel_definition(self) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Sample Number Max",
            category="Constraints",
            hexidecimal_color="66cf22",
        )

        definition.add_parameter(
            label="Sample Number Max",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
        )

        return definition
