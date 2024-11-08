from hal.admin import hal_admin

from .models.hamilton import MicrolabSTAR, VantageTrackGripperEntryExit
from .models.unchained_labs import Stunner

hal_admin.register(MicrolabSTAR)
hal_admin.register(VantageTrackGripperEntryExit)

hal_admin.register(Stunner)
