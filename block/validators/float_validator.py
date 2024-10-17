from typing import Any

from method.models import MethodWorkbookBase


def float_validator(value: Any, method: MethodWorkbookBase, args: tuple) -> bool:
    try:
        float(value)
    except (ValueError, TypeError):
        return False
    else:
        return True
