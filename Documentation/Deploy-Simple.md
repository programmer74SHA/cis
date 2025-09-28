

1. Edit `inventory.ini` 
2. Install Ansible useing ./install.sh.
3. Run the main-playbook.yml with  tag: `cluster` or `simple`.

---

## 1) Edit `inventory.ini`

### Required inventory fields per host

* `ansible_host`: IP of hosy skip if using `ansible_connection=local`.
* `ansible_user`: SSH username.
* `ansible_ssh_pass`: SSH password
* `ansible_connection`: use `local` for the BDA host, `ssh` for remote hosts.

---

## 2) Install Ansible and dependencies

```bash
./install
```
This sets up Ansible and checks connectivity using  `inventory.ini`.
---

## 3) Run the main installation

Choose **one** tag:

* `cluster`
* `simple`

Run:

```bash
ansible-playbook -i inventory.ini main-playbook.yml --tags "cluster"
```

---


# important
1. The NBA node Must have minmum 2 netwwork insterfaces
2. The interface of NBA must be Set in Inventory
