from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


@dataclass(kw_only=True)
class SolutionDefinition:
    @dataclass(kw_only=True)
    class _SolutionComponent:
        name: str
        amount: float
        unit: Literal["uL", "mg", "units"]

    name: str
    liquid_type: str
    volatility: str
    viscosity: str
    homogeneity: str
    storage_condition: str

    components: list[_SolutionComponent] = field(
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
            self._SolutionComponent(name=name, amount=amount, unit=unit),
        )


@dataclass(kw_only=True)
class SolutionPropertyPresetDefinition:
    name: str
    liquid_type: str
    volatility: str
    viscosity: str
    homogeneity: str
