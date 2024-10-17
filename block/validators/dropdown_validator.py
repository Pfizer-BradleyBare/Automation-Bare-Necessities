from typing import Any

from method.models import MethodWorkbookBase


def dropdown_validator(value: Any, method: MethodWorkbookBase, args: tuple) -> bool:
    acceptable_dropdown_values = list(args)

    return value in acceptable_dropdown_values
