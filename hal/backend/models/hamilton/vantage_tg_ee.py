from pathlib import Path

from plh.hamilton_venus.backend import (
    VantageTrackGripperEntryExit as PLHVantageTrackGripperEntryExit,
)

from debug import plh_logger

from .hamilton_backend_base import HamiltonBackendBase


class VantageTrackGripperEntryExit(HamiltonBackendBase):
    def initialize(self):
        bound_logger = plh_logger.bind(backend=str(self), type=type(self).__name__)

        bound_logger.info("Starting backend initialization.")

        if self.identifier in self._backend_instances:
            bound_logger.critical(
                "Backend has already been initialized. Initialization will be skipped and running instance will be maintained.",
            )
            return

        plh_backend = PLHVantageTrackGripperEntryExit(
            identifier=self.identifier,
            deck_layout=Path(self.deck_layout),
            simulation_on=self.simulation_on,
        )

        self._backend_instances[self.identifier] = plh_backend

        bound_logger.debug("Starting backend.")

        plh_backend.start()

        bound_logger.info("Completed backend initialization.")

    def deinitialize(self):
        bound_logger = plh_logger.bind(backend=str(self), type=type(self).__name__)

        bound_logger.info("Starting backend deinitialization.")

        if self.identifier not in self._backend_instances:
            bound_logger.critical(
                "Backend is not running. Nothing will occur.",
            )
            return

        plh_backend = self._backend_instances[self.identifier]

        bound_logger.debug("Stopping backend.")
        plh_backend.stop()

        del self._backend_instances[self.identifier]

        bound_logger.info("Completed backend deinitialization.")
