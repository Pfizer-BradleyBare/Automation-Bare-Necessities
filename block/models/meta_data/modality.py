from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class Modality(BlockBase):
    meta_data_text = models.TextField(null=True)  # noqa:DJ001

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Modality",
            category="Meta Data",
            hexidecimal_color="B085B7",
            text_hexidecimal_color="000000",
        )

        definition.add_parameter(
            label="Modality",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
            _field_name="meta_data_text",
            _field_type=str,
        )

        return definition
