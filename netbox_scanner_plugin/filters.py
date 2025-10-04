# filters.py (اختیاری - برای افزودن قابلیت فیلتر کردن)
import django_filters
from .models import Scanner, ScanResult

class ScannerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    scanner_type = django_filters.ChoiceFilter(choices=Scanner.SCANNER_TYPES)

    class Meta:
        model = Scanner
        fields = ['name', 'scanner_type', 'enabled']

class ScanResultFilter(django_filters.FilterSet):
    scanner = django_filters.ModelChoiceFilter(queryset=Scanner.objects.all())
    status = django_filters.ChoiceFilter(choices=ScanResult.STATUS_CHOICES)

    class Meta:
        model = ScanResult
        fields = ['scanner', 'status']