from netmiko import ConnectHandler
from django.utils import timezone
from .base import BaseScanner
from dcim.models import Device, DeviceRole, DeviceType, Manufacturer, Site, Interface
from ipam.models import IPAddress, VLAN
from dcim.choices import InterfaceTypeChoices
from ipam.choices import IPAddressStatusChoices

class CiscoSwitchScanner(BaseScanner):
    def scan(self):
        try:
            self.update_status('running')
            
            device_info = self._connect_and_gather_info()
            self._update_netbox_models(device_info)
            
            self.update_status('completed', {
                'device_info': device_info,
                'scan_type': 'cisco_switch'
            })
            
        except Exception as e:
            self.update_status('failed', {'error': str(e)})
    
    def _connect_and_gather_info(self):
        connection_params = {
            'device_type': 'cisco_ios',
            'host': self.scanner.target_host,
            'username': self.scanner.ssh_username,
            'password': self.scanner.ssh_password,
        }
        
        with ConnectHandler(**connection_params) as conn:
            # Get device basic info
            show_version = conn.send_command('show version', use_textfsm=True)
            show_interfaces = conn.send_command('show interfaces', use_textfsm=True)
            show_vlan = conn.send_command('show ip interface bri | include Vlan', use_textfsm=True)
            
            return {
                'version': show_version[0] if show_version else {},
                'interfaces': show_interfaces,
                'vlans': show_vlan,
            }
    
    def _update_netbox_models(self, device_info):
        version_info = device_info['version']
        
        # Get or create manufacturer
        manufacturer, _ = Manufacturer.objects.get_or_create(
            name='Cisco',
            defaults={'slug': 'cisco'}
        )
        

        device_role, created = DeviceRole.objects.get_or_create(
            name='switch',  # نام نقش را مطابق محیط NetBox خود تغییر دهید
            defaults={'slug': 'switch', 'color': '00ff00'}
        )
        # Get or create device type
        device_type, _ = DeviceType.objects.get_or_create(
            manufacturer=manufacturer,
            model=version_info.get('hardware', ['Unknown'])[0],
            defaults={'slug': version_info.get('hardware', ['unknown'])[0].lower()}
        )
        
        # Get or create device
        device, created = Device.objects.get_or_create(
            name=version_info.get('hostname', self.scanner.target_host),
            defaults={
                'device_type': device_type,
                'site': Site.objects.first(),  # Default to first site
                'status': 'active',
                'role': device_role,
                'serial': version_info.get('serial', [''])[0],
            }
        )
        
        # Update interfaces
        for interface_info in device_info['interfaces']:
            interface, _ = Interface.objects.get_or_create(
                device=device,
                name=interface_info['interface'],
                defaults={
                    'type': 'other',
                    'enabled': interface_info['link_status'] == 'up',
                }
            )
            
        self._create_or_update_vlans(device_info['vlans'], device.site,device)

    def _create_or_update_vlans(self, vlans_data, site, device):
        for vlan_info in vlans_data:
            interface_name = vlan_info.get('interface')
            ip_address = vlan_info.get('ip_address')
            status = vlan_info.get('status', '').lower()
            
            vlan_id = None
            if interface_name and interface_name.lower().startswith('vlan'):
                try:
                    vlan_id = int(interface_name[4:])
                except ValueError:
                    vlan_id = None

            vlan_name = interface_name

            vlan_obj, vlan_created = VLAN.objects.get_or_create(
                vid=vlan_id,
                site=site,
                defaults={'name': vlan_name, 'status': 'active'}
            )
            if not vlan_created:
                vlan_obj.name = vlan_name
                vlan_obj.status = 'active'
                vlan_obj.save()


            interface_obj, intf_created = Interface.objects.get_or_create(
                device=device,
                name=interface_name,
                defaults={
                    'type': InterfaceTypeChoices.TYPE_VIRTUAL,
                    'enabled': (status == 'up')
                }
            )
            if not intf_created:
                interface_obj.enabled = (status == 'up')
                interface_obj.save()

            if ip_address and ip_address.lower() != 'unassigned':
                ip_cidr = f"{ip_address}/32"
                ip_obj, ip_created = IPAddress.objects.get_or_create(
                    address=ip_cidr,
                    defaults={'status': IPAddressStatusChoices.STATUS_ACTIVE}
                )
                ip_obj.assigned_object = interface_obj
                ip_obj.save()