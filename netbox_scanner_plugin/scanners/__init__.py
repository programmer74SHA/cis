# scanners/__init__.py
from .network_range import NetworkRangeScanner
from .cisco_switch import CiscoSwitchScanner

__all__ = ['NetworkRangeScanner', 'CiscoSwitchScanner']