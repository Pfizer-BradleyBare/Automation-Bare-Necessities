from __future__ import annotations

from django.http import HttpRequest
from django.shortcuts import render

from .navbar import NavbarView


class IndexStatusView(NavbarView):
    def get(self, request: HttpRequest):
        return render(request, "abn/index_status.html", self.get_context_data())
