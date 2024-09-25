from django.contrib import admin

from .models import PredefinedSolution, SolutionComponent, UserDefinedSolution

# Register your models here.

admin.site.register(SolutionComponent)
admin.site.register(UserDefinedSolution)
admin.site.register(PredefinedSolution)
