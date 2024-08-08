from django.apps import AppConfig
from loguru import logger


class AbnConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "abn"

    def ready(self) -> None:
        import plh
        plh

        logger.enable("plh")
