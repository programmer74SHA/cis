---

# Elastic Maps Server Role

This Ansible role sets up and configures the Elastic Maps Server on specified hosts in the cluster. The Elastic Maps Server, running as a Docker container, is configured to interact with Elasticsearch and Kibana securely, using SSL certificates and Docker Compose.

## Role Structure

```
├── files/                                 # Directory for additional files
├── meta/
│   └── main.yml                           # Role metadata
├── tasks/
│   └── main.yml                           # Main tasks for setting up Elastic Maps Server
├── templates/
│   ├── docker-compose.yml.j2              # Docker Compose template for Elastic Maps Server
│   └── elastic-maps-server.yml.j2         # Elastic Maps Server config template
└── vars/
    └── main.yml                           # Default variables
```


## Variables

The following variables in `vars/main.yml` can be customized:

- **`kibana_home_directory_path`**: Home directory path for Kibana (`/var/lib/kibana` by default).
- **`elastic_certs_directory_path`**: Directory path for Elasticsearch and Kibana certificates.
- **`elastic_ca_filename`**: Filename for the Elasticsearch CA certificate.
- **`ems_docker_image_name`**: Docker image name for the Elastic Maps Server.
- **`ems_docker_image_tag`**: Tag for the Docker image version of the Elastic Maps Server.

## Tasks Overview

The main tasks in this role include:

1. **Create Required Directories**:
   - Creates necessary directories for caching and storing the Elastic Maps Server configuration and certificates.

2. **Copy and Load Docker Image**:
   - Copies the Elastic Maps Server Docker image from the Ansible controller to the target host.
   - Loads the Docker image on the target server.

3. **Tag Docker Image**:
   - Tags the loaded image with the appropriate repository and version for use in Docker Compose.

4. **Configure Elastic Maps Server**:
   - Copies `docker-compose.yml` and `elastic-maps-server.yml` templates to the configuration directory.
   - Populates configuration files with the correct server addresses, SSL certificates, and Elasticsearch connection details.

5. **Copy Certificates**:
   - Copies the CA certificate, Kibana private key, and certificate files to the target location for secure SSL communication.

6. **Set Ownership of Certificates**:
   - Changes ownership of the certificate files to be accessible by the Docker container running as a specific user (`1000:1000`).

7. **Start Elastic Maps Server**:
   - Starts the Elastic Maps Server using Docker Compose, ensuring it runs as a background service.

## Templates

- **`docker-compose.yml.j2`**: Defines the Docker Compose configuration for the Elastic Maps Server, including ports, volumes, and health checks.
- **`elastic-maps-server.yml.j2`**: Configures Elastic Maps Server to connect to Elasticsearch securely, with SSL settings and credentials.

