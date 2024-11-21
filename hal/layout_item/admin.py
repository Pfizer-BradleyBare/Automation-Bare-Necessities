from django.contrib import admin

from hal.admin import hal_admin

from .models import LoadedLayoutItem
from .models.hamilton import HamiltonLayoutItem

admin.site.register(LoadedLayoutItem)
hal_admin.register(HamiltonLayoutItem)
