# Logstash Configuration Ansible Role

This Ansible role installs and configures Logstash on specific hosts (usually `SF` and `COLLECTOR` nodes). It handles the creation of necessary directories, API key generation for secure access to Elasticsearch, and manages the Logstash service.

## Role Structure


1. **Directory and Certificate Setup**:
    - Ensures required directories for Logstash certificates are created with correct permissions.
    - Copies CA certificate files for SSL connections with Elasticsearch.

2. **Elasticsearch API Key Generation**:
    - Generates a secure API key with specific roles and permissions needed for Logstash to interact with Elasticsearch clusters.
    - Sets the generated API key as a fact to be used in Logstash configuration.

3. **Logstash Configuration**:
    - Configures Logstash using a template file (`logstash.yml.j2`) that incorporates the generated API key for seamless and secure communication with Elasticsearch.

4. **Logstash Installation and Service Management**:
    - Installs Logstash on `SF` and `COLLECTOR` nodes, if not already present.
    - Ensures that the Logstash service is started and enabled for automatic startup.
