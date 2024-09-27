from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import DROPDOWN_CONTAINER_NAMES, BlockBase


class Merge(BlockBase):
    container_name = models.CharField(max_length=255)
    container_type = models.CharField(max_length=255, default="")

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Merge",
            category="Pathways",
            hexidecimal_color="f3c721",
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
