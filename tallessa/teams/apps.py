from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TeamsAppConfig(AppConfig):
    name = 'tallessa.teams'
    verbose_name = _('Teams')
    label = 'tallessa_teams'
