import itertools

import xlwings


def write_container_labwares_sheet(sheet: xlwings.Sheet):
    from hal.labware.models import PipettableLabware
    from hal.layout_item.models import LayoutItemBase

    cells = []
    cells.append(["Container Labwares"])

    cells += [
        [
            layout_item.labware.container.identifier
            for layout_item in LayoutItemBase.objects.all()
            if isinstance(layout_item.labware, PipettableLabware)
        ],
    ]

    cells = list(zip(*itertools.zip_longest(*cells, fillvalue=None), strict=False))

    num_rows = len(cells)
    num_cols = 1

    if num_rows != 0:
        sheet.clear()
        sheet.clear_formats()
        sheet_range = sheet.range((1, 1), (num_rows, num_cols))
        sheet_range.value = cells
        sheet_range.autofit()
