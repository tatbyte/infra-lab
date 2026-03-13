# Vagrant Directory – Overview and Usage

## Purpose

This directory contains configuration files for spinning up multiple virtual machines (VMs) using Vagrant and libvirt.

The primary goal is to create a reproducible lab environment for testing Ansible automation across several hosts in a way that feels closer to real infrastructure.

This lab is intentionally designed to provide:

- a **Vagrant/libvirt management network** for VM lifecycle and built-in Vagrant communication
- a **LAN-facing bridged network** so each VM has its own reachable IP for SSH, Ansible, Docker, reverse proxy testing, and multi-host lab scenarios

---

## What the Code Does

- Uses a `.env` file to define VM settings such as:
  - box
  - memory
  - CPUs
  - user
  - whether to manage that user
  - password
  - bridge interface
  - hostname-to-IP mapping

- The `Vagrantfile` reads these settings and provisions VMs with:
  - static LAN IPs for each VM
  - optional user management with password/sudo setup
  - bridged networking for direct LAN access
  - resource allocation (RAM and CPU)
  - automated SSH configuration for Ansible compatibility

- Keeps the default libvirt management path so Vagrant can still manage the VM lifecycle.

---

## Network Design

This lab uses **two different network paths** on purpose.

### 1. Vagrant/libvirt management network

This network is used internally by Vagrant for:

- detecting the VM IP
- waiting for SSH during boot
- `vagrant ssh`
- machine lifecycle operations

Example IP range:

- `192.168.121.x`

Typical access:

- `vagrant@192.168.121.x`

### 2. Bridged LAN network

This network is used for normal lab access and realistic host testing.

It gives each VM its own IP on the LAN so it can be used like a real host for:

- SSH from the host
- SSH from other machines
- Ansible inventory testing
- Docker and container testing
- reverse proxy testing
- multi-host communication

Example IP:

- `192.168.0.101`

Typical access:

- `admin@192.168.0.101`

---

## Why This Lab Uses a LAN IP Per Host

The LAN IP is kept on purpose because this lab is used for more than just `vagrant ssh`.

It allows each VM to behave like a real machine on the network, which is useful for:

- testing Ansible against realistic target IPs
- testing Docker containers that expose ports on each host
- testing hostname/IP-based services
- validating reverse proxy behavior
- accessing VMs over SSH from another machine
- simulating a small real network

This is why the bridged/static IP design should be kept.

---

## Typical Use Cases

- Testing Ansible playbooks and roles on multiple hosts
- Simulating a small network for development or CI
- Experimenting with network configurations and automation
- Learning and practicing infrastructure-as-code
- Testing Docker or other services on separate hosts with real LAN IPs

---

## What You Can Do With These VMs

- SSH into each VM using the credentials from `.env`
- Run Ansible playbooks targeting multiple hosts
- Install and test software as you would on real machines
- Experiment with networking, user management, and system configuration
- Test Docker containers and service exposure on distinct VM IPs

---

## How Access Works

In practice, the same VM may be reachable in two ways:

- through the libvirt management network for Vagrant
- through the bridged LAN IP for normal operator access

The actual LAN login depends on which user mode you selected in `.env`.

Examples:

    vagrant@192.168.121.x
    admin@192.168.0.101

Recommended usage:

- use **Vagrant** for VM lifecycle
- use the **LAN IP** for your real SSH work and Ansible testing

Example:

    ssh admin@192.168.0.101

---

## User Modes

The Vagrant lab supports three practical user modes.

### 1. Original Vagrant user

Use:

    VM_CREATE_USER=false

Behavior:

- leaves the base box user setup unchanged
- keeps the default Vagrant account and key-based access path
- best when you want the box exactly as provided upstream

Typical access:

    vagrant ssh node1

### 2. Original Vagrant user plus password SSH

Use:

    VM_CREATE_USER=true
    VM_USER=vagrant
    VM_PASS=vagrant

Behavior:

- keeps the existing `vagrant` user
- updates that user password
- grants sudo through the managed provisioning block
- enables password SSH for LAN access

Typical access:

    ssh vagrant@192.168.0.101

### 3. Fully new lab user

Use:

    VM_CREATE_USER=true
    VM_USER=admin
    VM_PASS=admin

Behavior:

