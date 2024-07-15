from backend.models import BackendBase
from django.db import models
from layout_item.models import LayoutItemBase
from polymorphic.models import PolymorphicModel


class HeatCoolShakeBase(PolymorphicModel):
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


class HamiltonHeaterShaker(HeatCoolShakeBase):
    com_port = models.PositiveSmallIntegerField()


class HamiltonHeaterCooler(HeatCoolShakeBase):
    com_port = models.CharField(max_length=10)
