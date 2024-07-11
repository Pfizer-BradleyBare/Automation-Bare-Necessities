from django.contrib import admin

from .models import NonPipettableLabware, PipettableLabware

admin.site.register(NonPipettableLabware)
admin.site.register(PipettableLabware)
