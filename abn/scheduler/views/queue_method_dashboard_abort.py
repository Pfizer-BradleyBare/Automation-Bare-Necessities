from django.http import HttpRequest
from django.shortcuts import render

from .queue_method_dashboard_context import QueueMethodDashboardContextView


class QueueMethodDashboardAbortView(QueueMethodDashboardContextView):
    def get(self, request: HttpRequest, filename: str):

        return render(
            request,
            "scheduler/queue_method_dashboard_abort.html",
            self.get_context_data(filename=filename),
        )
