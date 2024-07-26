from django.http import HttpRequest
from django.shortcuts import render

from abn.views import NavbarView


class QueueMethodDashboardView(NavbarView):
    def get(self, request: HttpRequest, filename: str):
        return render(
            request,
            "scheduler/queue_method_dashboard.html",
            self.get_context_data()
            | {
                "state": "running",
                "deck_loading": [1],
                "notifications": [1],
                "filename": filename,
                "progress": 50,
                "time_remaining": "10 days 24 hours 25 minutes",
            },
        )
