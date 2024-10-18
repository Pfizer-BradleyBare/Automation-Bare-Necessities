from typing import Any

from method.models import MethodWorkbookBase


def free_text_validator(value: Any, _: MethodWorkbookBase) -> bool:
    """Check if the value is valid free text(string). Does not expect extra kwargs."""
    try:
        str(value)
    except (ValueError, TypeError):
        return False

    return True
