# Infra-Lab – Project Overview

## Project Goal

The primary purpose of this repository is to provide a virtual lab environment for testing Ansible roles and playbooks on multiple hosts before deploying them to real machines. This helps ensure your automation works as expected in a safe, reproducible setting.

## What You Can Do With This Setup

- Test and develop Ansible roles, playbooks, and inventory files across several VMs
- Simulate a multi-host network for infrastructure automation
- Experiment with system configuration, networking, and user management
- Practice infrastructure-as-code workflows
- Try out new software or scripts in a controlled environment
- Use the lab for CI/CD pipelines or integration testing
- Extend the setup for other tools (e.g., Docker, Kubernetes, custom scripts)

## Structure

- `vagrant/` – Vagrant configuration and environment files for VM setup
- `docs/` – Guides and documentation for configuring and using the lab

## Getting Started

1. Follow the instructions in `docs/01-configure-lab.md` to set up your environment.
2. Use the VMs to test Ansible or other automation tools.
3. Adjust the configuration as needed for your use case.

---

This lab is ideal for anyone wanting to safely test infrastructure changes, automation, or new software before applying them to production systems.
