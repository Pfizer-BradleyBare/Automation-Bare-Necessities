from django.contrib import admin

from .models import CoverablePlate, Lid, Plate, TipRack, VacuumManifold

admin.site.register(Plate)
admin.site.register(CoverablePlate)
admin.site.register(Lid)
admin.site.register(TipRack)
admin.site.register(VacuumManifold)
