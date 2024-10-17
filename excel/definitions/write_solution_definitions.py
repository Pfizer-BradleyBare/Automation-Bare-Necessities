from __future__ import annotations

import itertools

import xlwings


def write_solution_definitions_sheet(sheet: xlwings.Sheet):
    from solution.models import PredefinedSolution

    cells = []

    for solution in PredefinedSolution.objects.all():
        definition = solution.get_definition()

        cells.append(["Solution Definition"])
        cells.append(
            [
                "name",
                "property_liquid_type",
                "property_volatility",
                "property_viscosity",
                "property_homogeneity",
                "storage_condition",
            ],
        )
        cells.append(
            [
                definition.name,
                definition.liquid_type,
                definition.volatility,
                definition.viscosity,
                definition.homogeneity,
                definition.storage_condition,
            ],
        )

        cells.append(["Components"])
        cells.append(
            ["name", "amount", "units"],
        )

        cells += [
            [
                component.name,
                component.amount,
                component.unit,
            ]
            for component in definition.components
        ]

        cells.append([])

    cells = list(zip(*itertools.zip_longest(*cells, fillvalue=None)))

    num_rows = len(cells)
    num_cols = 6

    if num_rows != 0:
        sheet.clear()
        sheet.clear_formats()
        sheet_range = sheet.range((1, 1), (num_rows, num_cols))
        sheet_range.value = cells
        sheet_range.autofit()
