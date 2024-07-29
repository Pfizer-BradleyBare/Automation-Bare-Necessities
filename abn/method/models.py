import shutil
from pathlib import Path

from django.db import models


def get_upload_path(instance, filename):
    return f"_db_files/test_methods/{filename}"


class TestMethod(models.Model):
    filename = models.CharField(max_length=255)
    file = models.FileField(
        upload_to=get_upload_path,
        max_length=255,
        blank=False,
        null=False,
    )
    progress = models.IntegerField(default=0)

    def delete(self, using=None, keep_parents=False) -> tuple[int, dict[str, int]]:
        shutil.rmtree(Path(self.file.path).parent, ignore_errors=True)
        return super().delete(using, keep_parents)

    def __str__(self) -> str:
        return self.filename


class TestMessage(models.Model):
    test_method = models.ForeignKey(to=TestMethod, on_delete=models.CASCADE)
