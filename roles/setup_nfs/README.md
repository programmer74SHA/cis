
# NFS Setup & Configuration Role

This Ansible role installs, configures, and manages an **NFS server** on the **BDA node** and mounts the exported NFS share on **DATA-NODES**.
It ensures the NFS server is properly set up, exports are configured, services are restarted, and clients can access the shared directory seamlessly.

---


## Role Variables


| Variable                 | Description                               | Default Value    |
| ------------------------ | ----------------------------------------- | ---------------- |
| `NFS_SERVER_DIRECTORY`   | Directory that nfs data saves on that   | `/var/nfs/siem` |
| `NFS_CONFIGURATION_PATH` | Path to the NFS exports configuration     | `/etc/exports`   |
| `NFS_CLIENT_MOUNT_POINT` | Directory on clients where NFS is mounted | `/nfs/seim`      |


---

## Tasks Overview

This role performs the following actions:

### **On the NFS Server (BDA):**

1. Installs the **nfs-kernel-server** package.
2. Creates the export directory.
3. Configures the NFS export file using a Jinja2 template.
4. Restarts and enables the NFS service.

### **On the NFS Clients (DATA-NODES):**

1. Installs the **nfs-common** package.
2. Creates a local mount directory.
3. Mounts the exported NFS share automatically.

---

## Dependencies

This role has **no external role dependencies**.