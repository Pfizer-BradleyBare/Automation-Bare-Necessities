from abn.views import NavbarView
from debug.models import LogLevelOptions, Trace

from ..models import TestingMethodWorkbook


class TestProgressContextView(NavbarView):
    def get_context_data(self, **kwargs) -> dict:
        context = {}
        filename = kwargs.get("filename")
        context["filename"] = filename

        query = TestingMethodWorkbook.objects.filter(
            file__icontains=f"_ANCHOR_{filename}",
        )

        if not query.exists():
            context["method_found"] = False
            return super().get_context_data() | context

        context["method_found"] = True

        method = query.get()

        context["is_valid"] = method.is_valid

        progress_items = [
            method.solutions_read_checkpoint,
            method.worklist_read_checkpoint,
            method.method_read_checkpoint,
        ]
        progress = int(sum(progress_items) / len(progress_items) * 100)

        context["progress"] = progress

        query = Trace.objects.filter(
            meta_info__icontains=f"method={filename}",
            time_stamp__gte=method.creation_time,
        )

        if progress < 100:
            query = query.filter(log_level__gte=LogLevelOptions.INFO)
        else:
            query = query.filter(log_level__gte=LogLevelOptions.CRITICAL)

        context["rows"] = query.all()

        return super().get_context_data() | context
