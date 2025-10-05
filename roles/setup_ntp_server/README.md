# NTP Server & Client Setup Role

This Ansible role installs, configures, and manages **Chrony** for time synchronization across all servers.
It sets up the **BDA node** as the **NTP server** and configures all other nodes (**DATA-NODES**) as **NTP clients**.
It ensures secure and consistent time synchronization across the entire cluster using authentication keys.

---

## Role Variables

| Variable               | Description                                                                                        | Default Value             |
| ---------------------- | -------------------------------------------------------------------------------------------------- | ------------------------- |
| `ntp_servers`          | Comma-separated list of external NTP servers. If empty, the BDA node acts as the main time source. | `""`                      |
| `chrony_path`          | Path to the Chrony configuration directory.                                                        | `/etc/chrony`             |
| `chrony_service`       | Name of the Chrony service.                                                                        | `chrony`                  |
| `ntp_service`          | Name of the legacy NTP service (disabled by this role).                                            | `ntp`                     |
| `chrony_logdir`        | Directory where Chrony logs are stored.                                                            | `/var/log/chrony/`        |
| `chrony_key_id`        | Chrony authentication key ID used for secure synchronization.                                      | `85`                      |
| `chrony_key_file_path` | Path to the Chrony authentication key file.                                                        | `/etc/chrony/chrony.keys` |

You can define `ntp_servers` in **inventory.ini**:

```ini
ntp_servers=0.pool.ntp.org,1.pool.ntp.org,2.pool.ntp.org
```

---

## Tasks Overview

This role performs the following actions:

### **On the NTP Server (BDA):**

1. Installs the **Chrony** package.
2. Disables any running **ntpd** service to avoid conflicts.
3. Generates a secure Chrony authentication key.
4. Configures the **Chrony server** using a Jinja2 template (`server.conf.j2`).
5. Enables and starts the Chrony service.
6. Restarts Chrony automatically when the configuration changes.

---

### **On the NTP Clients (DATA-NODES):**

1. Installs the **Chrony** package.
2. Fetches the authentication key from the NTP server.
3. Configures the **Chrony client** using a Jinja2 template (`clients.conf.j2`).
4. Enables and starts the Chrony service.
5. Restarts Chrony automatically when the configuration changes.

---

## Dependencies

This role has **no external role dependencies**.
