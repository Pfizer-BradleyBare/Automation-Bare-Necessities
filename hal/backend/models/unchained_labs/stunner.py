from django.db import models

from .unchained_labs_backend_base import UnchainedLabsBackendBase


class Stunner(UnchainedLabsBackendBase):
    ip_address = models.CharField(max_length=50)
    port = models.SmallIntegerField()
