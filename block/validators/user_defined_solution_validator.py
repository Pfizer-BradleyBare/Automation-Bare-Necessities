from typing import Any

from method.models import MethodWorkbookBase
from solution.models import UserDefinedSolution


def user_defined_solution_validator(
    value: Any,
    method: MethodWorkbookBase,
    args: tuple,
) -> bool:
    from ..models.block_base import PREFIX_USER_DEFINED_SOLUTION_NAMES

    return UserDefinedSolution.objects.filter(
        name=value.replace(PREFIX_USER_DEFINED_SOLUTION_NAMES, ""),
        method=method,
    ).exists()
