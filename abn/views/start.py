from __future__ import annotations

import pathlib

from django.conf import settings
from django.core.files import File
from django.http import HttpRequest
from django.shortcuts import redirect
from loguru import logger

import abn
from excel.reader import read_workbook
from plh_config.load_config import load_config

from .navbar import NavbarView


class StartView(NavbarView):
    def get(self, request: HttpRequest):

        from method.models import TestingMethodWorkbook

        method = TestingMethodWorkbook(
            file=File(
                (pathlib.Path(settings.BASE_DIR) / "method_template.xlsm").open(
                    "rb",
                ),
            ),
        )

        method.clean()
        method.save()

        read_workbook(method)

        return redirect("abn:index_status")

        abn.state = "start"

        logger = logger.bind(source="ABN")
        logger = logger.bind(test="Hello this is a test")
        logger = logger.bind(test1="This is another test")
        logger.info("Starting ABN")

        load_config()

        abn.state = "run"
        return redirect("abn:index_status")
