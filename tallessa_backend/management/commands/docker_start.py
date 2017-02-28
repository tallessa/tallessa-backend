# encoding: utf-8

from __future__ import unicode_literals, print_function

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import ProgrammingError

from tallessa.teams.models import Team


class Command(BaseCommand):
    args = ''
    help = 'Docker development environment entry point'

    def handle(self, *args, **options):

        if not settings.DEBUG:
            raise ValueError('Should run with DEBUG=true')

        try:
            Team.objects.first()
        except ProgrammingError:
            call_command('setup')

        call_command('runserver', '0.0.0.0:8000')
