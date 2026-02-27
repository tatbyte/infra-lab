FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y sudo ufw openssh-server iproute2 iputils-ping vim curl \
    apt-transport-https ca-certificates gnupg lsb-release software-properties-common \
    locales \
    && apt-get clean

# Enable SSH password authentication
RUN sed -i 's/^#\?PasswordAuthentication .*/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/^#\?PermitRootLogin .*/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN mkdir -p /var/run/sshd

# User creation happens at container startup via entrypoint.sh,
# reading DOCKER_USER and DOCKER_PASS from the runtime environment (.env).
# Build context is docker/ so the path is relative to that root.
COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 22

ENTRYPOINT ["/entrypoint.sh"]
