from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import DROPDOWN_CONTAINER_NAMES, BlockBase


class SplitWorklist(BlockBase):
    left_container_name = models.CharField(max_length=255)
    left_container_type = models.CharField(max_length=255, default="")

    right_container_name = models.CharField(max_length=255)
    right_container_type = models.CharField(max_length=255, default="")

    container_choice = models.CharField(max_length=255)

    def get_excel_definition(self) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Split Worklist",
            category="Pathways",
            hexidecimal_color="f3c721",
        )

        definition.add_parameter(
            label="Left Container Name",
            advanced=False,
            default_value="",
            dropdown_items=f"{DROPDOWN_CONTAINER_NAMES}",
            free_text=True,
        )

        definition.add_parameter(
            label="Right Container Name",
            advanced=False,
            default_value="",
            dropdown_items=f"{DROPDOWN_CONTAINER_NAMES}",
            free_text=True,
        )

        definition.add_parameter(
            label="Left Container Type",
            advanced=True,
            default_value="TODO",
            dropdown_items="TODO",
            free_text=False,
        )

        definition.add_parameter(
            label="Right Container Type",
            advanced=True,
            default_value="TODO",
            dropdown_items="TODO",
            free_text=False,
        )

        definition.add_parameter(
            label="Right Container Type",
            advanced=True,
            default_value="TODO",
            dropdown_items="TODO",
            free_text=False,
        )

        return definition
