from __future__ import annotations

import pathlib

import pythoncom
import xlwings
from django.conf import settings
from django.core.files import File
from django.http import HttpRequest
from django.shortcuts import redirect
from loguru import logger

import abn
from excel.reader.read_method import read_method
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

        pythoncom.CoInitialize()

        with xlwings.App(visible=False, add_book=False) as app, app.books.open(
            method.file.path,
        ) as book:

            read_method(method, book.sheets["Method"])

        return redirect("abn:index_status")

        abn.state = "start"

        logger = logger.bind(source="ABN")
        logger = logger.bind(test="Hello this is a test")
        logger = logger.bind(test1="This is another test")
        logger.info("Starting ABN")

        load_config()

        abn.state = "run"
        return redirect("abn:index_status")
