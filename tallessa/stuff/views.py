from rest_framework import viewsets

from tallessa.teams.filters import TeamFilterBackend
from tallessa.teams.mixins import SetTeamOnCreate

from .models import Item, Location
from .serializers import CreateItemSerializer, CreateLocationSerializer, ItemSerializer, LocationSerializer


class StuffViewSet(SetTeamOnCreate, viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Item.objects.all()
    filter_backends = (TeamFilterBackend,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateItemSerializer
        else:
            return ItemSerializer


class LocationViewSet(SetTeamOnCreate, viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Location.objects.all()
    filter_backends = (TeamFilterBackend,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateLocationSerializer
        else:
            return LocationSerializer
