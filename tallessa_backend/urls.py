from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework import routers

from tallessa.stuff.views import LocationViewSet, StuffViewSet
from tallessa.tenants.views import CurrentTenantView, TenantViewSet


router = routers.DefaultRouter()
router.register(r'tenants', TenantViewSet)
router.register(r'stuff', StuffViewSet, base_name='stuff')
router.register(r'locations', LocationViewSet, base_name='locations')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/', include(router.urls, namespace='v1')),
    url(r'^api/v1/tenant', CurrentTenantView.as_view(), name='current-tenant'),
    url(r'^$', RedirectView.as_view(url='/api/v1')),
]
