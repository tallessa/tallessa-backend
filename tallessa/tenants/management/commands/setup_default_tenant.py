import logging

from django.core.management.base import BaseCommand, CommandError

from ...models import Tenant
from tallessa.utils import log_get_or_create


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        tenant, created = Tenant.objects.get_or_create(
            slug='hukassa',
            defaults=dict(
                name='Hukassa',
                hostname='hukassa.tallessa.eu',
            ),
        )
        log_get_or_create(logger, tenant, created)
