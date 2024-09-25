from django.apps import AppConfig


class MethodConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "method"

    def ready(self) -> None:
        ...
        # source_path = Path(
        #    "\\\\amer.pfizer.com\\pfizerfiles\\Research\\CHV\\btxpharmsci\\xAdmin\\AutomationBareNecessities\\Methods",
        # )
        # destination_path = Path(settings.BASE_DIR) / "_abn_methods"

        # shutil.rmtree(destination_path, ignore_errors=True)

        # shutil.copytree(source_path, destination_path, dirs_exist_ok=True)
