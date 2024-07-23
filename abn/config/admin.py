from django.contrib.admin import AdminSite, site
from django.contrib.auth.models import Group, User
from django.db.utils import OperationalError


class ConfigAdmin(AdminSite): ...


config_admin = ConfigAdmin()
# Register your models here.

config_admin = ConfigAdmin(name="config_admin")
# Register your models here.


# This disables the login page for admin.
class AccessUser:
    has_module_perms = has_perm = __getattr__ = lambda s, *a, **kw: True


config_admin.has_permission = (
    lambda r: setattr(r, "user", AccessUser()) or True
)  # type:ignore

site.unregister(Group)
site.unregister(User)

site.has_permission = lambda r: setattr(r, "user", AccessUser()) or True  # type:ignore

# must have at least 1 user to save things to the DB
try:
    if len(User.objects.all()) == 0:

        user = User(username="admin", password="admin")

        user.save()
except OperationalError:
    ...
