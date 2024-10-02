from __future__ import annotations

from django.db import models

from method.models import UserMethodWorkbookBase

from .solution_base import SolutionBase


class UserDefinedSolution(SolutionBase):
    method = models.ForeignKey(to=UserMethodWorkbookBase, on_delete=models.CASCADE)
