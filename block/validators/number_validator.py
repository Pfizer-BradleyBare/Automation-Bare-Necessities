from typing import Any

from method.models import MethodWorkbookBase


def number_validator(value: Any, _: MethodWorkbookBase) -> bool:
    """Check if the value is a valid numeric value (float or int). Does not expect extra kwargs."""
    try:
        float(value)
    except (ValueError, TypeError):
        return False

    return True
