from __future__ import annotations

import shutil
import threading
from datetime import datetime
from pathlib import Path

from django.core.files.storage import FileSystemStorage
from django.db import models
from loguru import logger
from polymorphic.models import PolymorphicModel


class CustomStorage(FileSystemStorage):
    def get_valid_name(self, name: str) -> str:
        """Maintains complete file path created in the DB. No spaces or special characters replaced."""
        return name


def upload_to(instance: MethodWorkbookBase, filename: str):
    stem = Path(filename).stem
    return f"_db_files/{type(instance).__name__.lower().replace('methodworkbook','_method_workbooks')}/{stem}/{datetime.now().strftime('%Y%m%d%H%M%S')}_ANCHOR_{stem}.xlsm"


class MethodWorkbookBase(PolymorphicModel):
    creation_time = models.DateTimeField(auto_now_add=True, editable=False)
    file = models.FileField(
        upload_to=upload_to,
        storage=CustomStorage,
        max_length=255,
        blank=False,
        null=False,
    )

    is_valid = models.BooleanField(editable=False, default=False)

    solutions_read_checkpoint = models.BooleanField(editable=False, default=False)
    worklist_read_checkpoint = models.BooleanField(editable=False, default=False)
    method_read_checkpoint = models.BooleanField(editable=False, default=False)
    method_validated_checkpoint = models.BooleanField(editable=False, default=False)
    containers_created_checkpoint = models.BooleanField(editable=False, default=False)
    containers_pipetted_checkpoint = models.BooleanField(editable=False, default=False)
    assign_labware_checkpoint = models.BooleanField(editable=False, default=False)
    devices_possible_checkpoint = models.BooleanField(editable=False, default=False)

    def validate_method(self):
        from block.models import BlockBase
        from block.models.meta_data import (
            Author,
            Category,
            DocumentNumber,
            MethodName,
            ValidModality,
            ValidProjectCode,
        )

        bound_logger = logger.bind(method=str(self))

        bound_logger.info("Starting method validation")

        if (
            not BlockBase.objects.filter(method=self, is_valid=False).exists()
            and Author.objects.filter(method=self).exists()
            and Category.objects.filter(method=self).exists()
            and DocumentNumber.objects.filter(method=self).exists()
            and MethodName.objects.filter(method=self).exists()
            and ValidModality.objects.filter(method=self).exists()
            and ValidProjectCode.objects.filter(method=self).exists()
        ):
            self.is_valid = True

        bound_logger.info("Completed method validation")

    def __str__(self) -> str:
        stem = Path(Path(self.file.path).name).stem
        return stem[stem.find("_ANCHOR_") + 8 :]

    def delete(self, using=None, keep_parents=False) -> tuple[int, dict[str, int]]:
        shutil.rmtree(Path(self.file.path).parent, ignore_errors=True)
        return super().delete(using, keep_parents)

    def save(self, *args, **kwargs):
        from excel.reader import read_workbook

        if not self.pk:
            super().save(*args, **kwargs)
            thread = threading.Thread(target=read_workbook, args=(self,), daemon=True)
            thread.start()
        else:
            super().save(*args, **kwargs)
