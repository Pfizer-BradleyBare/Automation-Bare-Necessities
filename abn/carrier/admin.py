from django.contrib import admin

from .models import HamiltonAutoloadCarrier, MoveableCarrier, NonMoveableCarrier

admin.site.register(NonMoveableCarrier)
admin.site.register(MoveableCarrier)
admin.site.register(HamiltonAutoloadCarrier)
