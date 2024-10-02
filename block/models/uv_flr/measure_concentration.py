from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import DROPDOWN_PREFIXED_WORKLIST_COLUMN_NAMES, BlockBase


class MeasureConcentration(BlockBase):

    output_worklist_column = models.CharField(max_length=255)
    extinction_coefficient = models.CharField(max_length=255)

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Measure Concentration",
            category="UV / FLR",
            hexidecimal_color="EDC0AA",
            text_hexidecimal_color="000000",
        )

        definition.add_parameter(
            label="Output Worklist Column",
            advanced=False,
            default_value="",
            dropdown_items=f"{DROPDOWN_PREFIXED_WORKLIST_COLUMN_NAMES}",
            free_text=False,
        )

        definition.add_parameter(
            label="Extinction Coefficient",
            advanced=False,
            default_value="",
            dropdown_items=f"{DROPDOWN_PREFIXED_WORKLIST_COLUMN_NAMES}",
            free_text=False,
        )

        return definition