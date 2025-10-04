# netbox_scanner_plugin/migrations/0001_initial.py

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('scanner_type', models.CharField(choices=[('network_range', 'Network Range Scan'), ('cisco_switch', 'Cisco Switch Scan')], max_length=20)),
                ('description', models.TextField(blank=True)),
                ('enabled', models.BooleanField(default=True)),
                ('ip_range', models.CharField(blank=True, max_length=100, null=True)),
                ('target_host', models.CharField(blank=True, max_length=255, null=True)),
                ('snmp_community', models.CharField(blank=True, max_length=100, null=True)),
                ('ssh_username', models.CharField(blank=True, max_length=100, null=True)),
                ('ssh_password', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ScanResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('started', models.DateTimeField(auto_now_add=True)),
                ('completed', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('running', 'Running'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending', max_length=20)),
                ('output', models.JSONField(blank=True, default=dict)),
                ('scanner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scan_results', to='netbox_scanner_plugin.scanner')),
            ],
            options={
                'ordering': ['-started'],
            },
        ),
    ]