import sys
from datetime import datetime

from django.apps import AppConfig
from loguru import logger


def logger_callable(info):
    from debug.models import TraceEntry

    message = info["message"]
    time = info["time"]["timestamp"]
    level = info["level"]["name"]

    try:
        source = info["extra"]["source"]
    except KeyError:
        source = "PLH"

    try:
        method = info["extra"]["method"]
    except KeyError:
        method = "None"

    try:
        device = info["extra"]["device"]
    except KeyError:
        device = "None"

    print("HERE")

    TraceEntry(log_source=source,log_level=level,device=device,method=method,message=message,time_stamp=datetime.fromtimestamp(time)).save()


class AbnConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "abn"

    def ready(self) -> None:
        import plh
        plh

        logger.enable("plh")

        logger.remove()
        logger.add(sys.stderr, level="DEBUG")
        logger.add(logger_callable, level="DEBUG", serialize=True)

        return super().ready()
