from django.db import models
from polymorphic.models import PolymorphicModel

from config.backend.models import BackendBase
from config.layout_item.models import LayoutItemBase


class CentrifugeBase(PolymorphicModel):
    class Meta:
        ordering = ["identifier"]

    identifier = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        blank=False,
        null=False,
    )

    enabled = models.BooleanField(default=True)

    backend = models.ForeignKey(to=BackendBase, on_delete=models.CASCADE)

    plates = models.ManyToManyField(to=LayoutItemBase)


class HamiltonHiG4(CentrifugeBase):
    class Meta:
        verbose_name = "Hamilton HiG4"
        verbose_name_plural = "Hamilton HiG4s"

    adapter_id = models.CharField(max_length=10)
