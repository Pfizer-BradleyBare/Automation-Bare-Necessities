from django.contrib import admin

from .models import MethodStart
from .models.pathways import ActivateContainer, Merge, SplitWorklist

admin.site.register(MethodStart)
admin.site.register(ActivateContainer)
admin.site.register(SplitWorklist)
admin.site.register(Merge)
