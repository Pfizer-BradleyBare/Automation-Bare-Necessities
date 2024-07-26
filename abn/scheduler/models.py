import shutil
from datetime import datetime
from pathlib import Path

from django.db import models


def get_upload_path(instance, filename):
    return f"_db_files/queued_methods/{filename[:-5]}/{datetime.now().strftime('%Y%m%d%H%M%S')}_{filename}"


class QueuedMethod(models.Model):
    filename = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False,
    )
    creation_time = models.DateTimeField(auto_now_add=True, editable=False)
    emails = models.CharField(max_length=100, blank=False, null=False)
    phone_numbers = models.CharField(max_length=100, blank=True)
    completion_time = models.DateTimeField(blank=False, null=False)
    file = models.FileField(
        upload_to=get_upload_path,
        max_length=255,
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        return self.filename

    def delete(self, using=None, keep_parents=False) -> tuple[int, dict[str, int]]:
        shutil.rmtree(Path(self.file.path).parent, ignore_errors=True)
        return super().delete(using, keep_parents)
