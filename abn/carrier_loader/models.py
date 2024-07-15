from carrier.models import CarrierBase
from django.db import models
from polymorphic.models import PolymorphicModel


class CarrierLoaderBase(PolymorphicModel):
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

    supported_carriers = models.ManyToManyField(to=CarrierBase)


class HamiltonSTARAutoload(CarrierLoaderBase): ...


class HamiltonVantageAutoload(CarrierLoaderBase): ...
