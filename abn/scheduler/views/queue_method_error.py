from django.http import HttpRequest
from django.shortcuts import render

from abn.views import NavbarView


class QueueMethodErrorView(NavbarView):
    def get(self, request: HttpRequest):
        return render(
            request,
            "scheduler/queue_method_error.html",
            self.get_context_data(),
        )
