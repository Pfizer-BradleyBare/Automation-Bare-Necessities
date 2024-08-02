from __future__ import annotations

import abn

from .base import BaseView


class NavbarView(BaseView):
    def get_context_data(self, **kwargs) -> dict:

        context = {"abn_state": abn.state}

        return super().get_context_data(**kwargs) | context
