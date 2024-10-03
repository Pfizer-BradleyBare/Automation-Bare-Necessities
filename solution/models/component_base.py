from __future__ import annotations

from polymorphic.models import PolymorphicModel


class ComponentBase(PolymorphicModel):
    """Used as a way to get all solutions and components to show up as a foreign key for SolutionComponent ONLY.
    Because ease of use for users is imperative.
    """

    def get_name(self) -> str:
        raise NotImplementedError
