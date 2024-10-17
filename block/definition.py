from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from method.models import MethodWorkbookBase


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
        block_field_validators: list[
            list[tuple[Callable[[Any, MethodWorkbookBase, tuple], bool], tuple]]
        ]
        """
        IMPORTANT: block_field_validators how does it work???

        A list of list of validators can be provided to be run against a value. 
        The sub list is a validator grouping, thus if any validator returns as true then the value is determined to be valid.
        The tuple parameter in the callable can be used to input extra validation info specific to the validation function.
        If the extra info starts with %% then the value will be replaced (attempted) with the corresponding field value in the model.
        """

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
        block_field_validators: list[
            list[tuple[Callable[[Any, MethodWorkbookBase, tuple], bool], tuple]]
        ],
    ) -> None:
        self.parameters.append(
            self._BlockParameter(
                label=label,
                advanced=advanced,
                default_value=default_value,
                dropdown_items=dropdown_items,
                free_text=free_text,
                block_field_name=block_field_name,
                block_field_validators=block_field_validators,
            ),
        )
