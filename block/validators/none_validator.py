from typing import Any

from method.models import MethodWorkbookBase


def none_validator(value: Any, method: MethodWorkbookBase, args: tuple) -> bool:
    return value is None
