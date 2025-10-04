# netbox_scanner_plugin/models.py
from django.db import models
from netbox.models import NetBoxModel
from django.urls import reverse

class Scanner(NetBoxModel):
    SCANNER_TYPES = (
        ('network_range', 'Network Range Scan'),
        ('cisco_switch', 'Cisco Switch Scan'),
    )

    name = models.CharField(max_length=100, unique=True)
    scanner_type = models.CharField(max_length=20, choices=SCANNER_TYPES)
    description = models.TextField(blank=True)
    enabled = models.BooleanField(default=True)
    
    # Network Range Scan parameters
    ip_range = models.CharField(max_length=100, blank=True, null=True)
    
    # Cisco Switch Scan parameters
    target_host = models.CharField(max_length=255, blank=True, null=True)
    snmp_community = models.CharField(max_length=100, blank=True, null=True)
    ssh_username = models.CharField(max_length=100, blank=True, null=True)
    ssh_password = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_scanner_plugin:scanner', args=[self.pk])

class ScanResult(NetBoxModel):
    scanner = models.ForeignKey(Scanner, on_delete=models.CASCADE, related_name='scan_results')
    started = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('running', 'Running'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ), default='pending')
    output = models.JSONField(default=dict, blank=True)
    
    class Meta:
        ordering = ['-started']
    
    def __str__(self):
        return f"{self.scanner.name} - {self.started}"