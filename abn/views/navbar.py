from __future__ import annotations

from .base import BaseView


class NavbarView(BaseView):
    def get_context_data(self, **kwargs) -> dict:

        context = {"abn_state": "run"}

        return super().get_context_data(**kwargs) | context
