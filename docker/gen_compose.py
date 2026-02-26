#!/usr/bin/env python3
import os
import yaml

# Read .env file
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

# Parse node entries (NODE1, NODE2, ...)
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
            'context': '.',
            'args': {
                'DOCKER_USER': env.get('DOCKER_USER', 'admin'),
                'DOCKER_PASS': env.get('DOCKER_PASS', 'admin')
            }
        },
        'container_name': node['name'],
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

# Output docker-compose.yml
output_path = os.path.join(os.path.dirname(__file__), 'docker-compose.yml')
with open(output_path, 'w') as f:
    yaml.safe_dump(compose, f, default_flow_style=False, sort_keys=False)

print(f"Generated {output_path} with {len(nodes)} node(s).")
