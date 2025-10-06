
---

# Elasticsearch Integrations Server Ansible Role

This Ansible role installs and configures the Elasticsearch integrations server, including the deployment of Docker images and setting up the necessary directories and configurations for the integration.

## Role Overview

This role is responsible for:
1. **Creating directories** for the integration server and Docker cache.
2. **Copying and loading Docker images** for Elasticsearch integrations.
3. **Setting up Docker Compose** to launch the integration server.

The role is designed to work specifically with nodes in the `BDA` group.

## Role Structure

### 1. Directory Setup
- **Creates Cache and Integration Directories**:
  - Creates the `/var/cache/siem` directory to store the Docker image.
  - Creates the `/usr/share/siem/integration` directory to hold the Docker Compose file and related integration assets.

### 2. Docker Image Handling
- **Copies Docker Image**:
  - The Docker image (`distribution.tar.gz`) is copied from the `files/` directory to `/var/cache/siem/distribution.tar.gz`.
- **Loads Docker Image**:
  - The Docker image is loaded into the Docker engine using the `docker load` command.
- **Extracts Docker Image ID**:
  - After loading the image, the role extracts the image ID using a regular expression from the output of the `docker load` command.
- **Tags the Docker Image**:
  - The image is tagged with the specified name and tag defined in the variables (`integrations_server_image_name` and `integrations_server_image_tag`).

### 3. Docker Compose Configuration
- **Copies the Docker Compose File**:
  - A `docker-compose.yml` template is copied to the target system under `/usr/share/siem/integration/docker-compose.yml`.
- **Starts the Docker Containers**:
  - The role then runs `docker compose` to start the containers in detached mode (`-d`) using the generated Docker Compose file.

## Configuration File (`docker-compose.yml.j2`)

The `docker-compose.yml.j2` file is a Jinja2 template used to create the final `docker-compose.yml` on the target system. You should adjust this template according to the required services for the Elasticsearch integration.


**Key Variables in the Docker Compose Template:**
- **`integrations_server_image_name`**: The name of the Docker image to use.
- **`integrations_server_image_tag`**: The tag/version of the Docker image.
- **`ES_HOST`** and **`ES_PORT`**: The Elasticsearch host and port the integration server will connect to.

## Role Variables

The following variables can be customized in your playbook or inventory:

- **`integrations_server_image_name`**: The name of the Docker image to use for the integration server (default: `siem.apk-group.net/library/package-registry/distribution`).
- **`integrations_server_image_tag`**: The version tag of the Docker image.


## Role Execution Flow

1. **Create Directories**: The role ensures that the directories `/var/cache/siem` and `/usr/share/siem/integration` are created.
2. **Copy Docker Image**: The Docker image (`distribution.tar.gz`) is copied from the `files/` directory to the system.
3. **Load Docker Image**: The Docker image is loaded into the Docker engine using the `docker load` command.
4. **Tag Docker Image**: The loaded Docker image is tagged with the name and version defined in the variables.
5. **Deploy Docker Compose**: The `docker-compose.yml` file is generated and copied to the system, then used to launch the integration server containers.

## Tags

- `cluster`: Used when you want to apply the role to a cluster setup.
- `simple`: Used for a simpler, single-node deployment.

---