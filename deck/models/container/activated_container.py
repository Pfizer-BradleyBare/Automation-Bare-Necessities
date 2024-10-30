from django.db import models

from .container_base import ContainerBase


class ActivatedContainer(ContainerBase):
    name = models.CharField(max_length=250)
