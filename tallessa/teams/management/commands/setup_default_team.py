import logging

from django.core.management.base import BaseCommand

from tallessa.utils import log_get_or_create

from ...models import Team


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        team, created = Team.objects.get_or_create(
            slug='hukassa',
            defaults=dict(
                name='Hukassa',
                hostname='hukassa.tallessa.eu',
            ),
        )
        log_get_or_create(logger, team, created)
