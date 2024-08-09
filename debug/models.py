from django.db import models


class LogSourceOptions(models.IntegerChoices):
    PLH = 1
    ABN = 2


class LogLevelOptions(models.IntegerChoices):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    CRITICAL = 4
    ERROR = 5


class Trace(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True)
    log_source = models.IntegerField(
        choices=LogSourceOptions.choices,
    )
    log_level = models.IntegerField(
        choices=LogLevelOptions.choices,
    )
    meta_info = models.TextField()
    message = models.TextField()

    class Meta:
        ordering = ["time_stamp"]

    def __str__(self) -> str:
        return self.message


class Silly(models.Model):
    a = 1
    b = 2
    c = 3

    def __str__(self) -> str:
        return f"{self.a}{self.b}{self.c}"
