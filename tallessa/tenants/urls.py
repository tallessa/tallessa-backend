from rest_framework import routers

from .views import TenantViewSet

router = routers.SimpleRouter()
router.register(r'tenants', TenantViewSet)
urlpatterns = router.urls
