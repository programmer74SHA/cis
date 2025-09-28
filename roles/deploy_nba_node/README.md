# Zeek and Suricata Network Monitoring Configuration Ansible Role

This Ansible role configures network monitoring using Zeek and Suricata, setting up necessary network interfaces, importing plugins, and configuring services for efficient deployment in a Security Information and Event Management (SIEM) environment.

## Role Structure

1. **Network Configuration** (`tasks/network_configuration.yml`): Sets up the required network interface if not present, installs `iproute2`, and enables promiscuous mode for packet monitoring.

    - **Key Tasks**:
      - Installs `iproute2` if missing.
      - Checks if the network interface exists, creating a dummy interface if absent.
      - Enables promiscuous mode on the network interface to capture all packets.

2. **SIEM and Zeek Plugin Setup** (`tasks/import_zeek_plugins.yml`): Ensures SIEM directories exist, copies the Zeek plugins bundle, and imports plugins into Zeek for network traffic analysis.

    - **Key Tasks**:
      - Creates SIEM and Zeek plugins directories.
      - Copies the Zeek plugins bundle to the NBA server.
      - Imports the plugins using `zkg unbundle`.

3. **Zeek Service Configuration** (`tasks/config_zeek_service.yml`): Configures Zeek to use the specified network interface and sets up the Zeek service using systemd.

    - **Key Tasks**:
      - Updates the Zeek `node.cfg` file to use the specified network interface.
      - Deploys changes to Zeek with `zeekctl deploy`.
      - Copies the Zeek systemd service file to `/etc/systemd/system` and reloads the daemon.

4. **Suricata Configuration** (`tasks/config_suricata.yml`): Updates the Suricata configuration to use the `pfring` interface and restarts the service.

    - **Key Tasks**:
      - Uses `sed` to modify the Suricata configuration to set the interface to `pfring`.
      - Restarts the Suricata service for changes to take effect.

## Variables

All customizable variables are defined in `vars/main.yml`. Key variables include:
- `nba_interface_name`: Name of the network interface for monitoring.
- `siem_file_directory`: Directory path for SIEM files.
- `zeek_plugins_directory`: Directory for storing Zeek plugins.
- `zeek_binaries_folder`: Path to Zeek binaries.

## Usage

Include this role in your playbook to automate the setup and configuration of Zeek and Suricata on your monitoring nodes.