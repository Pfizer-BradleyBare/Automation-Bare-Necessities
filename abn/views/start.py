from __future__ import annotations

from django.http import HttpRequest
from django.shortcuts import redirect
from loguru import logger

import abn
from plh_config.load_config import load_config

from .navbar import NavbarView


class StartView(NavbarView):
    def get(self, request: HttpRequest):

        abn.state = "start"

        logger.info("Starting ABN")

        load_config()

        abn.state = "run"
        return redirect("abn:index_status")
