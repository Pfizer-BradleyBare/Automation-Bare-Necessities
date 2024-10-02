import pythoncom
import xlwings

from method.models import UserMethodWorkbookBase


def read_workbook(method: UserMethodWorkbookBase):
    pythoncom.CoInitialize()

    with xlwings.App(visible=False, add_book=False) as app, app.books.open(
        method.file.path,
    ) as book:

        try:
            book.app.macro("abn_v3_workbook")()
        except pythoncom.com_error:
            print(
                "Cannot run ABN validation macro. Not a valid workbook or macros are not enabled.",
            )
            return
