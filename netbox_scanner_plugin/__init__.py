# __init__.py
from netbox.plugins import PluginConfig

class ScannerPluginConfig(PluginConfig):
    name = 'netbox_scanner_plugin'
    verbose_name = 'Network Scanner Plugin'
    description = 'Network discovery and scanner management for NetBox'
    version = '1.0.0'
    author = 'sajad balaniyan'
    base_url = 'scanner'
    required_settings = []
    default_settings = {}

config = ScannerPluginConfig