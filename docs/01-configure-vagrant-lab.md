# 01 – Configuring the Vagrant Lab Setup

This guide explains how to configure the Vagrant lab environment, access the virtual machines (VMs) from other PCs on the same network, and optionally SSH into the VMs from the host machine.

---

## 1. Prepare the Environment

### a. Install Required Software
- Vagrant
- libvirt and related packages (e.g., `virt-manager`, `vagrant-libvirt`)

### b. Clone or Copy the Project
- Place the project directory on your host machine.

---

## 2. Configure the Lab

### a. Set Up the .env File
- Copy `template.env` to `.env`:
  ```sh
  cp template.env .env
  ```
Edit `.env` to define:
  - VM_MAPPING: Comma-separated list of hostname:IP pairs (e.g., node1:192.168.0.101,node2:192.168.0.102)
  - VM_BOX: Vagrant box name (e.g., generic/ubuntu2204)
  - VM_MEMORY: RAM allocated to each VM (in MB, e.g., 2048)
  - VM_CPUS: Number of CPUs allocated to each VM (e.g., 2)
  - VM_USER: Username to create in each VM (e.g., admin)
  - VM_PASS: Password for the created user (e.g., admin)
  - BRIDGE_IF: Host network interface to bridge for VM LAN access (e.g., eth0)

### b. Check Network Interface
- Ensure `BRIDGE_IF` matches your host's LAN interface.
- Use `ip a` or `nmcli device status` to find the correct interface.

---

## 3. Launch the Lab

- Start the VMs:
  ```sh
  vagrant up
  ```
- VMs will be provisioned with static IPs and bridged networking.

---

## 4. Accessing VMs from Other PCs on the Same Network

### a. Ensure Host Network Configuration
- The host's LAN interface (e.g., eno1) must be connected to the same network as other PCs.
- VMs will have IPs in the LAN range (e.g., 192.168.0.101).

### b. Verify Connectivity
- From another PC, ping a VM's IP:
  ```sh
  ping 192.168.0.101
  ```
- SSH into the VM:
  ```sh
  ssh admin@192.168.0.101
  # Password: admin (or as set in .env)
  ```

---

## 5. Optionally: SSH from the Host Machine


You can SSH directly from the host to any VM:
  ```sh
  ssh tatbyte@192.168.0.101
  ```

### Configure SSH Access Without Vagrant

If you want passwordless SSH access from the host (without using `vagrant ssh`):

1. Generate an SSH key on the host (if you don't have one):
  Run the following command and press Enter to accept defaults:
  ssh-keygen -t ed25519 -C "user@example.com"

2. Copy your public key to each VM:
  ```sh
  ssh-copy-id admin@192.168.0.101
  ssh-copy-id admin@192.168.0.102
  # Enter the password as set in .env (e.g., admin)
  ```

3. Now you can SSH without a password:
  ```sh
  ssh admin@192.168.0.101
  ```

This allows you to use Ansible or other tools from the host without needing to use `vagrant ssh` or enter passwords.

Or use Vagrant's built-in SSH:
  ```sh
  vagrant ssh node1
  ```

---

## 6. Troubleshooting

- If you cannot access VMs from other PCs:
  - Check that the host firewall allows traffic to/from the VM IPs.
  - Ensure the bridge interface is correctly configured.
  - Verify VMs are running and have the expected IPs.

---

## Summary

1. Install dependencies and clone the project.
2. Configure `.env` for your network and VM needs.
3. Launch the lab with `vagrant up`.
4. Access VMs from other PCs or the host using SSH.

For advanced networking or persistent routes, see the main documentation.
