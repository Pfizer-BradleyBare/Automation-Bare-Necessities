from django.db import models

from ..block_base import BlockBase


class Merge(BlockBase):
    block_name = "Merge"
    block_category = "Pathways"

    container_name = models.CharField(max_length=255)
    container_type = models.CharField(max_length=255, default="")
