import itertools

import xlwings


def write_container_labwares_sheet(sheet: xlwings.Sheet):
    from hal.container import ContainerBase

    cells = []
    cells.append(["Container Labwares"])

    ContainerBase.subclasses.keys()

    cells += [list(ContainerBase.subclasses.keys())]

    cells = list(zip(*itertools.zip_longest(*cells, fillvalue=None), strict=False))

    num_rows = len(cells)
    num_cols = 1

    if num_rows != 0:
        sheet.clear()
        sheet.clear_formats()
        sheet_range = sheet.range((1, 1), (num_rows, num_cols))
        sheet_range.value = cells
        sheet_range.autofit()
