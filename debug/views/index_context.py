from abn.views import NavbarView
from debug.models import LogLevelOptions, LogSourceOptions, TraceEntry


class IndexContextView(NavbarView):

    def get_context_data(self, **kwargs) -> dict:

        num_objects = 500

        kwargs.setdefault("log_source", "ALL")
        kwargs.setdefault("log_level", "ALL")
        kwargs.setdefault("method_name", "")
        kwargs.setdefault("device_identifier", "")
        kwargs.setdefault("debug_message", "")

        log_source = str(kwargs.get("log_source"))
        log_level = str(kwargs.get("log_level"))
        method_name = kwargs.get("method_name")
        device_identifier = kwargs.get("device_identifier")
        debug_message = kwargs.get("debug_message")

        query = TraceEntry.objects

        if log_source != "ALL":
            query = query.filter(log_source=LogSourceOptions[log_source])
        if log_level != "ALL":
            query = query.filter(log_level__gte=LogLevelOptions[log_level])
        if method_name != "":
            query = query.filter(method__file__icontains=method_name)
        if device_identifier != "":
            query = query.filter(device_identifier__icontains=device_identifier)
        if debug_message != "":
            query = query.filter(message__icontains=debug_message)

        objects = query.all()[:num_objects]

        context = {
            "rows": sorted(
                [
                    [
                        object.time_stamp.strftime("%b %d, %Y, %I:%M %p"),
                        LogSourceOptions(object.log_source).label.upper(),
                        LogLevelOptions(object.log_level).label.upper(),
                        str(object.method),
                        object.device_identifier,
                        object.message,
                    ]
                    for object in objects
                ],
                key=lambda x: x[0],
            ),
        }

        return super().get_context_data(**kwargs) | context
