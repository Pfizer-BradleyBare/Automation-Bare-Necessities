from pathlib import Path

import pythoncom
import xlwings

from .block_definitions import write_block_definitions_sheet
from .solution_definitions import (
    write_solution_components_sheet,
    write_solution_definitions_sheet,
)
from .solution_property_presets import write_solution_property_presets_sheet


def write_definitions(excel_book_path: Path):

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

        write_solution_property_presets_sheet(
            book.sheets["__SolutionPropertyPresets"],
        )

        write_solution_components_sheet(book.sheets["__SolutionComponents"])

        write_solution_definitions_sheet(book.sheets["__SolutionDefinitions"])

        write_block_definitions_sheet(book.sheets["__BlockDefinitions"])

        book.save()
