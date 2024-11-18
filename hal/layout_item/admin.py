from hal.admin import hal_admin

from .models import LayoutItemBase
from .models.hamilton import HamiltonLayoutItem

hal_admin.register(HamiltonLayoutItem)
