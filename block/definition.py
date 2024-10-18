from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Concatenate

from method.models import MethodWorkbookBase

validator_function = Callable[Concatenate[Any, MethodWorkbookBase, ...], bool]
extra_kwargs = dict[str, Any]


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
            list[tuple[validator_function, extra_kwargs] | validator_function]
            | tuple[validator_function, extra_kwargs]
            | validator_function
        ]
        """
        IMPORTANT: block_field_validators how does it work???

        A list of list of validators can be provided to be run against a value. 
        The sub list is a validator grouping, thus if any validator returns as true then the value is determined to be valid (used for validating worklist columns).
        An optional dictionary of kwargs can be supplied as required by the validator function.
        If any kwargs start with %% then the value will be replaced (attempted) with the corresponding field value in the model.
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
            list[tuple[validator_function, extra_kwargs] | validator_function]
            | tuple[validator_function, extra_kwargs]
            | validator_function
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
