---

# Host Dependency Installation Role

This Ansible role installs various system dependencies and configures settings specific to different host types in a clustered environment. It includes tasks for updating repositories, managing time zones, and installing both pre- and post-installation packages based on host roles (e.g., BDA, SF, NBA).

## Role Structure

```
├── files/                                 # Additional files
├── handlers/
│   └── main.yml                           # Handlers for specific service restart/reload actions
├── meta/
│   └── main.yml                           # Role metadata
├── tasks/
│   ├── install_bda_hosts_dependencies.yml # BDA-specific dependencies
│   ├── install_nba_hosts_dependencies.yml # NBA-specific dependencies
│   ├── install_postinstall_packages.yml   # General post-install packages
│   ├── install_preinstall_packages.yml    # General pre-install packages
│   ├── install_scanner_hosts_dependencies.yml # Scanner-specific dependencies
│   ├── install_sf_hosts_dependencies.yml  # SF-specific dependencies
│   ├── main.yml                           # Main task file to execute all tasks
│   ├── update_repository_list.yml         # Task to update package repository list
│   └── update_time_zone.yml               # Task to configure time zone
└── vars/
    └── main.yml                           # Default variables for role
```

## Role Variables

Define these variables in `vars/main.yml` or override them in playbooks to customize the role:

- **`TimeZone`**: The timezone to set on all hosts, ensuring consistent system time across the cluster.

## Tasks Overview

The `main.yml` task file includes several task blocks to import and execute specific task files based on host roles and required dependencies:

1. **Update Repository List**:
   - Updates the package repository list to ensure packages are fetched from the latest sources.

2. **Install Pre-Install Packages**:
   - Installs essential system tools like `curl`, `wget`, and `net-tools` on all hosts.

3. **Install Post-Install Packages**:
   - Installs additional utilities for monitoring, system management, and diagnostics, such as `htop`, `tcpdump`, and `ufw`.

4. **Install Dependencies for Specific Host Types**:
   - Each host type (BDA, SF, NBA, Scanner) has a separate task file that installs role-specific packages:
     - **BDA**: Installs `kibana`, `filebeat`, `docker`, and other tools.
     - **NBA**: Installs `suricata`, `logstash`, and `zeek`.
     - **SF**: Installs `filebeat`, `kafka`, and `logstash`.
     - **Scanner**: Installs `nmap`, `siem-gvm`, and `logstash`.

5. **Configure System Time Zone**:
   - Sets the system timezone to the specified `TimeZone` variable and ensures that it is correctly applied.

## Handlers

If certain services need to be restarted or reloaded after package installations, handlers can be added in `handlers/main.yml` to handle these actions.
