from django.db import models
from layout_item.models import LayoutItemBase
from polymorphic.models import PolymorphicModel


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

    plates = models.ManyToManyField(to=LayoutItemBase)


class HamiltonHiG4(CentrifugeBase):
    class Meta:
        verbose_name = "Hamilton HiG4"
        verbose_name_plural = "Hamilton HiG4s"

    adapter_id = models.CharField(max_length=10)
