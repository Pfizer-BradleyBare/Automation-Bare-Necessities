from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import (
    DROPDOWN_CONTAINER_LABWARE_NAMES,
    DROPDOWN_CONTAINER_NAMES,
    BlockBase,
)


class ActivateContainer(BlockBase):
    name = models.CharField(max_length=255, null=True)  # noqa: DJ001
    type = models.CharField(max_length=255, null=True, blank=True)  # noqa: DJ001

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Activate Container",
            category="Pathways",
            hexidecimal_color="6DCE87",
            text_hexidecimal_color="000000",
        )

        definition.add_parameter(
            label="Name",
            advanced=False,
            default_value="",
            dropdown_items=f"{DROPDOWN_CONTAINER_NAMES}",
            free_text=True,
            _field_name="name",
            _field_type=str,
        )
        definition.add_parameter(
            label="Type",
            advanced=True,
            default_value="",
            dropdown_items=f"{DROPDOWN_CONTAINER_LABWARE_NAMES}",
            free_text=False,
            _field_name="type",
            _field_type=str,
        )

        return definition
