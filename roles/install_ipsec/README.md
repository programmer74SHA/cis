
---

# IPsec Installer Role

This Ansible role installs and configures IPsec-related components, including the necessary certificates, Kibana plugins, and related softwares.

## Overview

This role performs the following tasks:

- **Generates a Certificate Authority (CA)** and ensures the necessary directory structure is in place.
- **Installs IPsec-related packages**, including `siem-ipsec-manager` and `strongswan`.
- **Installs Kibana plugins** from `.zip` files present in the `files/` directory.

## Role Variables

- **cert_dest_dir**: Directory where certificates are stored (default: `/etc/siem/certs`).
- **CA_dest**: Location where the CA certificate will be copied (default: `{{ cert_dest_dir }}/SIEM-CA.crt`).
- **cert_dir**: Directory containing the CA certificate (default: `/etc/elasticsearch/certs`).

## Role Execution Flow


1. **Install IPsec Packages**: The role installs `siem-ipsec-manager` and `strongswan` using the `apt` module.
2. **Create Kibana Plugins Cache**: It ensures the cache directory for Kibana plugins exists.
3. **Copy and Install Kibana Plugins**: It will copy `.zip` files found in the `files/` directory to the Kibana plugins cache and install them.
4. **Display Installation Results**: It outputs the results of the Kibana plugin installation for review.

## Tags

- `cluster`: Used when you want to apply the role to a cluster setup.
- `simple`: Used for a simpler, single-node installation.
