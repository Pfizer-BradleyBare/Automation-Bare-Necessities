from django.http import HttpRequest
from django.shortcuts import render

from method.models import ExecutingMethod

from .queue_method_dashboard_context import QueueMethodDashboardContextView


class QueueMethodDashboardPauseView(QueueMethodDashboardContextView):
    def get(self, request: HttpRequest, filename: str):

        queued_method = ExecutingMethod.objects.get(file__icontains=filename)
        if queued_method.state == "Running":
            queued_method.state = "Paused"

        queued_method.save()

        return render(
            request,
            "scheduler/queue_method_dashboard_body.html",
            self.get_context_data(filename=filename),
        )
