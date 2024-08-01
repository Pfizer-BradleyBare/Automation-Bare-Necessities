from plh_config.admin import config_admin

from .models import CoverablePlate, Lid, Plate, TipRack, VacuumManifold

config_admin.register(Plate)
config_admin.register(CoverablePlate)
config_admin.register(Lid)
config_admin.register(TipRack)
config_admin.register(VacuumManifold)
