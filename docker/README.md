# Docker Directory – Overview and Usage

## Purpose

This directory contains configuration files for spinning up a multi-container lab environment using Docker Compose. The primary goal is to create a reproducible setup for testing Ansible automation, networking, and service orchestration across several containers.

## What the Code Does

- Uses a `.env` file to define container settings (image, memory, CPUs, user, password, network, and hostname-to-IP mapping).
- The `docker-compose.yml` (generated from `docker-compose.yml.template` and `gen_compose.py`) provisions containers with:
  - Static LAN IPs for each container
  - Custom user creation and SSH password setup
  - Bridged networking for direct LAN access
  - Resource allocation (RAM, CPU)
  - Automated SSH configuration for Ansible compatibility

## Typical Use Cases

- Testing Ansible playbooks and roles on multiple hosts
- Simulating a small network for development or CI
- Experimenting with network configurations and automation
- Learning and practicing infrastructure-as-code

## What You Can Do With These Containers

- SSH into each container using the credentials from `.env`
- Run Ansible playbooks targeting multiple hosts
- Install and test software as you would on real machines
- Experiment with networking, user management, and system configuration

## Limitations of Containers

- Performance is lower than physical hardware (especially for CPU and disk-intensive tasks)
- Access to hardware features (e.g., GPU, USB devices) is limited or unavailable
- Network behavior may differ from real-world setups (e.g., latency, broadcast)
- Not suitable for production workloads or high-availability testing
- Some advanced features (like nested virtualization) may require extra configuration or may not work
- Systemd is not fully supported inside containers by default, which may limit the ability to run services that depend on it or require a full init system.

## Extending the Lab

- Add more containers by updating the `VM_MAPPING` in `.env` and regenerating the compose file
- Change the base image or resources for different OS or performance
- Customize provisioning scripts for more complex setups
- Integrate with other tools (e.g., Vagrant, Kubernetes) for hybrid testing

## Getting Started

1. Copy `template.env` to `.env` and adjust settings as needed.
2. Run `python3 gen_compose.py` to generate `docker-compose.yml` from the template.
3. Run `docker compose up -d --build` to start the lab.
4. Use `docker exec -it <container>` or SSH directly to each container.
5. Test your Ansible playbooks or other automation tools.

---

For more details, see the comments in `.env`, `docker-compose.yml.template`, and `gen_compose.py`.
