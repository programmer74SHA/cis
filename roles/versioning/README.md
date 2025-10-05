# SIEM Setup Information and SSH Banner Configuration Ansible Role

This Ansible role creates SIEM setup information files and configures an SSH banner to be displayed on login. The role is designed to ensure the proper setup of SIEM directories, generate setup information files, and apply a security banner to SSH configurations.

## Role Structure

1. **Generate Setup Information** (`tasks/generate_setupinfo.yml`): Creates the SIEM directory, if it doesn't exist, and generates a setup information file from a template.

    - **Files and Variables**:
      - **Template**: `setupinfo.j2` is used to generate the setup information file.
      - **Path**: Generated setup information is saved to `/etc/siem/setupinfo`.
      - **Condition**: Only runs on hosts in the `BDA` group.
      - **Tags**: `simple` and `cluster` for selective execution.

2. **SSH Banner Configuration** (`tasks/ssh_banner.yml`): Configures an SSH banner by copying a banner template and updating SSH configurations to display the banner on login.

    - **Files and Variables**:
      - **Template**: `siem_sshd_banner.j2` provides the text for the SSH banner.
      - **Configuration**: Updates `/etc/ssh/sshd_config` to point to the banner file.
      - **Validation**: Uses `sshd` validation to ensure configuration syntax is correct.
      - **Service**: Restarts SSH to apply the banner configuration.

## Templates

- **`setupinfo.j2`**: Template for the setup information file, providing details relevant to SIEM setup.
- **`siem_sshd_banner.j2`**: Template for the SSH login banner, typically used to display security notices.
