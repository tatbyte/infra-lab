# Vagrant Directory – Overview and Usage

## Purpose

This directory contains configuration files for spinning up multiple virtual machines (VMs) using Vagrant and libvirt. The primary goal is to create a reproducible lab environment for testing Ansible automation across several hosts.

## What the Code Does

- Uses a `.env` file to define VM settings (box, memory, CPUs, user, password, network interface, and hostname-to-IP mapping).
- The `Vagrantfile` reads these settings and provisions VMs with:
  - Static LAN IPs for each VM
  - Custom user creation and SSH password setup
  - Bridged networking for direct LAN access
  - Resource allocation (RAM, CPU)
  - Automated SSH configuration for Ansible compatibility

## Typical Use Cases

- Testing Ansible playbooks and roles on multiple hosts
- Simulating a small network for development or CI
- Experimenting with network configurations and automation
- Learning and practicing infrastructure-as-code

## What You Can Do With These VMs

- SSH into each VM using the credentials from `.env`
- Run Ansible playbooks targeting multiple hosts
- Install and test software as you would on real machines
- Experiment with networking, user management, and system configuration

## Limitations of Virtual Machines

- Performance is lower than physical hardware (especially for CPU and disk-intensive tasks)
- Access to hardware features (e.g., GPU, USB devices) is limited or unavailable
- Network behavior may differ from real-world setups (e.g., latency, broadcast)
- Not suitable for production workloads or high-availability testing
- Some advanced features (like nested virtualization) may require extra configuration or may not work

## Extending the Lab

- Add more hosts by updating the `VM_MAPPING` in `.env`
- Change the base box or resources for different OS or performance
- Customize provisioning scripts for more complex setups
- Integrate with other tools (e.g., Docker, Kubernetes) for hybrid testing

## Getting Started

1. Copy `template.env` to `.env` and adjust settings as needed.
2. Run `vagrant up` to start the lab.
3. Use `vagrant ssh <hostname>` or SSH directly to each VM.
4. Test your Ansible playbooks or other automation tools.

---

For more details, see the comments in `.env` and `Vagrantfile`.
