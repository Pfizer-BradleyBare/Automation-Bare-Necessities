from __future__ import annotations

from django.db import models

from method.models import UserMethodWorkbookBase

from .component_base import ComponentBase


class UserDefinedComponent(ComponentBase):
    method = models.ForeignKey(to=UserMethodWorkbookBase, on_delete=models.CASCADE)
