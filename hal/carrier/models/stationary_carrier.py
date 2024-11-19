from debug import plh_logger

from .carrier_base import CarrierBase


class StationaryCarrier(CarrierBase):
    def initialize(self):
        bound_logger = plh_logger.bind(carrier=str(self), type=type(self).__name__)

        bound_logger.info("Starting carrier initialization.")
        bound_logger.info("Completed carrier initialization.")

    def deinitialize(self):
        bound_logger = plh_logger.bind(carrier=str(self), type=type(self).__name__)

        bound_logger.info("Starting carrier deinitialization.")
        bound_logger.info("Completed carrier deinitialization.")
