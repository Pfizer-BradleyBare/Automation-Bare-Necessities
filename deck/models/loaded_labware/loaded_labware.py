from django.db import models

from hal.labware.models import LabwareBase
from plh_config.layout_item.models import LayoutItemBase


class LoadedLabware(models.Model):
    labware = models.ForeignKey(to=LabwareBase, on_delete=models.CASCADE)

    layout_item = models.ForeignKey(to=LayoutItemBase, on_delete=models.CASCADE)
