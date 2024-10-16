from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import (
    DROPDOWN_CONTAINER_LABWARE_NAMES,
    DROPDOWN_CONTAINER_NAMES,
    DROPDOWN_PREFIXED_WORKLIST_COLUMN_NAMES,
    BlockBase,
)


class SplitWorklist(BlockBase):
    left_container_name = models.CharField(max_length=255, null=True)  # noqa: DJ001
    left_container_type = models.CharField(max_length=255, null=True, blank=True)  # noqa: DJ001

    right_container_name = models.CharField(max_length=255, null=True)  # noqa: DJ001
    right_container_type = models.CharField(max_length=255, null=True, blank=True)  # noqa: DJ001

    container_choice = models.CharField(max_length=255, null=True)  # noqa: DJ001

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Split Worklist",
            category="Pathways",
            hexidecimal_color="A0DAA9",
            text_hexidecimal_color="000000",
        )

        definition.add_parameter(
            label="Left Container Name",
            advanced=False,
            default_value="",
            dropdown_items=f"{DROPDOWN_CONTAINER_NAMES}",
            free_text=True,
            _field_name="left_container_name",
            _field_type=str,
        )

        definition.add_parameter(
            label="Right Container Name",
            advanced=False,
            default_value="",
            dropdown_items=f"{DROPDOWN_CONTAINER_NAMES}",
            free_text=True,
            _field_name="right_container_name",
            _field_type=str,
        )

        definition.add_parameter(
            label="Left Container Type",
            advanced=True,
            default_value="",
            dropdown_items=f"{DROPDOWN_CONTAINER_LABWARE_NAMES}",
            free_text=False,
            _field_name="left_container_type",
            _field_type=str,
        )

        definition.add_parameter(
            label="Right Container Type",
            advanced=True,
            default_value="",
            dropdown_items=f"{DROPDOWN_CONTAINER_LABWARE_NAMES}",
            free_text=False,
            _field_name="right_container_type",
            _field_type=str,
        )

        definition.add_parameter(
            label="Container Choice",
            advanced=False,
            default_value="",
            dropdown_items=f"Both (Full Volume),Both (Half Volume),{DROPDOWN_PREFIXED_WORKLIST_COLUMN_NAMES}",
            free_text=False,
            _field_name="container_choice",
            _field_type=str,
        )

        return definition
