from django.db import models

from abn.scheduler.models import QueuedMethod


class TraceEntry(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True)
    log_source = models.CharField(
        max_length=3,
        choices=(
            ("PLH", "PLH"),
            ("ABN", "ABN"),
        ),
    )
    log_level = models.CharField(
        max_length=10,
        choices=(
            ("DEBUG", "DEBUG"),
            ("INFO", "INFO"),
            ("WARNING", "WARNING"),
            ("CRITICAL", "CRITICAL"),
            ("ERROR", "ERROR"),
        ),
    )
    device_identifier = models.CharField(max_length=100)
    method = models.ForeignKey(to=QueuedMethod, on_delete=models.CASCADE)
    message = models.TextField()

    class Meta:
        ordering = ["time_stamp"]

    def __str__(self) -> str:
        return self.message
