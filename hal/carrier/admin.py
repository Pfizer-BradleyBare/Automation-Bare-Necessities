from hal.admin import hal_admin

from .models import HamiltonAutoloadCarrier, MoveableCarrier, StationaryCarrier

hal_admin.register(StationaryCarrier)
hal_admin.register(MoveableCarrier)
hal_admin.register(HamiltonAutoloadCarrier)
