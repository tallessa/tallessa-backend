from django.conf.urls import include, urls
from rest_framework_nested import routers

from tallessa.stuff.views import LocationViewSet, StuffViewSet
from tallessa.tenants.views import TenantViewSet


router = routers.DefaultRouter()
router.register(r'tenants', TenantViewSet)

tenants_router = routers.NestedSimpleRouter(router, 'tenants', lookup='tenant')
tenants_router.register(r'stuff', StuffViewSet, base_name='tenant-stuff')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(tenants_router.urls)),
]
