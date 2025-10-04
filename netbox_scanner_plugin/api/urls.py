from netbox.api.routers import NetBoxRouter
from . import views

router = NetBoxRouter()
router.register('scanners', views.ScannerViewSet)
router.register('scan-results', views.ScanResultViewSet)

urlpatterns = router.urls