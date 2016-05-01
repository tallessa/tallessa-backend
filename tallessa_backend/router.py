from rest_framework import routers

from tallessa.tenants.views import TenantViewSet


router = routers.DefaultRouter()
router.register(r'tenants', TenantViewSet)
urlpatterns = router.urls
