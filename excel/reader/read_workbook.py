from pathlib import Path

import pythoncom
import xlwings


def read_workbook(excel_book_path: Path):
    pythoncom.CoInitialize()

    with xlwings.App(visible=False, add_book=False) as app, app.books.open(
        excel_book_path,
    ) as book:

        try:
            book.app.macro("abn_v3_workbook")()
        except pythoncom.com_error:
            print(
                "Cannot add macros to workbook. Not a valid workbook or macros are not enabled.",
            )
            return
