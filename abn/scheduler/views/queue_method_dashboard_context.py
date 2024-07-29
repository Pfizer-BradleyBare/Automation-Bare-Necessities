from django.utils import timezone

from abn.views import NavbarView
from scheduler.models import QueuedMethod


class QueueMethodDashboardContextView(NavbarView):
    def get_context_data(self, **kwargs) -> dict:
        filename = kwargs.get("filename")

        queued_method = QueuedMethod.objects.get(filename=filename)

        context = {
            "state": queued_method.state.lower(),
            "filename": queued_method.filename,
            "progress": 0,
            "start_time": "10 days 24 hours 25 minutes",
            "time_remaining": "10 days 24 hours 25 minutes",
            "emails": queued_method.emails,
            "phone_numbers": queued_method.phone_numbers,
            "completion_time": queued_method.completion_time.astimezone(
                timezone.get_current_timezone(),
            ).strftime(
                "%Y-%m-%dT%H:%M",
            ),
        }

        return super().get_context_data(**kwargs) | context
