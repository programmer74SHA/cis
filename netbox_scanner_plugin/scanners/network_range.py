import nmap
from django.utils import timezone
from .base import BaseScanner
from ipam.models import IPAddress
from dcim.models import Device

class NetworkRangeScanner(BaseScanner):
    def scan(self):
        try:
            self.update_status('running')
            
            nm = nmap.PortScanner()
            ip_range = self.scanner.ip_range
            
            # Perform network scan
            nm.scan(hosts=ip_range, arguments='-sn -PE -PA21,23,80,3389')
            
            discovered_hosts = []
            
            for host in nm.all_hosts():
                host_info = {
                    'ip_address': host,
                    'status': nm[host].state(),
                    'hostname': nm[host].hostname(),
                }
                
                # Create or update IP Address in NetBox
                ip_address, created = IPAddress.objects.get_or_create(
                    address=host,
                    defaults={
                        'status': 'active',
                        'description': f'Discovered by scanner: {self.scanner.name}'
                    }
                )
                
                if created:
                    host_info['action'] = 'created'
                else:
                    host_info['action'] = 'exists'
                
                discovered_hosts.append(host_info)
            
            self.update_status('completed', {
                'discovered_hosts': discovered_hosts,
                'total_hosts': len(discovered_hosts),
                'scan_type': 'network_range'
            })
            
        except Exception as e:
            self.update_status('failed', {'error': str(e)})