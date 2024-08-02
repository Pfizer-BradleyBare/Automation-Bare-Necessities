from __future__ import annotations

from django.http import HttpRequest
from django.shortcuts import redirect, render

import abn

from .navbar import NavbarView


class StopView(NavbarView):
    def get(self, request: HttpRequest):
        return render(request, "abn/stop.html", self.get_context_data())

    def post(self, request: HttpRequest):
        abn.state = "stop"
        return redirect("abn:index")
