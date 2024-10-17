from typing import Any

from method.models import MethodWorkbookBase


def string_validator(value: Any, method: MethodWorkbookBase, args: tuple) -> bool:
    try:
        str(value)
    except (ValueError, TypeError):
        return False
    else:
        return True
