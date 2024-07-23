import pandas as pd
import plotly.express as px
from django.http.request import HttpRequest
from django.shortcuts import render


def gantt_chart(request: HttpRequest):
    df = pd.DataFrame(
        [
            dict(
                Task="Job A",
                Start="2009-01-01",
                Finish="2009-02-28",
                Resource="Alex",
            ),
            dict(
                Task="Job B",
                Start="2009-03-05",
                Finish="2009-04-15",
                Resource="Alex",
            ),
            dict(Task="Job C", Start="2009-02-20", Finish="2009-05-30", Resource="Max"),
        ],
    )

    try:
        fig = px.timeline(
            df,
            x_start="Start",
            x_end="Finish",
            y="Task",
            color="Resource",
        )

        context = {
            "gantt_chart_html": fig.to_html(
                full_html=False,
                default_height=900,
            ),
        }
    except ValueError:
        context = {}
    if request.method == "POST":
        return render(request, "scheduler/gantt_chart_figure.html", context)
    else:
        return render(request, "scheduler/gantt_chart.html", context)
