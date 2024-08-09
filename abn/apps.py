import sys

from django.apps import AppConfig


class AbnConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "abn"

    def ready(self) -> None:
        import plh
        from loguru import logger

        from debug.loguru_sink import loguru_sink_callable

        # Import here because technically should not happen until django is fully loaded.

        logger.enable(plh.__name__)

        logger.remove()
        logger.add(sys.stderr, level="DEBUG")
        logger.add(loguru_sink_callable, level="DEBUG", serialize=True)

        return super().ready()
