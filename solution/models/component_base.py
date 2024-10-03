from __future__ import annotations

from django.db import models
from polymorphic.models import PolymorphicModel


class ComponentBase(PolymorphicModel):
    """Used as a way to get all solutions and components to show up as a foreign key for SolutionComponent ONLY.
    Because ease of use for users is imperative.
    """

    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name
