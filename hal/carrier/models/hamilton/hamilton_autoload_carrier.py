from django.db import models
from plh.hamilton_venus.HSLLabwrAccess import TestLabwareIDExists

from debug import plh_logger
from hal.backend.models.hamilton import HamiltonBackendBase

from ..moveable_carrier import MoveableCarrier


class HamiltonAutoloadCarrier(MoveableCarrier):
    backend = models.ForeignKey(to=HamiltonBackendBase, on_delete=models.CASCADE)

    venus_labware_id = models.CharField(
        max_length=255,
        unique=True,
    )

    def initialize(self):
        bound_logger = plh_logger.bind(carrier=str(self), type=type(self).__name__)

        bound_logger.info("Starting carrier initialization.")

        backend = self.backend.get_plh_backend()

        venus_labware_id = self.venus_labware_id

        if venus_labware_id != self.identifier:
            bound_logger.warning(
                f"Identifier '{self.identifier}' and labware_id '{venus_labware_id}' do not match. If intentional, you may ignore. If not, was this a typo?",
            )

        bound_logger.debug("Start run of TestLabwareIDExists command.")

        command = TestLabwareIDExists.Command(
            options=[TestLabwareIDExists.Options(LabwareID=venus_labware_id)],
        )

        backend.execute(command)
        backend.wait(command)
        response = backend.acknowledge(command, TestLabwareIDExists.Response)

        bound_logger.debug("Complete run of TestLabwareIDExists command.")

        if venus_labware_id in response.BadLabwareIDs:
            bound_logger.critical(
                "labware_id is not recognized by the hamilton system. Initialization aborted.",
            )
            raise RuntimeError(
                "labware_id is not recognized by the hamilton system. Initialization aborted.",
            )

        bound_logger.info("Completed carrier initialization.")
