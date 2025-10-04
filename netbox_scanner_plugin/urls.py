from django.urls import path
from . import views

urlpatterns = [
    path('scanners/', views.ScannerListView.as_view(), name='scanner_list'),
    path('scanners/add/', views.ScannerEditView.as_view(), name='scanner_add'),
    path('scanners/<int:pk>/', views.ScannerView.as_view(), name='scanner'),
    path('scanners/<int:pk>/edit/', views.ScannerEditView.as_view(), name='scanner_edit'),
    path('scanners/<int:pk>/delete/', views.ScannerDeleteView.as_view(), name='scanner_delete'),
    path('scanners/<int:pk>/run-scan/', views.RunScanView.as_view(), name='run_scan'),
    path('scan-results/', views.ScanResultListView.as_view(), name='scanresult_list'),
    path('scan-results/<int:pk>/edit', views.ScanResultEditView.as_view(), name='scanresult_edit'),
    path('scan-results/<int:pk>/delete/', views.ScanResultEditView.as_view(), name='scanresult_delete'),
    path('scan-results/<int:pk>/', views.ScanResultListView.as_view(), name='scanresult'),

    path(
        "scan-results/<int:pk>/changelog/",
        views.ScanResultListView.as_view(),
        name="scanresult_changelog",
    ),
    path(
        "scanners/<int:pk>/changelog/",
        views.ScannerView.as_view(),
        name="scanner_changelog",
    ),
]