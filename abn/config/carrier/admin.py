from config.admin import config_admin

from .models import HamiltonAutoloadCarrier, MoveableCarrier, NonMoveableCarrier

config_admin.register(NonMoveableCarrier)
config_admin.register(MoveableCarrier)
config_admin.register(HamiltonAutoloadCarrier)
