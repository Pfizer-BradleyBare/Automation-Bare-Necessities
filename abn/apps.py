import sys
from datetime import datetime
from typing import cast

from django.apps import AppConfig
from django.utils import timezone
from loguru import logger


def logger_callable(info):
    from debug.models import LogLevelOptions, LogSourceOptions, Trace

    record = info.record

    message = record["message"]
    time = cast(datetime, record["time"]).astimezone(timezone.get_current_timezone())
    level = record["level"].name

    extra = record["extra"]

    try:
        source = extra["source"]
        del extra["source"]
    except KeyError:
        source = "PLH"

    meta_info = ", ".join(extra.values())

    Trace(
        log_source=LogSourceOptions[source],
        log_level=LogLevelOptions[level],
        meta_info=meta_info,
        message=message,
        time_stamp=time,
    ).save()


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
