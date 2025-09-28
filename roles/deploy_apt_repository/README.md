---

# APT Repository Setup Role

This Ansible role sets up and configures a local APT repository on specified hosts within a cluster environment. The repository is hosted via Nginx and is available to other nodes in the network. This is particularly useful for environments needing a dedicated package repository for SIEM components and dependencies.

## Role Structure

```
├── files/                         # Contains necessary files (e.g., repository archives)
├── handlers/main.yml              # Contains Nginx handlers
├── meta/main.yml                  # Metadata about the role
├── tasks/                         # Task files for setting up and managing the repository
│   ├── config_hostfile.yml        # Configures hostnames for all nodes
│   ├── deploy_local_apt_repository.yml # Deploys the repository to the primary node
│   ├── install_local_repositories_dependencies.yml # Installs repository dependencies
│   ├── main.yml                   # Main task file orchestrating repository setup
│   └── setup_all_hosts_apt_repository.yml # Configures APT sources list on nodes
├── templates/sf_repository.conf.j2 # Nginx configuration template for the repository
└── vars/main.yml                  # Variable definitions
```

## Prerequisites

- Ensure Nginx is installed on target hosts.
- Define inventory groups correctly, particularly the `SF` group, as this group’s first host will act as the main repository server.

## Variables

The following variables can be customized in `vars/main.yml`:

- **`siem_files_home_directory`**: Directory where SIEM files are stored (`/var/siem` by default).
- **`repository_archive_file_name`**: Name of the repository archive (e.g., `repo.tar.gz`).
- **`local_repository_directory_path`**: Path to deploy the APT repository.
- **`apt_sources_list_file_path`**: Path to the system's APT sources list (`/etc/apt/sources.list` by default).
- **`main_repository_ip_address`**: IP address of the main repository server (first host in `SF` group).

## Tasks Overview

The main tasks in this role include:

1. **Configuring Hosts**: Ensures each host is added to `/etc/hosts` with its subdomain for easy access.
2. **Deploying APT Repository**: 
   - Prepares directories and extracts repository files on the primary host.
   - Configures Nginx to serve the repository files.
3. **Setting Up APT Sources on All Hosts**: 
   - Adds the repository’s URL to the APT sources list on each host.
   - Updates the APT cache to recognize the new repository.
4. **Installing Dependencies**: 
   - Copies and extracts dependency packages required for setting up the local repository.
5. **Managing APT Sources List**: 
   - Backs up and creates a new sources list, ensuring it contains the local repository.

## Tags

- `cluster`: Runs tasks for initial repository setup on the primary server.
- `new-node`: Runs tasks needed for setting up a new node within the cluster.
- `add-scanner`, `add-collector`: Configures specific types of nodes with repository sources.

## Handlers

The role includes the following handlers in `handlers/main.yml`:

- **`Start Nginx`**: Starts the Nginx service.
- **`Reload Nginx`**: Reloads Nginx configuration to apply any changes.
- **`Test Nginx`**: Tests the Nginx configuration for errors.