from django.contrib import admin
from django.contrib.auth.models import Group, User

# Register your models here.

admin.site.unregister(Group)
admin.site.unregister(User)


class AccessUser:
    has_module_perms = has_perm = __getattr__ = lambda s, *a, **kw: True


admin.site.has_permission = (
    lambda r: setattr(r, "user", AccessUser()) or True
)  # type:ignore
