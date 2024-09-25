from __future__ import annotations

from django.db import models

from .user_method_base import UserMethodBase


class ExecutingMethod(UserMethodBase):
    state = models.CharField(
        max_length=15,
        choices=(
            ("Reading", "Reading"),
            ("Running", "Running"),
            ("Paused", "Paused"),
            ("Waiting on User", "Waiting on User"),
            ("Complete", "Complete"),
            ("Aborted", "Aborted"),
            ("Cleanup", "Cleanup"),
        ),
        default="Reading",
    )
    emails = models.CharField(max_length=100, blank=False, null=False)
    phone_numbers = models.CharField(max_length=100, blank=True)
    desired_completion_time = models.DateTimeField(blank=False, null=False)
