from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from .models import Tenant


def determine_tenant(request):
    hostname = request.META.get('HTTP_HOST')
    tenant = Tenant.objects.filter(hostname=hostname).first()

    if tenant is None:
        if hasattr(settings, 'TALLESSA_DEFAULT_TENANT_SLUG'):
            return Tenant.objects.get(slug=settings.TALLESSA_DEFAULT_TENANT_SLUG)
        else:
            raise ImproperlyConfigured('Tenant not found for hostname: {}'.format(hostname))

    return tenant


class TenantMiddleware(object):
    def process_request(self, request):
        request.tenant = determine_tenant(request)
