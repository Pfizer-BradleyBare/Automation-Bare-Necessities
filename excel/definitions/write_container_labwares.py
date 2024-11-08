import itertools

import xlwings


def write_container_labwares_sheet(sheet: xlwings.Sheet):
    from hal.labware.models import LabwareBase,PipettableLabwareMixin

    cells = []
    cells.append(["Container Labwares"])

    cells += [[labware.identifier] for labware in LabwareBase.objects.all() if isinstance(labware,PipettableLabwareMixin)] 

    cells = list(zip(*itertools.zip_longest(*cells, fillvalue=None)))

    num_rows = len(cells)
    num_cols = 1

    if num_rows != 0:
        sheet.clear()
        sheet.clear_formats()
        sheet_range = sheet.range((1, 1), (num_rows, num_cols))
        sheet_range.value = cells
        sheet_range.autofit()
