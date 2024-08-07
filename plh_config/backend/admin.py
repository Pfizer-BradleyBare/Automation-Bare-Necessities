from plh_config.admin import config_admin

from .models import MicrolabStar, Stunner, VantageTrackGripperEntryExit

config_admin.register(MicrolabStar)
config_admin.register(VantageTrackGripperEntryExit)
config_admin.register(Stunner)
