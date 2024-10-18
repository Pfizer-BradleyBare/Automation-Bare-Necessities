from typing import Any

from method.models import MethodWorkbookBase
from worklist.models import WorklistColumn


def worklist_column_validator(value: Any, method: MethodWorkbookBase) -> bool:
    """Check if the value is the name of a container for the given method. Does not expect extra kwargs."""
    from ..models.block_base import PREFIX_WORKLIST_COLUMN_NAMES

    return WorklistColumn.objects.filter(
        name=value.replace(PREFIX_WORKLIST_COLUMN_NAMES, ""),
        method=method,
    ).exists()