- creates a separate lab user when it does not already exist
- sets that user password and sudo access
- enables password SSH for LAN access

Typical access:

    ssh admin@192.168.0.101

If you switch modes after a VM was already created, rebuild it:

    vagrant destroy -f
    vagrant up

---

## SSH / Boot Issue Encountered

A boot-time issue was observed where:

- `vagrant up` showed:
  - `Host unreachable`
  - `Connection refused`
- but the VM was actually booting and became reachable later with manual SSH

This happened even though:

- the `vagrant` user still existed
- the Vagrant private key matched the guest `authorized_keys`
- SSH configuration was valid
- the firewall allowed SSH
- manual SSH worked after boot

So the issue was **not** caused by a broken SSH key, deleted user, or invalid sshd configuration.

---

## Root Cause

The root cause was related to **boot timing with two network interfaces**.

The VM had:

- one NIC for libvirt/Vagrant management
- one NIC for bridged LAN access

During boot, `systemd-networkd-wait-online.service` delayed the system while waiting for the network to be considered fully online.

That delay caused a problem:

- Vagrant started trying SSH on the management IP early
- port 22 was not ready yet
- Vagrant saw repeated `Connection refused`

So the machine itself was fine, but Vagrant reached it before SSH was available.

---

## Current Mitigation

The current Vagrant configuration increases SSH startup tolerance:

- `config.vm.boot_timeout = 300`
- `config.ssh.connect_timeout = 30`

Why this helps:

- Vagrant waits longer for the guest to finish booting
- transient early boot `Connection refused` failures are less likely to abort `vagrant up`

---

## Why This Fix Is Acceptable Here

This lab is built for:

- fast VM creation
- SSH access
- Ansible testing
- Docker and service testing

It does **not** need to block boot waiting for every network interface to be declared fully online before the system continues.

For this use case, allowing a longer SSH startup window improves reliability without changing the base box boot services.

---

## Relationship With Ansible

This Vagrant lab is intended to support Ansible development and testing.

The general workflow is:

1. Use Vagrant to create the VM
2. Use the LAN IP to reach the VM like a real host
3. Test Ansible roles and playbooks safely before using them elsewhere

This makes the lab useful for validating things such as:

- bootstrap users
- SSH access
- base roles
- Docker hosts
- service exposure
- multi-host automation behavior

The extra network interface is part of that realism and should not be treated as accidental.

---

## Recommended Workflow

1. Copy `template.env` to `.env` and adjust settings as needed
2. Run `vagrant up` to start the lab
3. Use the LAN IP to SSH into the VM with the user mode you selected
4. Test Ansible playbooks, roles, Docker, or other tooling

Examples:

    vagrant up
    ssh admin@192.168.0.101

Use `vagrant ssh <hostname>` when you keep the original base-box user mode. For password-managed modes, the LAN IP is usually the preferred path.

---

## Extending the Lab

- Add more hosts by updating `VM_MAPPING` in `.env`
- Change the base box or resources for different OS or performance
- Customize provisioning scripts for more complex setups
- Integrate with other tools such as Docker or Kubernetes for hybrid testing

---

## Limitations of Virtual Machines

- Performance is lower than physical hardware, especially for CPU and disk-intensive tasks
- Access to hardware features such as GPU or USB devices is limited or unavailable
- Network behavior may differ from real-world production environments
- Not suitable for production workloads or high-availability testing
- Some advanced features such as nested virtualization may require extra configuration or may not work

---

## Helpful Commands

### Check Vagrant SSH config

    vagrant ssh-config

### Check guest IPs

    ip -br addr
    ip route

### Check SSH readiness in the guest

    sudo journalctl -b -u ssh --no-pager
    sudo ss -tlnp | grep ':22'

### Check boot delays

    systemd-analyze
    systemd-analyze blame | head -30

---

## Summary

This directory provides a reproducible Vagrant/libvirt VM lab for realistic Ansible and Docker testing.

The setup intentionally uses:

- a libvirt management NIC for Vagrant
- a bridged LAN NIC for realistic per-host access

The boot-time SSH issue was caused by delayed network readiness, not by broken Ansible logic or invalid SSH configuration.

The current mitigation is a longer Vagrant boot and SSH timeout, while the per-host LAN IP design remains in place for testing.

---

For more details, see the comments in `.env` and `Vagrantfile`.
