from typing import Any

from method.models import MethodWorkbookBase


def container_validator(
    value: Any,
    method: MethodWorkbookBase,
    args: tuple,
) -> bool:
    from ..models.block_base import PREFIX_CONTAINER_NAMES
    from ..models.pathways import ActivateContainer

    return ActivateContainer.objects.filter(
        name=value.replace(PREFIX_CONTAINER_NAMES, ""),
        method=method,
    ).exists()
