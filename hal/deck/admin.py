from hal.admin import hal_admin

from .models import Deck, SubDeck

hal_admin.register(Deck)
hal_admin.register(SubDeck)
