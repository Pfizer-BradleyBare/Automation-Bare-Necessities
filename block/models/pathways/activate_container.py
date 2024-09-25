from django.db import models

from ..block_base import BlockBase


class ActivateContainer(BlockBase):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, default="")