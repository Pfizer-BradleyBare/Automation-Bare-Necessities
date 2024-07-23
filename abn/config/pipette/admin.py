from django.contrib import admin

from .models import (
    HamiltonPortraitCORE8SimpleContentDispense,
    LiquidClass,
    LiquidClassCategory,
    PipetteTip,
)

admin.site.register(LiquidClass)
admin.site.register(LiquidClassCategory)
admin.site.register(PipetteTip)
admin.site.register(HamiltonPortraitCORE8SimpleContentDispense)
# Register your models here.
