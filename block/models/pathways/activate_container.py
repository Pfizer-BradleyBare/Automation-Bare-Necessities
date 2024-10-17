from django.db import models

from ...definition import BlockDefinition
from ...validators import container_validator, labware_validator, string_validator
from ..block_base import (
    DROPDOWN_CONTAINER_LABWARE_NAMES,
    DROPDOWN_CONTAINER_NAMES,
    BlockBase,
)


class ActivateContainer(BlockBase):
    name = models.CharField(max_length=255, null=True)  # noqa: DJ001
    type = models.CharField(max_length=255, null=True, blank=True)  # noqa: DJ001

    @classmethod
    def get_definition(cls) -> BlockDefinition:
        definition = BlockDefinition(
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
            block_field_name="name",
            block_field_validators=[
                [(container_validator, ()), (string_validator, ())],
            ],
        )
        definition.add_parameter(
            label="Type",
            advanced=True,
            default_value="",
            dropdown_items=f"{DROPDOWN_CONTAINER_LABWARE_NAMES}",
            free_text=False,
            block_field_name="type",
            block_field_validators=[[(labware_validator, ())]],
        )

        return definition
