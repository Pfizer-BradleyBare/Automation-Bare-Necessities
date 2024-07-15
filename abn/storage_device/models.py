from django.db import models
from layout_item.models import LayoutItemBase
from polymorphic.models import PolymorphicModel


class StorageDeviceBase(PolymorphicModel):
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

    layout_items = models.ManyToManyField(to=LayoutItemBase)


class RandomAccessDeckStorage(StorageDeviceBase): ...
