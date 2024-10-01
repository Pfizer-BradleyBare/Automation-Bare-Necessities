from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import (
    DROPDOWN_PREFIXED_CONTAINER_NAMES,
    DROPDOWN_PREFIXED_PREDEFINED_SOLUTION_NAMES,
    DROPDOWN_PREFIXED_USER_DEFINED_SOLUTION_NAMES,
    DROPDOWN_PREFIXED_WORKLIST_COLUMN_NAMES,
    BlockBase,
)


class Pipette(BlockBase):

    solution = models.CharField(max_length=255)
    volume = models.CharField(max_length=255)

    min_aspirate_mix_cycles = models.CharField(max_length=255, blank=True)
    min_dispense_mix_cycles = models.CharField(max_length=255, blank=True)

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Pipette",
            category="Liquid Handling",
            hexidecimal_color="007BB2",
            text_hexidecimal_color="000000",
        )

        definition.add_parameter(
            label="Solution",
            advanced=False,
            default_value="",
            dropdown_items=f"{DROPDOWN_PREFIXED_CONTAINER_NAMES},{DROPDOWN_PREFIXED_PREDEFINED_SOLUTION_NAMES},{DROPDOWN_PREFIXED_USER_DEFINED_SOLUTION_NAMES},{DROPDOWN_PREFIXED_WORKLIST_COLUMN_NAMES}",
            free_text=False,
        )

        definition.add_parameter(
            label="Volume (uL)",
            advanced=False,
            default_value="",
            dropdown_items=f"{DROPDOWN_PREFIXED_WORKLIST_COLUMN_NAMES}",
            free_text=True,
        )

        definition.add_parameter(
            label="Min Aspirate Mix Cycles",
            advanced=True,
            default_value="10",
            dropdown_items="",
            free_text=True,
        )

        definition.add_parameter(
            label="Min Dispense Mix Cycles",
            advanced=True,
            default_value="10",
            dropdown_items="",
            free_text=True,
        )

        return definition
