from typing import Any

from method.models import MethodWorkbookBase

# from hal.labware.models import LabwareBase


def labware_validator(value: Any, _: MethodWorkbookBase) -> bool:
    """Check if the value is a labware identifier for this systems configuration. Does not expect extra kwargs."""
    return True
    # return LabwareBase.objects.filter(
    #    identifier=value.replace(PREFIX_CONTAINER_LABWARE_NAMES, ""),
    # ).exists()
