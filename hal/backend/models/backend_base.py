from abc import abstractmethod
from typing import ClassVar

from django.core.exceptions import ValidationError
from django.db import models
from plh.tools import BackendBase as PLHBackendBase
from polymorphic.models import PolymorphicModel

from debug import plh_logger


class BackendBase(PolymorphicModel):
    _backend_instances: ClassVar[dict[str, PLHBackendBase]] = {}

    identifier = models.CharField(
        max_length=50,
        unique=True,
        blank=False,
        null=False,
    )

    @abstractmethod
    def initialize(self): ...

    @abstractmethod
    def deinitialize(self): ...

    def get_plh_backend(self) -> PLHBackendBase:
        if self.identifier not in self._backend_instances:
            plh_logger.critical(
                f"A device attempted to use backend '{self.identifier}' but it is not currently running.",
            )
            raise RuntimeError(
                f"A device attempted to use backend '{self.identifier}' but it is not currently running.",
            )

        return self._backend_instances[self.identifier]

    def clean(self) -> None:
        if self.identifier in self._backend_instances:
            plh_logger.critical(
                f"Backend '{self.identifier}' is currently running. To make changes you first need to stop the backend.",
            )
            raise ValidationError(
                "Backend '{self.identifier}' is currently running. To make changes you first need to stop the backend.",
            )

        return super().clean()

    def __str__(self) -> str:
        return self.identifier

    class Meta:
        ordering = ["identifier"]
