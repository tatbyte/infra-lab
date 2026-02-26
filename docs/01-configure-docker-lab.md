# 01 – Configuring the Docker Lab Setup

This guide explains how to configure the Docker-based lab environment, access the containers from other PCs on the same network, and optionally SSH into the containers from the host machine.

---

## 1. Prepare the Environment

### a. Install Required Software
- Docker
- Docker Compose (v2 or later)
- Python 3 (for generating the compose file)

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
  - VM_IMAGE: Docker image name (e.g., ubuntu:22.04)
  - VM_MEMORY: RAM allocated to each container (in MB, e.g., 2048)
  - VM_CPUS: Number of CPUs allocated to each container (e.g., 2)
  - VM_USER: Username to create in each container (e.g., admin)
  - VM_PASS: Password for the created user (e.g., admin)
  - BRIDGE_IF: Host network interface to bridge for container LAN access (e.g., eth0)

### b. Generate the Compose File
- Run the script to generate `docker-compose.yml`:
  ```sh
  python3 gen_compose.py
  ```

---

## 3. Launch the Lab

- Start the containers:
  ```sh
  docker compose up -d
  ```
- Containers will be provisioned with static IPs and bridged networking.

---

## 4. Accessing Containers from Other PCs on the Same Network

### a. Ensure Host Network Configuration
- The host's LAN interface (e.g., eno1) must be connected to the same network as other PCs.
- Containers will have IPs in the LAN range (e.g., 192.168.0.101).

### b. Verify Connectivity
- From another PC, ping a container's IP:
  ```sh
  ping 192.168.0.101
  ```
- SSH into the container:
  ```sh
  ssh admin@192.168.0.101
  # Password: admin (or as set in .env)
  ```

---

## 5. Optionally: SSH from the Host Machine

You can SSH directly from the host to any container:
  ```sh
  ssh admin@192.168.0.101
  ```

### Configure SSH Access Without Password

If you want passwordless SSH access from the host:

1. Generate an SSH key on the host (if you don't have one):
   ```sh
   ssh-keygen -t ed25519 -C "user@example.com"
   # Press Enter to accept defaults
   ```

2. Copy your public key to each container:
   ```sh
   ssh-copy-id admin@192.168.0.101
   ssh-copy-id admin@192.168.0.102
   # Enter the password as set in .env (e.g., admin)
   ```

3. Now you can SSH without a password:
   ```sh
   ssh admin@192.168.0.101
   ```

Or use Docker's exec:
  ```sh
  docker exec -it <container> bash
  ```

---

## 6. Troubleshooting

- If you cannot access containers from other PCs:
  - Check that the host firewall allows traffic to/from the container IPs.
  - Ensure the bridge interface is correctly configured.
  - Verify containers are running and have the expected IPs.
  - Remember that systemd is not fully supported in containers by default; some services may not work as expected.

---

## Summary

1. Install dependencies and clone the project.
2. Configure `.env` for your network and container needs.
3. Generate the compose file and launch the lab with `docker compose up -d`.
4. Access containers from other PCs or the host using SSH.

For advanced networking or persistent routes, see the main documentation.
