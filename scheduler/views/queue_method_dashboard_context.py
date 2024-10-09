from django.utils import timezone

from abn.views import NavbarView
from method.models import ExecutingMethodWorkbook


class QueueMethodDashboardContextView(NavbarView):
    def get_context_data(self, **kwargs) -> dict:
        filename = kwargs.get("filename")

        queued_method = ExecutingMethodWorkbook.objects.get(file__icontains=filename)

        context = {
            "state": queued_method.state.lower(),
            "filename": str(queued_method),
            "progress": 50,
            "start_time": "10 days 24 hours 25 minutes",
            "time_remaining": "10 days 24 hours 25 minutes",
            "notifications_pending": False,
            "deck_loading_pending": True,
            "emails": queued_method.emails,
            "phone_numbers": queued_method.phone_numbers,
            "completion_time": queued_method.desired_completion_time.astimezone(
                timezone.get_current_timezone(),
            ).strftime(
                "%Y-%m-%dT%H:%M",
            ),
        }

        return super().get_context_data(**kwargs) | context
