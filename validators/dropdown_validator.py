from typing import Any

from method.models import MethodWorkbookBase


def dropdown_validator(value: Any, method: MethodWorkbookBase, *args: str) -> bool: ...
