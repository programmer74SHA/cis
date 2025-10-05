# SIEM ELK V8.X Installer

## Table of Contents

- [SIEM ELK V8.X Installer](#siem-elk-v8x-installer)
  - [Table of Contents](#table-of-contents)
    - [Configure Deploy Environment](#configure-deploy-environment)
    - [Install Ansible and their Dependencies](#install-ansible-and-their-dependencies)
    - [Run Ansible playbook](#run-ansible-playbook)
    - [Adding a New Node to the Cluster](#adding-a-new-node-to-the-cluster)
    - [Adding a Scanner Node to the Cluster](#adding-a-scanner-node-to-the-cluster)
    - [Adding a Zone-Collector Node to the Elasticsearch Cluster](#adding-a-zone-collector-node-to-the-elasticsearch-cluster)
    - [Configure NTP Server \& Clients](#configure-ntp-server--clients)
      - [How It Works](#how-it-works)
      - [Steps](#steps)
    - [Inventory glossary](#inventory-glossary)
      - [Sample Inventory files](#sample-inventory-files)
      - [Inventory Parameters](#inventory-parameters)
    - [Flexible Rule Feature](#flexible-rule-feature)
    - [Mixed-Node Feature](#mixed-node-feature)
      - [Example Inventory File](#example-inventory-file)
      - [Steps for Versioning](#steps-for-versioning)
    - [Update existing installation](#update-existing-installation)
      - [Prerequisites for Updates](#prerequisites-for-updates)
      - [Running an Update](#running-an-update)
      - [Update Process Features](#update-process-features)

> **You need to run the installer on BDA**

### Configure Deploy Environment

Before proceeding, you need to configure the `inventory.ini` file. This file stores server details. To fill this file and understand which variables you need to add for each host and view a sample file, refer to the [inventory glossary](#inventory-glossary) section in this document. This step is crucial as subsequent installation steps rely on the `inventory` data to perform their tasks.

### Install Ansible and their Dependencies

The Ansible installer includes a `install` shell script that installs Ansible and its dependencies from local file storage. After extracting this **Installer** on the deployer server, ensure the `install` script has executable permissions by running the following command in your terminal:

```bash
chmod +x install
```

To start installing dependencies, execute the script:

```bash
./install
```

This script installs all necessary Ansible dependencies and establishes a stable connection using the data configured in the previous step.

### Run Ansible playbook

Once the `install` script completes its tasks, you can execute the Ansible playbook to initiate the main installation process. You must specify exactly one of the following tags when running the command:

- `--tags "cluster"`: Use this tag to deploy the cluster configuration.
- `--tags "simple"`: Use this tag to deploy a simple configuration.

Run the following command with your chosen tag:

```bash
ansible-playbook -i inventory.ini main-playbook.yml --tags "cluster"
```

Replace `"cluster"` with `"simple"` if deploying the simple configuration.

Where `main-playbook.yml` integrates our developed Ansible roles. Ansible processes these roles sequentially, executing their tasks. After the playbook finishes, you can access ELK8 via your web browser.

### Adding a New Node to the Cluster

If you need to add a new node to your Elasticsearch cluster, you can use the `new-node` tag in the Ansible playbook. For example, if you want to add a new node with the `cold` role, follow these steps:

1. **Update the Inventory File**:  
   Edit your `inventory.ini` file and add the new host under the appropriate group. For instance, to add a node with the `cold` role, update the `cold` group in your inventory:

   ```ini
   [COLD]
   COLD1
   COLD2  # Add your new node here
   ```

2. **Run the Playbook with the `new-node` Tag**:  
   After updating the inventory, run the following command to add the new host to your Elasticsearch cluster:

   ```bash
   ansible-playbook -i inventory.ini main-playbook.yml --tags "new-node"
   ```

This command will execute the necessary tasks to integrate the new host with the specified role into your existing Elasticsearch cluster.

### Adding a Scanner Node to the Cluster

To add a scanner node to the current Elasticsearch cluster, follow these steps:

1. **Update the Inventory File**:  
   Edit your `inventory.ini` file and add the new scanner node under the `[SCANNER]` group. For example:

   ```ini
   # Sample Inventory File Update

   [SCANNER]
   SCANNER1  # Add your new scanner node here
   ```

2. **Run the Playbook with the `add-scanner` Tag**:  
   After updating the inventory file, run the Ansible playbook to integrate the new scanner node into your cluster. Use the `add-scanner` tag:

   ```bash
   ansible-playbook -i inventory.ini main-playbook.yml --tags "add-scanner"
   ```

This command will execute the necessary tasks to add the scanner node to the cluster and configure it appropriately. Make sure the `inventory.ini` file includes all the required parameters for the new scanner node, such as `ansible_host`, `ansible_user`, and other relevant settings.


### Adding a Zone-Collector Node to the Elasticsearch Cluster

To add a **zone-collector node** to your current Elasticsearch cluster, follow these steps:

1. **Update the Inventory File**:  
   Open your `inventory.ini` file and add the new collector node under the `[COLLECTOR]` group. Here’s an example of what the updated inventory might look like:

   ```ini
   # Sample Inventory File Update

   [COLLECTOR]
   COLLECTOR1  # Add your new collector node here
   ```

2. **Run the Playbook with the `add-collector` Tag**:  
   After updating the inventory file, run the Ansible playbook to integrate the new collector node into your cluster. Use the `add-collector` tag:

   ```bash
   ansible-playbook -i inventory.ini main-playbook.yml --tags "add-collector"
   ```

3. **Combine the Collector Node with NBA Node** (Optional):  
   If you’d like the collector node to serve as an NBA node as well, add it to both the `[COLLECTOR]` and `[NBA]` groups in the inventory file:

   ```ini
   # Sample Inventory File with Combined Roles

   [COLLECTOR]
   COLLECTOR1  # Collector node

   [NBA]
   COLLECTOR1  # Same node included as NBA
   ```

This configuration allows the **collector node** to act as both a collector and an NBA node within the cluster.

### Configure NTP Server & Clients

The installer automatically configures **Chrony** for time synchronization across all nodes. This ensures consistent timestamps across the entire SIEM cluster.

#### How It Works

* The **BDA node** acts as the **NTP server** by default.
* All other nodes act as **NTP clients**.
* Secure synchronization is enforced using **Chrony authentication keys**.
* You can optionally configure external NTP servers.

#### Steps

1. **Define External NTP Servers** *(Optional)*
   In your `inventory.ini`, set the `ntp_servers` variable:

   ```ini
   ntp_servers=0.pool.ntp.org,1.pool.ntp.org,2.pool.ntp.org
   ```

   If `ntp_servers` is **not defined**, the BDA node synchronizes internally and clients sync with it.

2. **Run the Installer**
   The `setup_ntp_server` role runs automatically during installation:

   ```bash
   ansible-playbook -i inventory.ini main-playbook.yml --tags "cluster"
   ```

3. **Verify Synchronization**
   After deployment, you can check Chrony status:

   ```bash
   chronyc tracking
   chronyc sources -v
   ```

### Inventory glossary

The inventory file contains essential host information required for deployment. Below, we detail the variables each host needs. Refer to the provided `inventory.ini` template and add your host's data accordingly.

#### Sample Inventory files

The inventory file is in an INI-like format. It lists servers sequentially:

```ini
# Sample Inventory File
BDA_1
SF_1
```

You can also group servers:

```ini
# Sample Inventory File
[BDA]
BDA_1
...

[SF]
SF_1
...
```

#### Inventory Parameters

Here are key Ansible Inventory parameters:

| Example            | Description                                                                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| ansible_host       | Host address (IPv4, IPv6, or DNS). Use `host_ip_or_nameserver` for connecting to another host or `localhost` if Ansible runs on the host. |
| ansible_user       | Host username used by Ansible to connect and execute tasks.                                                                               |
| ansible_ssh_pass   | Host username password for Ansible authentication.                                                                                        |
| ansible_connection | Type of connection used by Ansible (`local` for `localhost`, `ssh` for remote servers).                                                   |

### Flexible Rule Feature

The installer  supports  flexible rule feature, allowing the Elasticsearch cluster setup to be performed with or without a load balancer (LB) host. This update ensures that the installation can proceed regardless of whether an LB host is included.


---

### Mixed-Node Feature

The mixed-node feature allows a single host to belong to multiple groups, enabling more flexible role assignments. For instance, a host such as `hot2` can be part of both the `hot` and `warm` groups, allowing it to handle roles associated with both groups. This flexibility is useful for scenarios where resources need to be dynamically allocated or when nodes need to fulfill multiple roles.

#### Example Inventory File

Here’s a sample inventory file demonstrating how a host can be included in multiple groups:

```ini
# Sample Inventory File

[HOT]
HOT1
HOT2  # Included in both HOT and WARM groups

[WARM]
WARM1
HOT2  # Included in both HOT and WARM groups

[COLD]
COLD1
...

[FROZEN]
FROZEN1
...
```

In this example:
- `HOT1` is exclusively part of the `HOT` group.
- `HOT2` is part of both the `HOT` and `WARM` groups.
- `WARM1` is exclusively part of the `WARM` group.
- `COLD1` and `FROZEN1` are part of their respective groups.

This configuration allows `HOT2` to handle roles from both `HOT` and `WARM` groups, demonstrating how mixed-node setups can enhance the flexibility of your infrastructure.
#### Steps for Versioning

The version number is controlled using the `siem_version` variable, which is set in the `Makefile` and propagated throughout the relevant files (such as `local_repository.json`, `install`, and `inventory.ini`).

Here’s how the versioning mechanism works:

1. **Define Version in Makefile**:
   The version of the SIEM is defined in the `Makefile` using a variable `siem_version`, which will be used across various scripts and configuration files.

   ```makefile
   siem_version=7.3.0
   ```

2. **Automated Version Update**:
   The `update_version` target in the `Makefile` updates the version number in the following files:
   - `install` script
   - `local_repository.json` file
   - `inventory.ini` file

   These files are essential for ensuring that the correct version number is applied across all stages of the installation process.

### Update existing installation

The installer now supports in-place updates of existing ELK deployments, allowing you to upgrade your stack without requiring a complete reinstallation. This feature provides zero-downtime rolling updates with automatic configuration preservation.

#### Prerequisites for Updates

- Existing SIEM ELK installation (compatible base version)
- All cluster nodes must be in healthy state (green or yellow status)
- Sufficient disk space for temporary backups
- Network connectivity to updated package repositories

#### Running an Update

To update an existing installation, use the `update` tag with your current inventory configuration:

```bash
ansible-playbook -i inventory.ini main-playbook.yml --tags "update"
```

#### Update Process Features

**Rolling Updates**: Elasticsearch nodes are updated sequentially to maintain cluster availability:
1. Frozen nodes → Cold nodes → Warm nodes → Hot nodes → SF nodes → BDA node
2. Shard allocation is temporarily disabled during each node update
3. Machine learning jobs are paused and resumed automatically
4. Cluster health is verified before proceeding to the next node

**Component Updates**: The update process handles:
- **Elasticsearch**: Rolling updates with shard management and ML job handling
- **Kibana**: Plugin management, configuration backup/restore, data preservation  
- **Logstash**: Configuration and data directory preservation
- **Docker Services**: Updated image versions for Maps Server, Fleet Server, Integration Server
