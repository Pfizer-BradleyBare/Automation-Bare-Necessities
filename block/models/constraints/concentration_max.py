from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class ConcentrationMax(BlockBase):

    constraint_text = models.TextField()

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Concentration Max",
            category="Constraints",
            hexidecimal_color="FD6F3B",
        )

        definition.add_parameter(
            label="Concentration Max",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
        )

        return definition
