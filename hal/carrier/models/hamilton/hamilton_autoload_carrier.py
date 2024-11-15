from django.db import models
from plh.hamilton_venus.HSLLabwrAccess import TestLabwareIDExists

from debug import plh_logger
from hal.backend.models.hamilton import HamiltonBackendBase

from ..moveable_carrier import MoveableCarrier


class HamiltonAutoloadCarrier(MoveableCarrier):
    backend = models.ForeignKey(to=HamiltonBackendBase, on_delete=models.CASCADE)

    carrier_labware_id = models.CharField(
        max_length=50,
        unique=True,
    )

    def initialize(self):
        backend = self.backend.get_plh_backend()

        labware_id = self.carrier_labware_id

        command = TestLabwareIDExists.Command(
            options=[TestLabwareIDExists.Options(LabwareID=labware_id)],
        )

        backend.execute(command)
        backend.wait(command)
        response = backend.acknowledge(command, TestLabwareIDExists.Response)

        if labware_id in response.BadLabwareIDs:
            plh_logger.critical(
                f"HamiltonAutoloadCarrier '{self.identifier}' carrier_labware_id is not recognized by the hamilton system. Initialization aborted.",
            )
            raise RuntimeError(
                f"HamiltonAutoloadCarrier '{self.identifier}' carrier_labware_id is not recognized by the hamilton system. Initialization aborted.",
            )
