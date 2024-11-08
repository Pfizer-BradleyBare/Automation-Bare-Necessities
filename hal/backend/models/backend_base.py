from django.db import models
from polymorphic.models import PolymorphicModel


class BackendBase(PolymorphicModel):
    class Meta:
        ordering = ["identifier"]

    identifier = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        return self.identifier
