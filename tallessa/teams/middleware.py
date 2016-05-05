from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from .models import Team


def determine_team(request):
    hostname = request.META.get('HTTP_HOST')
    team = Team.objects.filter(hostname=hostname).first()

    if team is None:
        if hasattr(settings, 'TALLESSA_DEFAULT_TEAM_SLUG'):
            return Team.objects.get(slug=settings.TALLESSA_DEFAULT_TEAM_SLUG)
        else:
            raise ImproperlyConfigured('Team not found for hostname: {}'.format(hostname))

    return team


class TeamMiddleware(object):
    def process_request(self, request):
        request.team = determine_team(request)
