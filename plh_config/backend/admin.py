from plh_config.admin import config_admin

from .models import MicrolabSTAR, Stunner, VantageTrackGripperEntryExit

config_admin.register(MicrolabSTAR)
config_admin.register(VantageTrackGripperEntryExit)
config_admin.register(Stunner)
