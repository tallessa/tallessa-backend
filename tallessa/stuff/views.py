from rest_framework import viewsets

from tallessa.teams.filters import TeamFilterBackend
from tallessa.teams.mixins import SetTeamOnCreate

from .models import Item, Place
from .serializers import CreateItemSerializer, CreatePlaceSerializer, ItemSerializer, PlaceSerializer


class StuffViewSet(SetTeamOnCreate, viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Item.objects.all()
    filter_backends = (TeamFilterBackend,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateItemSerializer
        else:
            return ItemSerializer


class PlaceViewSet(SetTeamOnCreate, viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Place.objects.all()
    filter_backends = (TeamFilterBackend,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreatePlaceSerializer
        else:
            return PlaceSerializer
