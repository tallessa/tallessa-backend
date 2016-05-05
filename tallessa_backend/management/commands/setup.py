import logging

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import call_command
from django.core.management.base import BaseCommand

from tallessa.utils import log_get_or_create


# usually you should getLogger(__name__) but we are not under the tallessa namespace right now
logger = logging.getLogger('tallessa')


class Command(BaseCommand):
    def handle(self, *args, **options):
        management_commands = [
            (('collectstatic',), dict(interactive=False)),
            (('migrate',), dict()),
        ]

        if settings.DEBUG:
            management_commands.append((('setup_default_team',), dict()))

        for pargs, opts in management_commands:
            logger.info("** Running: %s", pargs[0])
            call_command(*pargs, **opts)

        if settings.DEBUG:
            user, created = User.objects.get_or_create(
                username='mahti',
                defaults=dict(
                    first_name='Markku',
                    last_name='Mahtinen',
                    is_staff=True,
                    is_superuser=True,
                ),
            )

            if created:
                user.set_password('mahti')
                user.save()

            log_get_or_create(logger, user, created)
