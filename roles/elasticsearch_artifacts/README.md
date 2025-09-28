# Nginx Artifact Server Configuration Ansible Role

This Ansible role configures Nginx to serve artifact files, sets up Nginx load balancing, and manages artifact directories on specific host groups (`LB`, `SF`, and `COLLECTOR`). The role ensures that artifacts are correctly set up and managed on various nodes within a clustered environment.

## Role Structure


1. **Cluster Mode Nginx Configuration**: Configures Nginx to serve artifact files in a load-balanced setup on hosts within the `LB` group.

    - **Task File**: `configure_nginx_to_server_artifacts_files_cluster.yml`
    - **Configuration**: Creates necessary directories, copies artifact files, and configures Nginx.
    - **Condition**: Runs only if the host belongs to the `LB` group.

2. **Simple Mode Nginx Configuration**: Configures Nginx to serve artifact files in a non-clustered mode for standalone hosts.

    - **Task File**: `configure_nginx_to_server_artifacts_files_simple.yml`
    - **Condition**: Runs if the host is in `SF` or `COLLECTOR` groups.

3. **Nginx Load Balancer for Fleet**: Sets up Nginx as a load balancer to manage fleet services in a clustered environment.

    - **Template**: `fleet-lb.conf.disable.j2` for load balancing configuration.


## Templates

- **`default.j2`**: Template for Nginx default site configuration.
- **`fleet-lb.conf.disable.j2`**: Template for configuring Nginx as a load balancer for fleet services.

## Variables

Define the following variables in `vars/main.yml`:
- **artifact_server_datastore_path**: Path where artifact files are stored.
- **artifact_server_nginx_config_file_name**: Filename for the Nginx configuration.
- **artifact_server_nginx_config_available_path**: Path to store the available configuration for Nginx.
- **artifact_server_nginx_config_enables_path**: Path to enable the Nginx configuration.
- **nginx_service_username**: Username for Nginx ownership.
- **nginx_service_groupname**: Group for Nginx ownership.

## Usage

Include this role in your playbook to automate the configuration of Nginx as an artifact server, load balancer, and artifact manager across different node types.
