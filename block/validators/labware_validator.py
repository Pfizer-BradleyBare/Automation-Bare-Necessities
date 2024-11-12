from typing import Any

from hal.labware.models import PipettableLabware
from hal.layout_item.models import LayoutItemBase
from method.models import MethodWorkbookBase


def labware_validator(value: Any, _: MethodWorkbookBase) -> bool:
    """Check if the value is a labware identifier for this systems configuration. Does not expect extra kwargs."""
    from ..models.block_base import PREFIX_CONTAINER_LABWARE_NAMES

    return value.replace(PREFIX_CONTAINER_LABWARE_NAMES, "") in {
        layout_item.labware.container.identifier
        for layout_item in LayoutItemBase.objects.all()
        if isinstance(layout_item.labware, PipettableLabware)
    }
