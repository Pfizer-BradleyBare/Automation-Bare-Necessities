from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path

from django.core.files.storage import FileSystemStorage
from django.db import models
from polymorphic.models import PolymorphicModel


class TemplateMethod(models.Model): ...


class CustomStorage(FileSystemStorage):
    def get_valid_name(self, name: str) -> str:
        """Maintains complete file path created in the DB. No spaces or special characters replaced."""
        return name


def upload_to(instance: UserMethod, filename: str):
    return f"_db_files/{type(instance).__name__.lower().replace('method','_methods')}/{Path(filename).stem}/{datetime.now().strftime('%Y%m%d%H%M%S')}_{filename}"


class UserMethod(PolymorphicModel):
    creation_time = models.DateTimeField(auto_now_add=True, editable=False)
    file = models.FileField(
        upload_to=upload_to,
        storage=CustomStorage,
        max_length=255,
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        stem = Path(Path(self.file.path).name).stem
        return stem[stem.find("_") + 1 :]

    def delete(self, using=None, keep_parents=False) -> tuple[int, dict[str, int]]:
        shutil.rmtree(Path(self.file.path).parent, ignore_errors=True)
        return super().delete(using, keep_parents)


class TestingMethod(UserMethod): ...


class ExecutingMethod(UserMethod):
    state = models.CharField(
        max_length=15,
        choices=(
            ("Reading", "Reading"),
            ("Running", "Running"),
            ("Paused", "Paused"),
            ("Waiting on User", "Waiting on User"),
            ("Complete", "Complete"),
            ("Aborted", "Aborted"),
        ),
        default="Reading",
    )
    emails = models.CharField(max_length=100, blank=False, null=False)
    phone_numbers = models.CharField(max_length=100, blank=True)
    desired_completion_time = models.DateTimeField(blank=False, null=False)
