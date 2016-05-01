from rest_framework import viewsets

from .models import Tenant
from .serializers import CreateTenantSerializer, TenantSerializer


class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateTenantSerializer
        else:
            return TenantSerializer
