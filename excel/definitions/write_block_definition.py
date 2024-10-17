import itertools

import xlwings


def write_block_definitions_sheet(sheet: xlwings.Sheet):
    from block.models import BlockBase

    cells = []

    for block in BlockBase.block_subclasses.values():
        definition = block.get_block_definition()

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
