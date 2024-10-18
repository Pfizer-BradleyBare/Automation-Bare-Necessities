from typing import Any

from method.models import MethodWorkbookBase


def none_validator(value: Any, _: MethodWorkbookBase) -> bool:
    """Check if the value is a python NoneType (None). Does not expect extra kwargs. This should only be used with parameters that could come from a worklist column."""
    return value is None
