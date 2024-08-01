from plh_config.admin import config_admin

from .models import (
    HamiltonPortraitCORE8SimpleContentDispense,
    LiquidClass,
    LiquidClassCategory,
    PipetteTip,
)

config_admin.register(LiquidClass)
config_admin.register(LiquidClassCategory)
config_admin.register(PipetteTip)
config_admin.register(HamiltonPortraitCORE8SimpleContentDispense)
# Register your models here.
