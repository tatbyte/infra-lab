# Infra-Lab – Project Overview

## Project Goal

The primary purpose of this repository is to provide a virtual lab environment for testing Ansible roles and playbooks on multiple hosts before deploying them to real machines. This helps ensure your automation works as expected in a safe, reproducible setting.

## What You Can Do With This Setup

- Test and develop Ansible roles, playbooks, and inventory files across several VMs or containers
- Simulate a multi-host network for infrastructure automation
- Experiment with system configuration, networking, and user management
- Practice infrastructure-as-code workflows
- Try out new software or scripts in a controlled environment
- Use the lab for CI/CD pipelines or integration testing
- Extend the setup for other tools (e.g., Docker, Kubernetes, custom scripts)

## Structure

- `vagrant/` – Vagrant configuration and environment files for VM setup
- `docker/` – Docker Compose configuration and scripts for container-based lab setup
- `docs/` – Guides and documentation for configuring and using the lab


## Getting Started


Refer to the documentation in the `docs/` directory for detailed setup instructions:

1. For Vagrant installation, see: `docs/00-vagrant-installation.md`
2. For Vagrant-based VM lab setup, see: `docs/01-configure-vagrant-lab.md`
3. For Docker-based container lab setup, see: `docs/02-configure-docker-lab.md`

After following the relevant setup guide, use the VMs or containers to test Ansible or other automation tools. Adjust the configuration as needed for your use case.

---

This lab is ideal for anyone wanting to safely test infrastructure changes, automation, or new software before applying them to production systems. You can choose between a Vagrant-based VM lab or a Docker-based container lab, depending on your needs and available resources.
