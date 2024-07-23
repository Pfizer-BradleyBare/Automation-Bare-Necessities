from django.contrib import admin

from .models import HamiltonSTARAutoload, HamiltonVantageAutoload

admin.site.register(HamiltonSTARAutoload)
admin.site.register(HamiltonVantageAutoload)
