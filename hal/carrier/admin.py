from hal.admin import hal_admin

from .models import MoveableCarrier, StationaryCarrier, hamilton

hal_admin.register(StationaryCarrier)
hal_admin.register(MoveableCarrier)
hal_admin.register(hamilton.HamiltonAutoloadCarrier)
