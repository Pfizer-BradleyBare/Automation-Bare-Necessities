from django.apps import AppConfig
from django.db.utils import OperationalError


class SolutionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "solution"

    def ready(self) -> None:
        super().ready()

        from solution.models import PredefinedSolution, SolutionPropertyPreset

        try:
            if len(SolutionPropertyPreset.objects.all()) == 0:

                SolutionPropertyPreset(
                    name="Water",
                    liquid_type="Aqueous",
                    volatility="Low",
                    viscosity="Medium",
                    homogeneity="Homogenous",
                ).save()

        except OperationalError:
            ...

        try:
            if len(PredefinedSolution.objects.all()) == 0:

                PredefinedSolution(
                    name="Water",
                    storage_condition="Ambient",
                    liquid_type="Aqueous",
                    volatility="Low",
                    viscosity="Medium",
                    homogeneity="Homogenous",
                ).save()

        except OperationalError:
            ...
