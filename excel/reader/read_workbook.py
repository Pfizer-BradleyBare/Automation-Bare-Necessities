import pythoncom
import xlwings

from method.models import MethodWorkbookBase

from .read_method import read_method
from .read_solutions import read_solutions
from .read_worklist import read_worklist


def read_workbook(method: MethodWorkbookBase):
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

        read_method(method, book.sheets["Method"])
        read_solutions(method, book.sheets["Solutions"])
        read_worklist(method, book.sheets["Worklist"])
