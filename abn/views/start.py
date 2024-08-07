from __future__ import annotations

from django.http import HttpRequest
from django.shortcuts import redirect

import abn
from plh_config.load_config import load_config

from .navbar import NavbarView


class StartView(NavbarView):
    def get(self, request: HttpRequest):

        load_config()

        abn.state = "run"
        return redirect("abn:index_status")
