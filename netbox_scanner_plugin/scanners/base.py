# scanners/base.py
import abc
from netbox_scanner_plugin.models import ScanResult

class BaseScanner(abc.ABC):
    def __init__(self, scanner_instance, scan_result_instance):
        self.scanner = scanner_instance
        self.scan_result = scan_result_instance
    
    @abc.abstractmethod
    def scan(self):
        pass
    
    def update_status(self, status, output=None):
        self.scan_result.status = status
        if output:
            self.scan_result.output = output
        self.scan_result.save()