from datetime import datetime
from typing import cast

from django.utils import timezone

from .models import LogLevelOptions, LogSourceOptions, Trace


def loguru_sink_callable(info):
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

    meta_info = ", ".join([f"{key}={value}" for key, value in extra.items()])

    Trace(
        log_source=LogSourceOptions[source],
        log_level=LogLevelOptions[level],
        meta_info=meta_info,
        message=message,
        time_stamp=time,
    ).save()
