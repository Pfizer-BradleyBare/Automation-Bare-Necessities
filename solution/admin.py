from django.contrib import admin

from .models import (
    PredefinedComponent,
    PredefinedSolution,
    SolutionComponent,
    SolutionPropertyPreset,
    UserDefinedComponent,
    UserDefinedSolution,
)

# Register your models here.

admin.site.register(UserDefinedSolution)
admin.site.register(PredefinedSolution)
admin.site.register(SolutionPropertyPreset)
admin.site.register(SolutionComponent)
admin.site.register(PredefinedComponent)
admin.site.register(UserDefinedComponent)
