from rest_framework import generics, viewsets

from .models import Team
from .serializers import CreateTeamSerializer, TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateTeamSerializer
        else:
            return TeamSerializer


class CurrentTeamView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_object(self):
        return self.request.team
