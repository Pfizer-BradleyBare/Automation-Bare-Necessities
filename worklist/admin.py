from django.contrib import admin

from .models import WorklistColumn, WorklistColumnValue

admin.site.register(WorklistColumn)
admin.site.register(WorklistColumnValue)
