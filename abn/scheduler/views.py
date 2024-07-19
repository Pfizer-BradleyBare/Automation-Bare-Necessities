import pandas as pd
import plotly.express as px
from django.http.request import HttpRequest
from django.shortcuts import redirect, render


def test_method(request: HttpRequest):
    return render(request, "scheduler/test_method.html", {})


def method_queue(request: HttpRequest):
    return render(request, "scheduler/method_queue.html", {})


def queue_method_success(request: HttpRequest):
    return render(request, "scheduler/queue_method_success.html", {})


def queue_method(request: HttpRequest):
    context = {}
    try:
        emails = [
            email for email in request.POST["input-emails"].split(",") if email != ""
        ]
        phone_numbers = [
            phone_number
            for phone_number in request.POST["input-phone-numbers"].split(",")
            if phone_number != ""
        ]
        if len(emails) + len(phone_numbers) > 0:
            return redirect(queue_method_success)

    except KeyError:
        ...

    return render(request, "scheduler/queue_method.html", context)


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
    return render(request, "scheduler/gantt_chart.html", context)
