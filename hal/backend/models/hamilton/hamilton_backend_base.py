from django.db import models

from ..backend_base import BackendBase


class HamiltonBackendBase(BackendBase):
    deck_layout = models.FilePathField(
        path="C:\\Program Files (x86)\\HAMILTON\\Methods\\plh",
        match=r"^(?!active_layout\.lay|blank_layout\.lay).*\.lay$",
        recursive=True,
        help_text="Custom made layouts can be placed in any sub folder in the parent folder: C:\\Program Files (x86)\\HAMILTON\\Methods\\plh",
    )
    simulation_on = models.BooleanField()
