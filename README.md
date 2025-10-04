# NetBox Scanner Plugin

A NetBox plugin for automated network discovery and device scanning. This plugin provides network range scanning and Cisco switch scanning capabilities to automatically populate NetBox with discovered devices, interfaces, IP addresses, and VLANs.

---

## ✨ Features

| Feature                   | Description                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| Network Range Scanning    | Discovers active IP addresses and services within specified IP ranges.                      |
| Cisco Switch Scanning     | Automatically extracts and imports switch configuration, interfaces, and VLAN information.  |
| Automated Data Population | Creates and updates NetBox models (Devices, Interfaces, IP Addresses, VLANs) automatically. |
| Scan History & Results    | Tracks and reviews all scan results with detailed output.                                   |
| Integrated User Interface | Simple interface integrated into NetBox for managing scanners and viewing results.          |

---

## 🚀 Installation

### Prerequisites

* NetBox v3.2 or later
* Python 3.10+
* Required Python packages: `python-nmap`, `netmiko`, `textfsm`

### Step-by-Step Installation

#### 0. Clone the Plugin Repository

```bash
cd /opt/netbox/netbox/plugins/

git clone https://github.com/sajadblnyn/netbox-scanner-plugin.git
```

#### 1. Install the Python Package

Activate the NetBox virtual environment and install the plugin.

```bash
# Activate NetBox virtual environment
source /opt/netbox/venv/bin/activate

# Install the plugin package (from a distribution)
pip install netbox-scanner-plugin

# Or, for a development installation from a local path
pip install -e /path/to/netbox-scanner-plugin
```

#### 2. Install Nmap

```bash

# Install nmap by apt
sudo apt install nmap

```

#### 3. Enable the Plugin

In `configuration.py`, add the plugin to the `PLUGINS` list:

```python
PLUGINS = [
    'netbox_scanner_plugin',  # Add this line
]
```

#### 4. Configure the Plugin (Optional)

Define configuration in `PLUGINS_CONFIG` if needed:

```python
PLUGINS_CONFIG = {
    'netbox_scanner_plugin': {
        'default_timeout': 300,
        'max_scan_threads': 5,
        # Add other parameters as needed
    },
}
```

#### 5. Run Database Migrations

```bash
cd /opt/netbox/netbox/
python3 manage.py migrate netbox_scanner_plugin
```

#### 6. Collect Static Files

```bash
python3 manage.py collectstatic --no-input
```

#### 7. Restart NetBox Services

```bash
sudo systemctl restart netbox netbox-rq
```

---

## 📖 Usage

### Creating and Managing Scanners

* Navigate to `Plugins → Network Scanner Plugin → Scanners` in the NetBox UI.
* Click **Add Scanner** to create a new scanner.
* Configure scanner parameters:

**Network Range Scanners:**

* `IP Range`: The network range to scan (e.g., 192.168.1.0/24)

**Cisco Switch Scanners:**

* `Target Host`: Hostname or IP of the switch
* `Credentials`: SNMP community string or SSH username/password

### Running Scans and Viewing Results

* Click **Run Scan** next to any scanner.
* Monitor progress and view results in **Scan History**.
* Click individual scan results to see detailed output and created/updated NetBox objects.

---

## 🔧 Configuration Reference

### Scanner Model

| Field          | Description                                         |
| -------------- | --------------------------------------------------- |
| name           | Unique identifier for the scanner                   |
| scanner_type   | Type of scanner (`network_range` or `cisco_switch`) |
| enabled        | Enable or disable the scanner                       |
| ip_range       | Target IP range for network scans                   |
| target_host    | Hostname or IP for Cisco device scans               |
| snmp_community | SNMP community string                               |
| ssh_username   | SSH username                                        |
| ssh_password   | SSH password                                        |

### Scan Result Model

| Field     | Description                                               |
| --------- | --------------------------------------------------------- |
| scanner   | Reference to the parent scanner                           |
| started   | Scan start timestamp                                      |
| completed | Scan completion timestamp                                 |
| status    | Scan status (`pending`, `running`, `completed`, `failed`) |
| output    | JSON output of detailed scan results                      |

---

## 🛠️ Development

### Project Structure

```
netbox-scanner-plugin/
├── netbox_scanner_plugin/
│   ├── api/
│   ├── migrations/
│   ├── scanners/
│   ├── templates/
│   ├── __init__.py
│   ├── models.py
│   ├── tables.py
│   ├── views.py
│   └── urls.py
├── pyproject.toml
└── README.md
```

### Setting Up a Development Environment

```bash
python3 -m venv ~/.virtualenvs/my_plugin
source ~/.virtualenvs/my_plugin/bin/activate

# Make NetBox available in your environment
echo /opt/netbox/netbox > $VIRTUAL_ENV/lib/python3.12/site-packages/netbox.pth

# Install the plugin in development mode
pip install -e .
```

---

## 🐛 Troubleshooting

### Common Issues

* **Plugin not appearing:** Verify it is in `PLUGINS` list and services restarted.
* **Database errors:** Ensure migrations are applied (`python3 manage.py migrate`).
* **Scan failures:** Check network connectivity and credentials. Review scan result output.

### Getting Help

* Check NetBox logs for detailed errors.
* Ensure all required Python packages (`python-nmap`, `netmiko`) are installed.

---

## 📄 License

This plugin is distributed under the same license as NetBox.

---

## 🤝 Contributing

Contributions are welcome! Submit issues, feature requests, or pull requests.
