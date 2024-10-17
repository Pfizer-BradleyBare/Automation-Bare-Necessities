from django.contrib import admin

from .models import MethodStart
from .models.comments import OverviewComment, RuntimeComment, SilentComment
from .models.heat_cool_shake import Incubate, IncubateAndShake, Rest, Shake
from .models.liquid_handling import Dilute, Pipette
from .models.meta_data import Author, Category, DocumentNumber, Modality, Project
from .models.pathways import ActivateContainer, Merge, SplitWorklist
from .models.uv_flr import MeasureConcentration

admin.site.register(MethodStart)
admin.site.register(ActivateContainer)
admin.site.register(SplitWorklist)
admin.site.register(Merge)

admin.site.register(SilentComment)
admin.site.register(RuntimeComment)
admin.site.register(OverviewComment)


admin.site.register(Author)
admin.site.register(Modality)
admin.site.register(Category)
admin.site.register(DocumentNumber)
admin.site.register(Project)

admin.site.register(Pipette)
admin.site.register(Dilute)

admin.site.register(Incubate)
admin.site.register(Shake)
admin.site.register(IncubateAndShake)
admin.site.register(Rest)

admin.site.register(MeasureConcentration)
