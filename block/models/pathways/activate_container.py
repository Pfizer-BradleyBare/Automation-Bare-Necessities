from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import DROPDOWN_CONTAINER_NAMES, BlockBase


class ActivateContainer(BlockBase):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True)

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Activate Container",
            category="Pathways",
            hexidecimal_color="2BAE66",
        )

        definition.add_parameter(
            label="Name",
            advanced=False,
            default_value="",
            dropdown_items=f"{DROPDOWN_CONTAINER_NAMES}",
            free_text=True,
        )
        definition.add_parameter(
            label="Type",
            advanced=True,
            default_value="TODO",
            dropdown_items="TODO",
            free_text=False,
        )

        return definition
