from netbox.api.viewsets import NetBoxModelViewSet
from ..models import Scanner, ScanResult
from .serializers import ScannerSerializer, ScanResultSerializer

class ScannerViewSet(NetBoxModelViewSet):
    queryset = Scanner.objects.all()
    serializer_class = ScannerSerializer

class ScanResultViewSet(NetBoxModelViewSet):
    queryset = ScanResult.objects.all()
    serializer_class = ScanResultSerializer