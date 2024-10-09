from datetime import datetime
from pathlib import Path
from shutil import copy

from django.conf import settings
from django.http import HttpRequest
from django.http.response import FileResponse

from abn.views import NavbarView
from excel.definitions import write_definitions


class TemplatesBlankView(NavbarView):
    def get(self, request: HttpRequest):
        method_path = Path(settings.BASE_DIR) / "method_template.xlsm"

        temp_method_path = (
            Path(settings.BASE_DIR)
            / "_temp"
            / f"{datetime.now().strftime('%Y%m%d%H%M%S')}_method_template.xlsm"
        )

        (Path(settings.BASE_DIR) / "_temp").mkdir(exist_ok=True)

        copy(method_path, temp_method_path)

        write_definitions(temp_method_path)

        return FileResponse(
            open(
                temp_method_path,
                "rb",
            ),
            as_attachment=True,
            filename="RENAME_ME_Blank_Template.xlsm",
        )
