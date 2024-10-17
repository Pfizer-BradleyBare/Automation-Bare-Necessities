from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class BlockDefinition:
    @dataclass(kw_only=True)
    class _BlockParameter:
        label: str
        advanced: bool
        default_value: str
        dropdown_items: str
        free_text: bool
        block_field_name: str
        block_field_type: type[float | str]

    name: str
    category: str
    hexidecimal_color: str
    text_hexidecimal_color: str

    parameters: list[_BlockParameter] = field(
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
        block_field_name: str,
        block_field_type: type[float | str],
    ) -> None:
        self.parameters.append(
            self._BlockParameter(
                label=label,
                advanced=advanced,
                default_value=default_value,
                dropdown_items=dropdown_items,
                free_text=free_text,
                block_field_name=block_field_name,
                block_field_type=block_field_type,
            ),
        )
