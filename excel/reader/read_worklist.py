from __future__ import annotations

from typing import Any, cast

import xlwings
from loguru import logger

from method.models import MethodWorkbookBase
from worklist.models import WorklistColumn, WorklistColumnValue


def read_worklist(method: MethodWorkbookBase, sheet: xlwings.Sheet):
    bound_logger = logger.bind(
        source="ABN",
        method=str(method),
    )

    bound_logger.info("Starting read of worklist")

    rows: list[list[Any]] = cast(list, sheet.used_range.value)

    for column_index in range(len(rows[0])):
        column = [row[column_index] for row in rows]

        column_name = column[0]

        if column_name is None:
            continue

        bound_logger.info(f"Column '{column_name}' found")

        worklist_column = WorklistColumn(name=column_name, method=method)
        worklist_column.clean()
        worklist_column.save()

        bound_logger.info("Reading column values")
        column_values = column[1:]

        for row, value in enumerate(column_values):
            bound_logger.debug(f"Reading row '{row+1}' value '{value!s}'")
            worklist_column_value = WorklistColumnValue(
                worklist_column=worklist_column,
                row=row,
                value=value,
            )
            worklist_column_value.clean()
            worklist_column_value.save()

        bound_logger.info("Column values read")

        bound_logger.info("Column read")

    bound_logger.info("Completed read of worklist")
