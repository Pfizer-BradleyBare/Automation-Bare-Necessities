from django.db import models

from ..block_base import BlockBase


class SplitWorklist(BlockBase):
    left_container_name = models.CharField(max_length=255)
    left_container_type = models.CharField(max_length=255, default="")

    right_container_name = models.CharField(max_length=255)
    right_container_type = models.CharField(max_length=255, default="")

    container_choice = models.CharField(max_length=255)
