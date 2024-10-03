from __future__ import annotations

from typing import Any, cast

import xlwings


def read_solutions(sheet: xlwings.Sheet):

    from solution.models import (
        PredefinedComponent,
        SolutionComponent,
        UserDefinedSolution,
    )

    used_range: list[list[Any]] = cast(list, sheet.used_range.value)[:]

    if len(used_range) < 5:
        return

    used_range = used_range[4:]

    for row_index in range(0, len(used_range), 11):
        for column_index in range(0, len(used_range[row_index]), 6):
            solution_title: str | None = used_range[row_index][column_index]

            if solution_title is None:
                continue

            solution_title = solution_title.replace("\n(Click here to edit)", "")
            storage_condition: str = used_range[row_index + 2][column_index + 4]
            liquid_type: str = used_range[row_index + 3][column_index + 4]
            volatility: str = used_range[row_index + 4][column_index + 4]
            viscosity: str = used_range[row_index + 5][column_index + 4]
            homogeneity: str = used_range[row_index + 6][column_index + 4]

            solution = UserDefinedSolution(
                name=solution_title,
                storage_condition=storage_condition,
                liquid_type=liquid_type,
                volatility=volatility,
                viscosity=viscosity,
                homogeneity=homogeneity,
            )
            solution.clean()
            solution.save()

            for i in range(8):
                name = used_range[row_index + 2 + i][column_index + 0]
                amount = used_range[row_index + 2 + i][column_index + 1]
                unit = used_range[row_index + 2 + i][column_index + 2]

                if name is None or amount is None or unit is None:
                    continue

                query = PredefinedComponent.objects.filter(name=name)

                if query.exists:
                    component =

                query = SolutionComponent.objects.filter(
                    name=name,
                    amount=amount,
                    unit=unit,
                )

                if query.exists():
                    solution.components.add(query.get())
