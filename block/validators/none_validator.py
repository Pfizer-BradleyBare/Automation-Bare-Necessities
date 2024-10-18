from typing import Any

from method.models import MethodWorkbookBase


def none_validator(value: Any, _: MethodWorkbookBase) -> bool:
    """Check if the value is a python NoneType (None). Does not expect extra kwargs."""
    return value is None
