from __future__ import annotations

from django.db import models


class SolutionComponent(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
