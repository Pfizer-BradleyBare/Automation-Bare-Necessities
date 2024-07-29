from django.http import HttpRequest
from django.shortcuts import render

from abn.views import NavbarView


class QueueMethodDashboardEditView(NavbarView):
    def get(self, request: HttpRequest, filename: str):

        return render(
            request,
            "scheduler/queue_method_dashboard_edit.html",
            self.get_context_data(),
        )
