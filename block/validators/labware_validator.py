from typing import Any

from method.models import MethodWorkbookBase
from plh_config.labware.models import PipettableLabware


def labware_validator(
    value: Any,
    method: MethodWorkbookBase,
    args: tuple,
) -> bool:
    from ..models.block_base import PREFIX_CONTAINER_LABWARE_NAMES

    return PipettableLabware.objects.filter(
        identifier=value.replace(PREFIX_CONTAINER_LABWARE_NAMES, ""),
    ).exists()
