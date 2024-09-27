from __future__ import annotations

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


def write_solution_definitions_sheet(sheet: xlwings.Sheet): ...


def write_solution_components_sheet(sheet: xlwings.Sheet): ...
