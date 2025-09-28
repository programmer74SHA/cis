# Elasticsearch and Load Balancer Installation Identification Ansible Role

This Ansible role is designed to ensure that it only runs on hosts designated for Elasticsearch, verifying if Elasticsearch is already installed, and identifying if new load balancer nodes are present by checking specific directories.

## Role Structure

1. **Identify New Hosts** (`tasks/identify_new_hosts.yml`): Ensures this role is run only on hosts in the `ELASTICSEARCH` group, checks for Elasticsearch installation, and sets a fact if installation is needed.

    - **Files and Variables**:
        - **Task**: Checks for the presence of Elasticsearch binaries and service configuration.
        - **Fact**: `install_needed` is set to `true` if Elasticsearch is not installed.
        - **Tag**: `new-node` for selective playbook runs.

2. **Identify New Load Balancer Nodes** (`tasks/identify_new_lb.yml`): Checks if a specific directory (`/var/www/elastic`) exists to determine if this host is a new load balancer.

    - **Files and Variables**:
        - **Directory**: `/var/www/elastic` is checked for existence.
        - **Fact**: `is_new_lb` is set to `true` if the directory does not exist, indicating a new load balancer.

