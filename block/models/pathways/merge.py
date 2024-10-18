from django.db import models

from ...definition import BlockDefinition
from ...validators import container_validator, free_text_validator, labware_validator
from ..block_base import (
    DROPDOWN_CONTAINER_LABWARE_NAMES,
    DROPDOWN_CONTAINER_NAMES,
    BlockBase,
)


class Merge(BlockBase):
    container_name = models.CharField(max_length=255, null=True)  # noqa: DJ001
    container_type = models.CharField(max_length=255, null=True, blank=True)  # noqa: DJ001

    @classmethod
    def get_definition(cls) -> BlockDefinition:
        definition = BlockDefinition(
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
            block_field_name="container_name",
            block_field_validators=[container_validator, free_text_validator],
        )

        definition.add_parameter(
            label="Container Type",
            advanced=True,
            default_value="",
            dropdown_items=f"{DROPDOWN_CONTAINER_LABWARE_NAMES}",
            free_text=False,
            block_field_name="container_type",
            block_field_validators=[labware_validator],
        )

        return definition
