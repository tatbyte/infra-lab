# Changelog

All notable changes to this project will be documented in this file.

## [1.4.0] - 2026-03-13
### Added
- Added `VM_CREATE_USER` to the Vagrant lab configuration so user creation, password SSH setup, and sudo provisioning can be enabled or skipped for fresh base-box testing.

### Changed
- Hardened the Vagrant provisioning script by escaping shell values before creating users or setting passwords.
- Increased Vagrant SSH startup tolerance with a longer boot timeout and explicit SSH connect timeout.

### Documentation
- Updated the Vagrant lab guide to explain when `VM_CREATE_USER` should be used and when a VM must be recreated to return to the base box state.
- Expanded the Vagrant README with clearer network design, access patterns, boot-time SSH behavior, and recommended workflow for Ansible-focused lab usage.

## [1.3.0] - 2026-02-27
### Changed
- Refactored Docker setup: reorganized directory structure, updated .gitignore, enhanced README, and improved gen_compose.py for secure and best-practice .env and secret management ([#5](https://github.com/tatbyte/infra-lab/issues/5)).

### Documentation
- Improved Docker lab documentation: clarified macvlan network limitations and SSH access from host, added instructions for adding temporary and persistent routes, and mentioned alternatives ([#7](https://github.com/tatbyte/infra-lab/issues/7)).

## [1.2.0] - 2026-02-26
### Changed
- Improved and clarified documentation for Vagrant and Docker lab setups ([#3](https://github.com/tatbyte/infra-lab/issues/3)).
- Updated all setup guides to reference correct filenames and step order.
- Added instructions for tagging and changelog updates.

## [1.1.0] - 2026-02-26
### Added
- Docker-based lab environment: Compose templates, generation script, and documentation for container-based testing and automation.
- New documentation: `docs/01-configure-docker-lab.md` for Docker setup.
- Updated main README to include Docker lab option and instructions.

## [1.0.0] - 2026-02-26 
### Added
- Vagrant-based lab environment: Vagrantfile, provisioning scripts, and documentation for VM-based testing and automation.
- Setup and usage guides for Vagrant lab.
