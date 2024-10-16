from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class ConcentrationMax(BlockBase):
    constraint_text = models.TextField(null=True)  # noqa:DJ001

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Concentration Max",
            category="Constraints",
            hexidecimal_color="FF8C55",
            text_hexidecimal_color="000000",
        )

        definition.add_parameter(
            label="Concentration Max",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
            _field_name="constraint_text",
            _field_type=str,
        )

        return definition
