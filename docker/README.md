# Docker Directory – Overview and Usage

## Purpose

This directory contains configuration files for spinning up a multi-container lab environment using Docker Compose. The primary goal is to create a reproducible setup for testing Ansible automation, networking, and service orchestration across several containers.

## Directory Structure

```
docker/
├── compose/
│   └── docker-compose.yml       # Generated — do not edit by hand
├── images/
│   └── base/
│       └── Dockerfile           # Base image for all lab containers
├── scripts/
│   └── entrypoint.sh            # Creates the lab user at container startup
├── gen_compose.py               # Reads .env and generates compose/docker-compose.yml
├── docker-compose.yml.template  # Reference example of the generated compose format
├── template.env                 # Example .env — copy to .env and customise
└── README.md
```

## What the Code Does

- Uses a `.env` file (in `docker/`) to define node names, IPs, credentials, and network settings.
- `gen_compose.py` reads `.env` and generates `compose/docker-compose.yml` with all values resolved — no `${VAR}` placeholders are used.
- Each container is built from `images/base/Dockerfile`, which installs common packages and copies the entrypoint script.
- `scripts/entrypoint.sh` creates the lab user at container startup using `DOCKER_USER` and `DOCKER_PASS` from the environment — credentials are never baked into the image.
- Containers are given static IPs on a macvlan network for direct LAN access.

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

- Add more containers by adding `NODE<n>=name:ip` entries in `.env` and regenerating the compose file
- Change the base image or resources in `images/base/Dockerfile`
- Customise `scripts/entrypoint.sh` for more complex provisioning
- Integrate with other tools (e.g., Vagrant, Kubernetes) for hybrid testing

## Getting Started

1. Copy `template.env` to `.env` and adjust settings as needed:
   ```sh
   cp template.env .env
   ```
2. Run `gen_compose.py` to generate the compose file:
   ```sh
   python3 gen_compose.py
   ```
3. Start the lab:
   ```sh
   cd compose
   docker compose up -d --build
   ```
4. Use `docker exec -it <container> bash` or SSH directly to each container.
5. Test your Ansible playbooks or other automation tools.

---

For more details, see the comments in `.env`, `docker-compose.yml.template`, and `gen_compose.py`.
