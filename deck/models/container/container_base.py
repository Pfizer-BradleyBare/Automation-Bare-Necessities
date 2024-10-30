from django.db import models
from polymorphic.models import PolymorphicModel

from method.models import MethodWorkbookBase


class ContainerBase(PolymorphicModel):
    method = models.ForeignKey(to=MethodWorkbookBase, on_delete=models.CASCADE)
    computed_required_volume = models.FloatField()
