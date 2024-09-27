from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class Merge(BlockBase):
    container_name = models.CharField(max_length=255)
    container_type = models.CharField(max_length=255, default="")

    def get_excel_definition(self) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Merge",
            category="Pathways",
            hexidecimal_color="f3c721",
        )

        definition.add_parameter(
            label="Container Name",
            advanced=False,
            default_value="",
            dropdown_items="%%get_container_names_as_string",
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
