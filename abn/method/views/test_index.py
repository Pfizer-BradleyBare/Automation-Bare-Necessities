from pathlib import Path

from django.http import HttpRequest
from django.shortcuts import redirect, render

from abn.views import NavbarView


class TestIndexView(NavbarView):
    def get(self, request: HttpRequest):
        return render(
            request,
            "method/test_index.html",
            self.get_context_data(),
        )

    def post(self, request: HttpRequest):
        raw_method_file = request.FILES["input-method-file"]
        method_file_name = Path(raw_method_file.name).stem
        return redirect("method:progress", method_file_name)
