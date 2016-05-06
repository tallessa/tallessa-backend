from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UsersAppConfig(AppConfig):
    name = 'tallessa.users'
    verbose_name = _('Users')
    label = 'tallessa_users'
