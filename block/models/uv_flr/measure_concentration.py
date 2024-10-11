from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase
from ..block_base import DROPDOWN_PREFIXED_WORKLIST_COLUMN_NAMES


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

    def assign_parameters(self, parameters: dict):

        self.output_worklist_column = parameters["Output Worklist Column"]
        self.extinction_coefficient = parameters["Extinction Coefficient"]

        return super().assign_parameters(parameters)