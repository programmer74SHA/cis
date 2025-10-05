---

# Pre-Checks Role

## Overview
The `pre_checks` role is designed to validate essential conditions before executing the main playbook tasks. This role performs checks on user privileges, required group configurations, and specific cluster node requirements. By ensuring all preconditions are met, it prevents unintended issues during deployment, particularly in clustered environments.


## Role Tasks

1. **Root User Validation**:
   - Ensures the playbook is executed by the `root` user.
   - Stops execution if not running with appropriate privileges.

2. **Cluster Role and Group Validation**:
   - Confirms necessary groups (e.g., `HOT`, `FROZEN`, `SF`, etc.) are present.
   - Checks load-balancer (`LB`) group and ensures proper configurations for `SF` nodes.

3. **System Configuration Updates**:
   - Configures system kernel parameters (e.g., disabling IPv6 and adjusting memory settings).

## File Structure
```
roles/pre_checks/
├── README.md                # Role documentation
├── handlers/
│   └── main.yml             # Reloads system configuration changes
├── tasks/
│   ├── check_root_user.yml  # Validates user privileges
│   ├── main.yml             # Entry point for all pre-checks
│   ├── role_checking.yml    # Validates group configurations and roles
│   └── sysctl_config.yml    # Configures system kernel parameters
├── templates/
│   └── sysctl.conf.j2       # Template for sysctl configuration
└── vars/
    └── main.yml             # Role-specific variables
```

### Task Descriptions

- **`main.yml`**: Entry point for the role, which calls individual tasks for role validation and root user checks.
- **`check_root_user.yml`**: Confirms the playbook is running as root, with a `meta: end_play` action if it isn’t.
- **`role_checking.yml`**: 
  - Checks the LB group for hosts.
  - Ensures at least two hosts are present in the SF group when LB group has hosts.
  - Verifies required groups (`HOT`, `FROZEN`, `COLD`, `WARM`, `SF`, `BDA`, `NBA`, `SCANNER`, `ELASTICSEARCH`, `LB`) are present, ending the play if any are missing.
- **`sysctl_config.yml`**:
  - Deploys kernel parameter configurations using a Jinja2 template (`sysctl.conf.j2`).


