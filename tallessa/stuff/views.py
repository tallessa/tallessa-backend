from rest_framework import viewsets, generics

from .models import Item, Location
from .serializers import CreateItemSerializer, ItemSerializer, CreateLocationSerializer, LocationSerializer
from tallessa.tenants.filters import TenantFilterBackend
from tallessa.tenants.mixins import SetTenantOnCreate


class StuffViewSet(SetTenantOnCreate, viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Item.objects.all()
    filter_backends = (TenantFilterBackend,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateItemSerializer
        else:
            return ItemSerializer


class LocationViewSet(SetTenantOnCreate, viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Item.objects.all()
    filter_backends = (TenantFilterBackend,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateLocationSerializer
        else:
            return LocationSerializer
