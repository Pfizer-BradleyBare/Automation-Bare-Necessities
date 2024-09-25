from __future__ import annotations

from django.db import models

from method.models import UserMethodBase

from .solution_base import SolutionBase


class UserDefinedSolution(SolutionBase):
    method = models.ForeignKey(to=UserMethodBase, on_delete=models.CASCADE)
