from pathlib import Path

from django.http import HttpRequest
from django.shortcuts import redirect, render

from abn.views import NavbarView
from method.models import UserMethod


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

        query = UserMethod.objects.filter(filename=method_file_name)
        if query.exists():
            test_method = query.get()
            test_method.delete()

        UserMethod(filename=method_file_name, file=raw_method_file).save()

        return redirect("method:progress", method_file_name)
