from django.db import models


class QueuedMethod(models.Model):
    name = models.CharField(max_length=10)
