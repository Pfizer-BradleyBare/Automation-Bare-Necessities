from django.db import models
from polymorphic.models import PolymorphicModel

from plh_config.backend.models import BackendBase
from plh_config.layout_item.models import LayoutItemBase


class TipBase(PolymorphicModel):
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

    tip_volume = models.FloatField()

    tip_racks = models.ManyToManyField(to=LayoutItemBase)

    def __str__(self) -> str:
        return self.identifier


class HamiltonFTR(TipBase):
    class Meta:
        verbose_name = "Hamilton FTR"
        verbose_name_plural = "Hamilton FTRs"


class HamiltonNTR(TipBase):
    class Meta:
        verbose_name = "Hamilton NTR"
        verbose_name_plural = "Hamilton NTRs"

    tip_rack_waste = models.ForeignKey(to=LayoutItemBase, on_delete=models.CASCADE)


class HamiltonEETipStack(models.Model):
    class Meta:
        verbose_name = "Hamilton EE tip stack"
        verbose_name_plural = "Hamilton EE tip stacks"

    tip_rack = models.ForeignKey(to=LayoutItemBase, on_delete=models.CASCADE)
    module_number = models.PositiveSmallIntegerField()
    stack_number = models.PositiveSmallIntegerField()


class HamiltonEETipBase(TipBase):
    tip_stacks = models.ManyToManyField(to=HamiltonEETipStack)
    tip_rack_waste = models.ForeignKey(to=LayoutItemBase, on_delete=models.CASCADE)


class HamiltonEEFTR1000uL(HamiltonEETipBase):
    class Meta:
        verbose_name = "Hamilton EE FTR 1000uL"
        verbose_name_plural = "Hamilton EE FTR 1000uLs"


class HamiltonEENTR(HamiltonEETipBase):
    class Meta:
        verbose_name = "Hamilton EE NTR"
        verbose_name_plural = "Hamilton EE NTRs"
