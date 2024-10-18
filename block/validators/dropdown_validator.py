from __future__ import annotations

from typing import Any

from method.models import MethodWorkbookBase


def dropdown_validator(
    value: Any,
    _: MethodWorkbookBase,
    acceptable_values: list[str],
) -> bool:
    """Check if the value is a valid acceptable value present in a dropdown. Expects -> acceptable_values: list[str]."""
    return value in acceptable_values
