from typing import Any

from method.models import MethodWorkbookBase
from solution.models import PredefinedSolution


def predefined_solution_validator(
    value: Any,
    method: MethodWorkbookBase,
    args: tuple,
) -> bool:
    from ..models.block_base import PREFIX_PREDEFINED_SOLUTION_NAMES

    return PredefinedSolution.objects.filter(
        name=value.replace(PREFIX_PREDEFINED_SOLUTION_NAMES, ""),
    ).exists()
