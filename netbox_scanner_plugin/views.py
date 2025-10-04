# views.py
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View
from django.http import JsonResponse
from django.contrib import messages
from netbox.views.generic import (
    ObjectListView, ObjectEditView, ObjectDeleteView, ObjectView,
)
from .models import Scanner, ScanResult
from .tables import ScannerTable, ScanResultTable
from .forms import ScannerForm
from .scanners import NetworkRangeScanner, CiscoSwitchScanner
import threading

class ScannerListView(ObjectListView):
    queryset = Scanner.objects.all()
    table = ScannerTable
    template_name = 'netbox_scanner_plugin/scanner_list.html'

class ScannerView(ObjectView):
    queryset = Scanner.objects.all()
    template_name = 'netbox_scanner_plugin/scanner.html'

class ScannerEditView(ObjectEditView):
    queryset = Scanner.objects.all()
    form = ScannerForm
    template_name = 'netbox_scanner_plugin/scanner_edit.html'

class ScannerDeleteView(ObjectDeleteView):
    queryset = Scanner.objects.all()

class RunScanView(View):
    def post(self, request, pk):
        try:
            scanner = Scanner.objects.get(pk=pk)
            scan_result = ScanResult.objects.create(scanner=scanner)
            
            # انتخاب اسکنر مناسب بر اساس نوع
            if scanner.scanner_type == 'network_range':
                scanner_instance = NetworkRangeScanner(scanner, scan_result)
            elif scanner.scanner_type == 'cisco_switch':
                scanner_instance = CiscoSwitchScanner(scanner, scan_result)
            else:
                return JsonResponse({'error': 'Unknown scanner type'}, status=400)
            
            # اجرای اسکن در یک نخ جداگانه
            thread = threading.Thread(target=scanner_instance.scan)
            thread.daemon = True
            thread.start()
            
            return JsonResponse({
                'status': 'started',
                'scan_result_id': scan_result.pk,
                'message': f'Scan for {scanner.name} has been started'
            })
            
        except Scanner.DoesNotExist:
            return JsonResponse({'error': 'Scanner not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

class ScanResultListView(ObjectListView):
    queryset = ScanResult.objects.all()
    table = ScanResultTable
    template_name = 'netbox_scanner_plugin/scanresult_list.html'

class ScanResultEditView(ObjectEditView):
    queryset = Scanner.objects.all()
    form = ScannerForm
    template_name = 'netbox_scanner_plugin/scanresult_edit.html'
