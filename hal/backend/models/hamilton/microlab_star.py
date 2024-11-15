from pathlib import Path

from plh.hamilton_venus.backend import MicrolabSTAR as PLHMicrolabSTAR

from debug import plh_logger

from .hamilton_backend_base import HamiltonBackendBase


class MicrolabSTAR(HamiltonBackendBase):
    def initialize(self):
        if self.identifier in self._backend_instances:
            plh_logger.critical(
                f"Backend '{self.identifier}' has already been initialized. Initialization will be skipped and running instance will be maintained.",
            )
            return

        plh_backend = PLHMicrolabSTAR(
            identifier=self.identifier,
            deck_layout=Path(self.deck_layout),
            simulation_on=self.simulation_on,
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
