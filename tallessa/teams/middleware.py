from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import get_object_or_404

from .models import Team


def determine_team(request):
    hostname = request.META.get('HTTP_HOST')
    if getattr(settings, 'TALLESSA_DEFAULT_TEAM_SLUG'):
        try:
            return Team.objects.get(hostname=hostname)
        except Team.DoesNotExist:
            return get_object_or_404(Team, slug=settings.TALLESSA_DEFAULT_TEAM_SLUG)
    else:
        return get_object_or_404(Team, hostname=hostname)



class TeamMiddleware(object):
    def process_request(self, request):
        request.team = determine_team(request)
