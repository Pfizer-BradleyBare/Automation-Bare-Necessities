from abc import ABCMeta

from django.db import models
from polymorphic.models import PolymorphicModel


class _AbstractModelMeta(ABCMeta, type(models.Model)): #type:ignore
    pass


class AbstractModel(models.Model, metaclass=_AbstractModelMeta):
    # You may have common fields here.

    class Meta:
        abstract = True


class _AbstractPolymorphicModelMeta(ABCMeta, type(PolymorphicModel)): #type:ignore
    pass


class AbstractPolymorphicModel(PolymorphicModel, metaclass=_AbstractPolymorphicModelMeta):
    # You may have common fields here.

    class Meta:
        abstract = True
