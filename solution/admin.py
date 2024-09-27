from django.contrib import admin

from .models import PredefinedSolution, SolutionPropertyPreset, UserDefinedSolution

# Register your models here.

admin.site.register(UserDefinedSolution)
admin.site.register(PredefinedSolution)
admin.site.register(SolutionPropertyPreset)
