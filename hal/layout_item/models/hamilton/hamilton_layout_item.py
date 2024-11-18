from __future__ import annotations

from django.db import models
from plh.hamilton_venus.HSLLabwrAccess import TestLabwareIDExists

from debug import plh_logger
from hal.backend.models.hamilton import HamiltonBackendBase

from ..layout_item_base import LayoutItemBase


class HamiltonLayoutItem(LayoutItemBase):
    backend = models.ForeignKey(to=HamiltonBackendBase, on_delete=models.CASCADE)

    venus_labware_id = models.CharField(
        max_length=255,
        unique=True,
    )

    def initialize(self):
        backend = self.backend.get_plh_backend()

        venus_labware_id = self.venus_labware_id

        if venus_labware_id != self.identifier:
            plh_logger.warning(
                f"HamiltonLayoutItem identifier '{self.identifier}' and labware_id '{venus_labware_id}' do not match. If intentional, you may ignore. If not, was this a typo?",
            )

        command = TestLabwareIDExists.Command(
            options=[TestLabwareIDExists.Options(LabwareID=venus_labware_id)],
        )

        backend.execute(command)
        backend.wait(command)
        response = backend.acknowledge(command, TestLabwareIDExists.Response)

        if venus_labware_id in response.BadLabwareIDs:
            plh_logger.critical(
                f"HamiltonLayoutItem '{self.identifier}' labware_id is not recognized by the hamilton system. Initialization aborted.",
            )
            raise RuntimeError(
                f"HamiltonLayoutItem '{self.identifier}' labware_id is not recognized by the hamilton system. Initialization aborted.",
            )
