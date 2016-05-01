from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class StuffAppConfig(AppConfig):
    name = 'tallessa.stuff'
    verbose_name = _('Stuff')
    label = 'tallessa_stuff'
