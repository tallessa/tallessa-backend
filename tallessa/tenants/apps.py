from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TenantsAppConfig(AppConfig):
    name = 'tallessa.tenants'
    verbose_name = _('Tenants')
    label = 'tallessa_tenants'
