#!/bin/bash
# entrypoint.sh — creates the lab user at container startup using runtime env vars.
# DOCKER_USER and DOCKER_PASS are injected via env_file: .env in docker-compose.yml.
# No credentials are baked into the image.

set -e

DOCKER_USER="${DOCKER_USER:-admin}"
DOCKER_PASS="${DOCKER_PASS:-changeme}"

if ! id "$DOCKER_USER" &>/dev/null; then
    useradd -ms /bin/bash "$DOCKER_USER"
    echo "$DOCKER_USER:$DOCKER_PASS" | chpasswd
    mkdir -p /etc/sudoers.d
    echo "$DOCKER_USER ALL=(ALL) NOPASSWD:ALL" > "/etc/sudoers.d/$DOCKER_USER"
    chmod 440 "/etc/sudoers.d/$DOCKER_USER"
fi

exec /usr/sbin/sshd -D
