from __future__ import annotations

from django.http import HttpRequest
from django.shortcuts import redirect

import abn

from .navbar import NavbarView


class StopView(NavbarView):
    def get(self, request: HttpRequest):
        abn.state = False
        return redirect("abn:index")
