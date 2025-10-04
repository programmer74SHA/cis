# tables.py
import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from .models import Scanner, ScanResult

class ScannerTable(NetBoxTable):
    name = tables.Column(linkify=True)
    scanner_type = tables.Column(verbose_name='Type')
    enabled = columns.BooleanColumn(verbose_name='Enabled')
    ip_range = tables.Column(verbose_name='IP Range')
    target_host = tables.Column(verbose_name='Target Host')

    class Meta(NetBoxTable.Meta):
        model = Scanner
        fields = ('pk', 'id', 'name', 'scanner_type', 'enabled', 'ip_range', 'target_host', 'description')
        default_columns = ('pk', 'name', 'scanner_type', 'enabled', 'description')

class ScanResultTable(NetBoxTable):
    scanner = tables.Column(linkify=True)
    status = columns.ChoiceFieldColumn()
    started = tables.DateTimeColumn()
    completed = tables.DateTimeColumn()
    summary = tables.Column(accessor='output', orderable=False, verbose_name='Summary', empty_values=())

    def render_summary(self, value, record):
        if record.output:
            if record.scanner.scanner_type == 'network_range':
                hosts = record.output.get('discovered_hosts', [])
                return f"Discovered {len(hosts)} hosts : {hosts}"
            elif record.scanner.scanner_type == 'cisco_switch':
                return f"Scanned {record.scanner.target_host}"
        return "No results"

    class Meta(NetBoxTable.Meta):
        model = ScanResult
        fields = ('pk', 'id', 'scanner', 'status', 'started', 'completed', 'summary')
        default_columns = ('pk', 'scanner', 'status', 'started', 'completed', 'summary')