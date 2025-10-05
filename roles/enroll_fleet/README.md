---

# Copy Fleet Server and Elastic Agent Setup Role

This Ansible role configures and deploys the Elastic Agent and Fleet Server for ELK, specifically for the `SF` and `COLLECTOR` groups. It includes generating and managing Elasticsearch service tokens, creating Docker images, and setting up a Fleet Server Docker container with required configurations.

## Role Tasks Overview

- **Token Management**: Verifies and manages Elasticsearch service tokens for the Fleet Server.
- **Docker Image Handling**: Loads and tags the Elastic Agent Docker image for Fleet Server.
- **Configuration Setup**: Creates directories and renders the `docker-compose.yml` template file with dynamic variables for Fleet Server configuration.


## Variables

These are defined in `defaults/main.yml`:

- **docker_image_name**: The name of the Docker image for the Elastic Agent.
- **docker_image_tag**: The tag (version) of the Docker image.

## Role Structure and Tasks

```yaml
- name: Run on SF group only
  # Manages Elasticsearch service tokens and generates Fleet Server configurations

- name: load the elastic-agent docker image
  # Loads, tags, and prepares the Elastic Agent Docker image for deployment
```

## Role Workflow

1. **Token Management** (SF group only):
   - Creates necessary directories for the Fleet Server Docker Compose files.
   - Retrieves and checks the existence of the Elasticsearch service token.
   - If a token already exists, it deletes it before creating a new one.
   - Extracts the token and sets it as `es_service_token_fleet`.
   - Extracts the `ca_trusted_fingerprint` from `kibana.yml` for Fleet Server.

2. **Docker Image Handling** (SF and COLLECTOR groups):
   - Creates a directory for Fleet Server Docker images.
   - Copies and loads the `elastic-agent.tar.gz` Docker image file.
   - Tags the Docker image with the specified `docker_image_name` and `docker_image_tag`.

3. **Configuration Setup**:
   - Renders the `docker-compose.yml` file using the `docker-compose.yml.j2` template.
   - Sets up the Fleet Server container using the dynamically generated `docker-compose.yml`.

## Template Configuration (`docker-compose.yml.j2`)

The `docker-compose.yml` template is configured with the following parameters:
- **FLEET_SERVER_SERVICE_TOKEN**: Set to `es_service_token_fleet`, generated dynamically.
- **FLEET_SERVER_ELASTICSEARCH_CA_TRUSTED_FINGERPRINT**: Dynamically fetched `cert_fingerprint`.
- **Other Environmental Variables**: Uses the host IP for the Elasticsearch host.

### Example of `docker-compose.yml`

```yaml
version: "3"
services:
  fleet_server:
    image: "{{ docker_image_name }}:{{ docker_image_tag }}"
    container_name: "elastic_fleet_server"
    ...
    ports:
      - 8222:8222
```

## Tags

- **`simple`**: Applies to both main tasks for token management and Docker image loading.
- **`add-collector`**: Specifically applies the Docker image loading block to hosts in `COLLECTOR` group.

