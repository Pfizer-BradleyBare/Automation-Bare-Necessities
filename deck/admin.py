from django.contrib import admin

from .models.container import ActivatedContainer, SolutionContainer

# Register your models here.

admin.site.register(SolutionContainer)
admin.site.register(ActivatedContainer)
