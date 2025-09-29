# Kafka Configuration Ansible Role

This Ansible role installs and configures Kafka tools (`kaf` and `kafka-topics`) on specified hosts. It also copies essential configuration files for managing Kafka topics, specifically within `SF` or `COLLECTOR` group nodes. 

## Role Structure


1. **Copy Kafka Binaries**:
    - Copies the `kaf` binary to `/usr/bin/kaf` with executable permissions (`0755`).
    - Copies the `kafka-topics` binary to `/usr/bin/kafka-topics`, also with executable permissions.

2. **Configure Kafka Settings**:
    - Copies `kaf-config` to `/root/kaf-config` for use with the `kaf` CLI.
    - This config file specifies Kafka settings such as `brokers`, `SASL`, `TLS`, and other connection details.

### Configuration File (`kaf-config`)

The `kaf-config` file defines essential configurations for connecting to Kafka brokers:
- **`current-cluster`**: Name of the current cluster (e.g., `local`).
- **`brokers`**: Lists Kafka broker addresses (e.g., `127.0.0.1:9094`).
- **SASL and TLS settings**: Allows further security configurations if needed.

### Example `kaf-config` File

```yaml
current-cluster: local
clusteroverride: ""
clusters:
  - name: local
    version: ""
    brokers:
      - 127.0.0.1:9094
    SASL: null
    TLS: null
    security-protocol: ""
    schema-registry-url: ""
    schema-registry-credentials: null
```