from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class ConcentrationMin(BlockBase):

    constraint_text = models.TextField()

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Concentration Min",
            category="Constraints",
            hexidecimal_color="FD6F3B",
        )

        definition.add_parameter(
            label="Concentration Min",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
        )

        return definition
