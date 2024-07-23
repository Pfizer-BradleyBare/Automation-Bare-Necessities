from abn_config.admin import config_admin

from .models import HamiltonMicrolabStar, HamiltonTrackGripperEntryExitVantage, Stunner

config_admin.register(HamiltonMicrolabStar)
config_admin.register(HamiltonTrackGripperEntryExitVantage)
config_admin.register(Stunner)
