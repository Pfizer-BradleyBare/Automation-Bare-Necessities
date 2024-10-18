from typing import Any

from method.models import MethodWorkbookBase
from plh_config.labware.models import PipettableLabware


def labware_validator(value: Any, _: MethodWorkbookBase) -> bool:
    """Check if the value is a labware identifier for this systems configuration. Does not expect extra kwargs."""
    from ..models.block_base import PREFIX_CONTAINER_LABWARE_NAMES

    return PipettableLabware.objects.filter(
        identifier=value.replace(PREFIX_CONTAINER_LABWARE_NAMES, ""),
    ).exists()
