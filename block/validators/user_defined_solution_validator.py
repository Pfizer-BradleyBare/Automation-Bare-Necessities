from typing import Any

from method.models import MethodWorkbookBase
from solution.models import UserDefinedSolution


def user_defined_solution_validator(value: Any, method: MethodWorkbookBase) -> bool:
    """Check if the value is the name of a UserDefinedSolution for the given method. Does not expect extra kwargs."""
    from ..models.block_base import PREFIX_USER_DEFINED_SOLUTION_NAMES

    return UserDefinedSolution.objects.filter(
        name=value.replace(PREFIX_USER_DEFINED_SOLUTION_NAMES, ""),
        method=method,
    ).exists()
