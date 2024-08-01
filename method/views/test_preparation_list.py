from pathlib import Path

from django.http import FileResponse, HttpRequest

from abn.views import NavbarView


class TestPreparationListView(NavbarView):
    def get(self, request: HttpRequest, filename: str):
        return FileResponse(
            open(
                Path(
                    "C:\\Users\\BAREB\\OneDrive - Pfizer\\Music\\_Template_MethodCreationTool.xlsm",
                ),
                "rb",
            ),
            as_attachment=True,
            filename=f"{Path(filename).stem}_prep_list.xlsm",
        )
