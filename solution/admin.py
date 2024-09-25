from django.contrib import admin

from .models import PredefinedSolution, UserDefinedSolution

# Register your models here.

admin.site.register(UserDefinedSolution)
admin.site.register(PredefinedSolution)
