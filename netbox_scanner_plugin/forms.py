# forms.py
from django import forms
from netbox.forms import NetBoxModelForm
from .models import Scanner

class ScannerForm(NetBoxModelForm):
    class Meta:
        model = Scanner
        fields = [
            'name', 'scanner_type', 'description', 'enabled',
            'ip_range', 'target_host', 'snmp_community', 
            'ssh_username', 'ssh_password'
        ]
        widgets = {
            'ssh_password': forms.PasswordInput(render_value=True),
        }

    def clean(self):
        super().clean()  # run parent clean method
        cleaned_data = self.cleaned_data
        scanner_type = cleaned_data.get('scanner_type')

        if scanner_type == 'network_range':
            if not cleaned_data.get('ip_range'):
                raise forms.ValidationError("IP Range is required for Network Range Scan")

        elif scanner_type == 'cisco_switch':
            if not cleaned_data.get('target_host'):
                raise forms.ValidationError("Target host is required for Cisco Switch Scan")

            if not cleaned_data.get('snmp_community') and not (
                cleaned_data.get('ssh_username') and cleaned_data.get('ssh_password')
            ):
                raise forms.ValidationError(
                    "Either SNMP community or SSH credentials are required for Cisco Switch Scan"
                )
        return cleaned_data
