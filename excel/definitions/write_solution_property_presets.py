import itertools

import xlwings


def write_solution_property_presets_sheet(sheet: xlwings.Sheet):
    from solution.models import SolutionPropertyPreset

    cells = []
    cells.append(["Preset Definitions"])
    cells.append(["name", "liquid_type", "volatility", "viscosity", "homogeneity"])

    for preset in SolutionPropertyPreset.objects.all():
        definition = preset.get_definition()

        cells.append(
            [
                definition.name,
                definition.liquid_type,
                definition.volatility,
                definition.viscosity,
                definition.homogeneity,
            ],
        )

    cells = list(zip(*itertools.zip_longest(*cells, fillvalue=None)))

    num_rows = len(cells)
    num_cols = 5

    if num_rows != 0:
        sheet.clear()
        sheet.clear_formats()
        sheet_range = sheet.range((1, 1), (num_rows, num_cols))
        sheet_range.value = cells
        sheet_range.autofit()
