from django.contrib import admin

from .models import MethodStart
from .models.comments import OverviewComment, RuntimeComment, SilentComment
from .models.constraints import (
    ConcentrationMax,
    ConcentrationMin,
    SampleNumberMax,
    SampleNumberMin,
)
from .models.meta_data import Author, Category, INXNumber, Modality, Scale
from .models.pathways import ActivateContainer, Merge, SplitWorklist

admin.site.register(MethodStart)
admin.site.register(ActivateContainer)
admin.site.register(SplitWorklist)
admin.site.register(Merge)

admin.site.register(SilentComment)
admin.site.register(RuntimeComment)
admin.site.register(OverviewComment)

admin.site.register(SampleNumberMax)
admin.site.register(SampleNumberMin)
admin.site.register(ConcentrationMax)
admin.site.register(ConcentrationMin)

admin.site.register(Author)
admin.site.register(Modality)
admin.site.register(Category)
admin.site.register(INXNumber)
admin.site.register(Scale)
