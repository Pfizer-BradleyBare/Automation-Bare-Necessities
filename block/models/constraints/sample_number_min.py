from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class SampleNumberMin(BlockBase):

    constraint_text = models.TextField()

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Sample Number Min",
            category="Constraints",
            hexidecimal_color="66cf22",
        )

        definition.add_parameter(
            label="Sample Number Min",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
        )

        return definition
