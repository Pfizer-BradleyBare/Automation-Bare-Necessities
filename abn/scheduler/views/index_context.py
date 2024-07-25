import pandas as pd
import plotly.express as px

from abn.views import NavbarView


class IndexContextView(NavbarView):

    def get_context_data(self, **kwargs) -> dict:

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
                dict(
                    Task="Job C",
                    Start="2009-02-20",
                    Finish="2009-05-30",
                    Resource="Max",
                ),
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

        return super().get_context_data(**kwargs) | context
