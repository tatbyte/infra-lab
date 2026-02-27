#!/usr/bin/env python3
import os
import yaml

# Read .env file to discover node definitions and network settings.
# All values are resolved at generation time and written directly into
# docker-compose.yml — no ${VAR} placeholders are used, because Docker
# Compose only resolves variables from an .env in the compose file's own
# directory, not from env_file (which is container-only).
env_path = os.path.join(os.path.dirname(__file__), '.env')
env = {}
with open(env_path) as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if '=' in line:
            k, v = line.split('=', 1)
            env[k.strip()] = v.strip()

# Parse node entries (NODE1, NODE2, ...) — format: NODE<n>=name:ip
# Extracts both name and IP from a single definition to avoid duplication.
nodes = []
for i in range(1, 10):  # Support up to 9 nodes
    node_key = f'NODE{i}'
    if node_key in env:
        name_ip = env[node_key].split(':', 1)
        if len(name_ip) == 2:
            nodes.append({
                'name': name_ip[0],
                'ip': name_ip[1]
            })

services = {}
for node in nodes:
    services[node['name']] = {
        'build': {
            # context is docker/ (parent of compose/), dockerfile relative to it
            'context': '..',
            'dockerfile': 'images/base/Dockerfile',
        },
        'container_name': node['name'],
        # Credentials are injected at runtime from .env — no build args.
        # Path is relative to the compose file location (compose/)
        'env_file': ['../.env'],
        'tty': True,
        'stdin_open': True,
        'networks': {
            'lab_macvlan': {
                'ipv4_address': node['ip']
            }
        },
        'restart': 'unless-stopped'
    }

compose = {
    'services': services,
    'networks': {
        'lab_macvlan': {
            'driver': 'macvlan',
            'driver_opts': {
                'parent': env.get('MACVLAN_PARENT', 'eth0')
            },
            'ipam': {
                'config': [
                    {
                        'subnet': env.get('SUBNET', '192.168.0.0/24'),
                        'gateway': env.get('GATEWAY', '192.168.0.1')
                    }
                ]
            }
        }
    }
}

# Output compose/docker-compose.yml
output_path = os.path.join(os.path.dirname(__file__), 'compose', 'docker-compose.yml')
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w') as f:
    yaml.safe_dump(compose, f, default_flow_style=False, sort_keys=False)

print(f"Generated {output_path} with {len(nodes)} node(s).")
print("Remember: copy template.env -> .env and fill in your values before running docker compose.")
