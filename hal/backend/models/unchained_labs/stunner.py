from django.db import models
from plh.UnchainedLabs_Instruments.backend import Stunner as PLHStunner

from debug import plh_logger

from .unchained_labs_backend_base import UnchainedLabsBackendBase


class Stunner(UnchainedLabsBackendBase):
    ip_address = models.CharField(max_length=50)
    port = models.SmallIntegerField()

    def initialize(self):
        if self.identifier in self._backend_instances:
            plh_logger.critical(
                f"Backend '{self.identifier}' has already been initialized. Initialization will be skipped and running instance will be maintained.",
            )
            return

        plh_backend = PLHStunner(
            identifier=self.identifier,
            ip_address=self.ip_address,
            port=self.port,
        )

        self._backend_instances[self.identifier] = plh_backend

        plh_backend.start()

    def deinitialize(self):
        if self.identifier not in self._backend_instances:
            plh_logger.critical(
                f"Backend '{self.identifier}' has not yet been initialized. Nothing will occur.",
            )
            return

        plh_backend = self._backend_instances[self.identifier]

        plh_backend.stop()
