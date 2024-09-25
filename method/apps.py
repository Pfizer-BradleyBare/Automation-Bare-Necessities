import shutil
from pathlib import Path

from django.apps import AppConfig
from django.conf import settings


class MethodConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "method"

    def ready(self) -> None:
        path = Path(settings.BASE_DIR) / "_abn_methods"

        shutil.rmtree(path, ignore_errors=True)
