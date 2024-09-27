from __future__ import annotations

from dataclasses import dataclass, field

import xlwings


@dataclass(kw_only=True)
class BlockDefinitionExcelDefinition:

    @dataclass(kw_only=True)
    class _BlockParameterExcelDefinition:
        label: str
        advanced: bool
        default_value: str
        dropdown_items: str
        free_text: bool

    name: str
    category: str
    hexidecimal_color: str

    parameters: list[_BlockParameterExcelDefinition] = field(
        init=False,
        default_factory=list,
    )

    def add_parameter(
        self,
        *,
        label: str,
        advanced: bool,
        default_value: str,
        dropdown_items: str,
        free_text: bool,
    ) -> None:
        self.parameters.append(
            self._BlockParameterExcelDefinition(
                label=label,
                advanced=advanced,
                default_value=default_value,
                dropdown_items=dropdown_items,
                free_text=free_text,
            ),
        )


def write_block_definitions_sheet(sheet: xlwings.Sheet): ...
