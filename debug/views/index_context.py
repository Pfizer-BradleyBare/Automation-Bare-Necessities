from django.utils import timezone

from abn.views import NavbarView
from debug.models import LogLevelOptions, LogSourceOptions, Trace


class IndexContextView(NavbarView):

    def get_context_data(self, **kwargs) -> dict:

        num_objects = 500

        kwargs.setdefault("log_source", "ALL")
        kwargs.setdefault("log_level", "ALL")
        kwargs.setdefault("meta_info", "")
        kwargs.setdefault("debug_message", "")

        log_source = str(kwargs.get("log_source"))
        log_level = str(kwargs.get("log_level"))
        meta_info = kwargs.get("meta_info")
        debug_message = kwargs.get("debug_message")

        query = Trace.objects

        if log_source != "ALL":
            query = query.filter(log_source=LogSourceOptions[log_source])
        if log_level != "ALL":
            query = query.filter(log_level__gte=LogLevelOptions[log_level])
        if meta_info != "":
            for meta_info in str(meta_info).split(","):
                query = query.filter(meta_info__icontains=meta_info.strip())
        if debug_message != "":
            for debug_message in str(debug_message).split(","):
                query = query.filter(message__icontains=debug_message.strip())

        objects = query.all()[:num_objects]

        context = {
            "rows": [
                [
                    object.time_stamp.astimezone(
                        timezone.get_current_timezone(),
                    ).strftime("%b %d, %Y, %I:%M %p"),
                    LogSourceOptions(object.log_source).label.upper(),
                    LogLevelOptions(object.log_level).label.upper(),
                    object.meta_info,
                    object.message,
                ]
                for object in objects
            ],
        }

        return super().get_context_data(**kwargs) | context
