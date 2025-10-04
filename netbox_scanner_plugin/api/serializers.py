from netbox.api.serializers import NetBoxModelSerializer
from ..models import Scanner, ScanResult

class ScannerSerializer(NetBoxModelSerializer):
    class Meta:
        model = Scanner
        fields = ('id', 'name', 'scanner_type', 'description', 'enabled', 'ip_range', 'target_host', 'snmp_community', 'ssh_username', 'ssh_password')

class ScanResultSerializer(NetBoxModelSerializer):
    scanner = ScannerSerializer(nested=True, read_only=True)

    class Meta:
        model = ScanResult
        fields = ('id', 'scanner', 'started', 'completed', 'status', 'output')