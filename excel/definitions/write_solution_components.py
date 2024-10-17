from __future__ import annotations

import itertools

import xlwings


def write_solution_components_sheet(sheet: xlwings.Sheet):
    from solution.models import PredefinedComponent

    cells = []
    cells.append(["Solution Components"])

    cells += [[component.name] for component in PredefinedComponent.objects.all()]

    cells = list(zip(*itertools.zip_longest(*cells, fillvalue=None)))

    num_rows = len(cells)
    num_cols = 1

    if num_rows != 0:
        sheet.clear()
        sheet.clear_formats()
        sheet_range = sheet.range((1, 1), (num_rows, num_cols))
        sheet_range.value = cells
        sheet_range.autofit()
