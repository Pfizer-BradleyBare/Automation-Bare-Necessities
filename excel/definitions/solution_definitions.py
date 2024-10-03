from __future__ import annotations

import itertools
from dataclasses import dataclass, field
from typing import Literal

import xlwings


@dataclass(kw_only=True)
class SolutionDefinitionExcelDefinition:

    @dataclass(kw_only=True)
    class _SolutionComponentExcelDefinition:
        name: str
        amount: float
        unit: Literal["uL", "mg", "units"]

    name: str
    liquid_type: str
    volatility: str
    viscosity: str
    homogeneity: str
    storage_condition: str

    components: list[_SolutionComponentExcelDefinition] = field(
        init=False,
        default_factory=list,
    )

    def add_component(
        self,
        *,
        name: str,
        amount: float,
        unit: Literal["uL", "mg", "units"],
    ) -> None:
        self.components.append(
            self._SolutionComponentExcelDefinition(name=name, amount=amount, unit=unit),
        )


def write_solution_definitions_sheet(sheet: xlwings.Sheet):
    from solution.models import PredefinedSolution

    cells = []

    for solution in PredefinedSolution.objects.all():
        definition = solution.get_excel_definition()

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
