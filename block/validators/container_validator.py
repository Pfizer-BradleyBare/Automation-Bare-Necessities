from typing import Any

from method.models import MethodWorkbookBase


def container_validator(value: Any, method: MethodWorkbookBase) -> bool:
    """Check if the value is the name of a container for the given method. Does not expect extra kwargs."""
    from ..models.block_base import PREFIX_CONTAINER_NAMES
    from ..models.pathways import ActivateContainer

    return ActivateContainer.objects.filter(
        name=value.replace(PREFIX_CONTAINER_NAMES, ""),
        method=method,
    ).exists()
