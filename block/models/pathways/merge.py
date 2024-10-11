from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import DROPDOWN_CONTAINER_NAMES, BlockBase


class Merge(BlockBase):
    container_name = models.CharField(max_length=255)
    container_type = models.CharField(max_length=255, blank=True)

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Merge",
            category="Pathways",
            hexidecimal_color="A0DAA9",
            text_hexidecimal_color="000000",
        )

        definition.add_parameter(
            label="Container Name",
            advanced=False,
            default_value="",
            dropdown_items=f"{DROPDOWN_CONTAINER_NAMES}",
            free_text=True,
        )
        definition.add_parameter(
            label="Container Type",
            advanced=True,
            default_value="TODO",
            dropdown_items="TODO",
            free_text=False,
        )

        return definition

    def assign_parameters(self, parameters: dict):
        self.container_name = parameters["Container Name"]

        try:
            self.container_type = parameters["Container Type"]
        except KeyError:
            self.container_type = ""

        return super().assign_parameters(parameters)