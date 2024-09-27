from dataclasses import dataclass

import xlwings


@dataclass(kw_only=True)
class SolutionPropertyPresetExcelDefinition:
    name: str
    liquid_type: str
    volatility: str
    viscosity: str
    homogeneity: str


def write_solution_property_presets_sheet(sheet: xlwings.Sheet): ...
