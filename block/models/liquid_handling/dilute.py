from __future__ import annotations

from django.db import models

from ...definition import BlockDefinition
from ...validators import (
    container_validator,
    none_validator,
    number_validator,
    predefined_solution_validator,
    user_defined_solution_validator,
)
from ..block_base import (
    DROPDOWN_PREFIXED_CONTAINER_NAMES,
    DROPDOWN_PREFIXED_PREDEFINED_SOLUTION_NAMES,
    DROPDOWN_PREFIXED_USER_DEFINED_SOLUTION_NAMES,
    DROPDOWN_PREFIXED_WORKLIST_COLUMN_NAMES,
    BlockBase,
)


class Dilute(BlockBase):
    solution = models.CharField(max_length=255, null=True)  # noqa: DJ001
    target_concentration = models.CharField(max_length=255, null=True)  # noqa: DJ001
    target_volume = models.CharField(max_length=255, null=True)  # noqa: DJ001

    min_aspirate_mix_cycles = models.CharField(max_length=255, null=True, blank=True)  # noqa: DJ001
    min_dispense_mix_cycles = models.CharField(max_length=255, null=True, blank=True)  # noqa: DJ001
    max_source_volume = models.CharField(max_length=255, null=True, blank=True)  # noqa: DJ001

    @classmethod
    def get_definition(cls) -> BlockDefinition:
        definition = BlockDefinition(
            name="Dilute",
            category="Liquid Handling",
            hexidecimal_color="38A4D0",
            text_hexidecimal_color="000000",
        )

        definition.add_parameter(
            label="Solution",
            advanced=False,
            default_value="",
            dropdown_items=f"{DROPDOWN_PREFIXED_CONTAINER_NAMES},{DROPDOWN_PREFIXED_PREDEFINED_SOLUTION_NAMES},{DROPDOWN_PREFIXED_USER_DEFINED_SOLUTION_NAMES},{DROPDOWN_PREFIXED_WORKLIST_COLUMN_NAMES}",
            free_text=False,
            block_field_name="solution",
            block_field_validators=[
                [
                    container_validator,
                    predefined_solution_validator,
                    user_defined_solution_validator,
                ],
            ],
        )

        definition.add_parameter(
            label="Target Concentration",
            advanced=False,
            default_value="",
            dropdown_items=f"{DROPDOWN_PREFIXED_WORKLIST_COLUMN_NAMES}",
            free_text=True,
            block_field_name="target_concentration",
            block_field_validators=[number_validator, none_validator],
        )

        definition.add_parameter(
            label="Target Volume (uL)",
            advanced=False,
            default_value="",
            dropdown_items=f"{DROPDOWN_PREFIXED_WORKLIST_COLUMN_NAMES}",
            free_text=True,
            block_field_name="target_volume",
            block_field_validators=[number_validator, none_validator],
        )

        definition.add_parameter(
            label="Min Aspirate Mix Cycles",
            advanced=True,
            default_value="10",
            dropdown_items="",
            free_text=True,
            block_field_name="min_aspirate_mix_cycles",
            block_field_validators=[number_validator],
        )

        definition.add_parameter(
            label="Min Dispense Mix Cycles",
            advanced=True,
            default_value="10",
            dropdown_items="",
            free_text=True,
            block_field_name="min_dispense_mix_cycles",
            block_field_validators=[number_validator],
        )

        definition.add_parameter(
            label="Max Source Volume (uL)",
            advanced=True,
            default_value="",
            dropdown_items="",
            free_text=True,
            block_field_name="max_source_volume",
            block_field_validators=[number_validator],
        )

        return definition
