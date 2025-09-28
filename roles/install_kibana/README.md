
---

# Ansible Role: Kibana

This Ansible role installs, configures, and manages Kibana in an Elastic Stack environment, handling SSL setup, Fleet integration, Elasticsearch output configurations, and geo-IP data provisioning. This role is designed for environments with multiple host groups (e.g., `BDA`, `SF`, `HOT`), allowing it to adapt configurations based on the host's group membership.

## Table of Contents

- [Ansible Role: Kibana](#ansible-role-kibana)
  - [Table of Contents](#table-of-contents)
  - [Role Overview](#role-overview)
  - [Directory Structure](#directory-structure)
  - [Role Variables](#role-variables)
  - [Key Role Tags](#key-role-tags)
  - [Tasks Overview](#tasks-overview)
  - [Usage Notes](#usage-notes)
  - [Handlers](#handlers)

## Role Overview

The Kibana role enables seamless setup and configuration of Kibana nodes, with flexible support for multiple environments. This includes:

- Installation of Kibana from a local repository.
- SSL certificate management.
- Integration with Fleet server for Elastic Agent management.
- Geo-IP database handling and provisioning via Nginx.
- Configurable Elasticsearch output settings for different host groups.

## Directory Structure

The role is organized as follows:

```plaintext
.
├── files
│   ├── ca-certs.pem                  # CA certificate for Kibana
│   └── geoip.conf                    # GeoIP configuration for Nginx
├── handlers
│   └── main.yml                      # Handlers to restart or reload services
├── meta
│   └── main.yml                      # Metadata about the role
├── tasks
│   ├── config_kibana_new_node.yml    # Configure Fleet outputs for a new node
│   ├── configure_kibana.yml          # General Kibana configuration tasks
│   ├── copy_geo_ip_files.yml         # Copy GeoIP files and configure Nginx
│   ├── create_x509_certificate_file.yml # Create X.509 certificate
│   ├── install_kibana.yml            # Install Kibana
│   ├── main.yml                      # Main playbook for this role
│   └── start_kibana_service.yml      # Start and enable Kibana service
├── templates
│   └── kibana.yml.j2                 # Kibana configuration template
└── vars
    └── main.yml                      # Variable definitions
```

## Role Variables

The role relies on specific variables for customization. Define these in `vars/main.yml` or your playbook as needed.

- **Kibana Paths and Certificates**:
  - `kibana_home_directory_path`: Base directory for Kibana data.
  - `kibana_certs_directory_path`: Directory for storing Kibana SSL certificates.
  - `kibana_ca_file_path`: Path to the Kibana CA certificate.
  - `kibana_private_key_file_path`: Path to the Kibana private key.
  - `kibana_crt_file_path`: Path to the Kibana SSL certificate.

- **SSL and Security**:
  - `es_ssl_certificate_path`: Elasticsearch SSL certificates location.
  - `kibana_certificate_country_name`, `kibana_certificate_organization_name`, etc.: Certificate details for Kibana's SSL certificate.

## Key Role Tags

Use the following tags to control which parts of the role are executed:

- `simple`: Runs basic Kibana configuration and setup.
- `cluster`: Enables multi-host clustered configuration.
- `new-node`: Configures Kibana for newly added nodes in the cluster.

## Tasks Overview

The role's main tasks cover:

1. **Installation**:
   - Installs Kibana from a specified local repository, primarily for hosts in the `BDA` group.

2. **Configuration**:
   - Configures `kibana.yml` based on a template with dynamic variables, supporting SSL and Fleet outputs.
   - Adds new hosts to `xpack.fleet.outputs.hosts` as needed for multi-host setups.

3. **SSL Certificate Management**:
   - Creates an X.509 certificate file, generates fingerprints, and manages Kibana's keystore for SSL and secure communication.

4. **Service Management**:
   - Starts, enables, and reloads Kibana and Nginx services based on configuration changes.

5. **Geo-IP Configuration**:
   - Sets up geo-IP databases for Kibana, copied to `BDA` hosts and served via Nginx.



## Usage Notes

- **Certificate Management**: Ensure that SSL certificate files are appropriately defined and secured, particularly in distributed or clustered environments.
- **Geo-IP Database Configuration**: Geo-IP database files are served via Nginx for access by Kibana. Verify that Nginx is properly installed and configured.
- **Role Compatibility**: This role assumes an existing Elastic Stack environment with defined host groups (e.g., `BDA`, `SF`, `HOT`). Adapt group names and variables based on your infrastructure.

## Handlers

The following handlers are triggered based on changes in configuration files or service needs:

- **Restart Kibana**: Restarts the Kibana service if any configuration files are modified.
- **Reload Nginx**: Reloads Nginx configuration to reflect changes in geo-IP or CA files.
- **Reload Systemd**: Reloads Systemd to pick up any new service configurations.

