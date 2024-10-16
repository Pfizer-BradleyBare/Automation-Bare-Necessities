from __future__ import annotations

import itertools
from dataclasses import dataclass, field

import xlwings


@dataclass(kw_only=True)
class BlockDefinitionExcelDefinition:
    @dataclass(kw_only=True)
    class _BlockParameterExcelDefinition:
        label: str
        advanced: bool
        default_value: str
        dropdown_items: str
        free_text: bool
        block_field_name: str
        block_field_type: type[float | str]

    name: str
    category: str
    hexidecimal_color: str
    text_hexidecimal_color: str

    parameters: list[_BlockParameterExcelDefinition] = field(
        init=False,
        default_factory=list,
    )

    def add_parameter(
        self,
        *,
        label: str,
        advanced: bool,
        default_value: str,
        dropdown_items: str,
        free_text: bool,
        block_field_name: str,
        block_field_type: type[float | str],
    ) -> None:
        self.parameters.append(
            self._BlockParameterExcelDefinition(
                label=label,
                advanced=advanced,
                default_value=default_value,
                dropdown_items=dropdown_items,
                free_text=free_text,
                block_field_name=block_field_name,
                block_field_type=block_field_type,
            ),
        )


def write_block_definitions_sheet(sheet: xlwings.Sheet):
    from block.models import BlockBase

    cells = []

    for block in BlockBase.block_subclasses.values():
        definition = block.get_excel_definition()

        cells.append(["Block Definition"])
        cells.append(
            ["name", "category", "hexidecimal_color", "text_hexidecimal_color"],
        )
        cells.append(
            [
                definition.name,
                definition.category,
                definition.hexidecimal_color,
                definition.text_hexidecimal_color,
            ],
        )

        cells.append(["Parameter Definitions"])
        cells.append(
            ["label", "advanced", "default_value", "dropdown_items", "free_text"],
        )

        cells += [
            [
                parameter.label,
                parameter.advanced,
                parameter.default_value,
                parameter.dropdown_items,
                parameter.free_text,
            ]
            for parameter in definition.parameters
        ]

        cells.append([])

    cells = list(zip(*itertools.zip_longest(*cells, fillvalue=None)))

    num_rows = len(cells)
    num_cols = 5

    sheet.clear()
    sheet.clear_formats()
    sheet_range = sheet.range((1, 1), (num_rows, num_cols))
    sheet_range.value = cells
    sheet_range.autofit()


def write_container_labwares_sheet(sheet: xlwings.Sheet):
    from plh_config.labware.models import PipettableLabware

    cells = []
    cells.append(["Container Labwares"])

    cells += [[labware.identifier] for labware in PipettableLabware.objects.all()]

    cells = list(zip(*itertools.zip_longest(*cells, fillvalue=None)))

    num_rows = len(cells)
    num_cols = 1

    if num_rows != 0:
        sheet.clear()
        sheet.clear_formats()
        sheet_range = sheet.range((1, 1), (num_rows, num_cols))
        sheet_range.value = cells
        sheet_range.autofit()
