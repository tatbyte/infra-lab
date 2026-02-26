FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y sudo ufw openssh-server iproute2 iputils-ping vim curl \
    apt-transport-https ca-certificates gnupg lsb-release software-properties-common \
    locales \
    && apt-get clean

ARG DOCKER_USER
ARG DOCKER_PASS
RUN useradd -ms /bin/bash $DOCKER_USER && \
    echo "$DOCKER_USER:$DOCKER_PASS" | chpasswd && \
    echo "$DOCKER_USER ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Enable SSH password authentication
RUN sed -i 's/^#\?PasswordAuthentication .*/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/^#\?PermitRootLogin .*/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN mkdir -p /var/run/sshd

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
