from typing import Any

from method.models import MethodWorkbookBase
from solution.models import PredefinedSolution


def predefined_solution_validator(value: Any, _: MethodWorkbookBase) -> bool:
    """Check if the value is the name of a PredefinedSolution for the system configuration. Does not expect extra kwargs."""
    from ..models.block_base import PREFIX_PREDEFINED_SOLUTION_NAMES

    return PredefinedSolution.objects.filter(
        name=value.replace(PREFIX_PREDEFINED_SOLUTION_NAMES, ""),
    ).exists()
