You can either use anisble playbook or docker compose file to deploy "docker-challenge-solved-mohit-arora" container and wrapper container.

Ansible way:
version: ansible 2.10.8

Command to execute:
ansible-playbook hive-playbook.yaml

Docker Compose way:
version v2.29.2-desktop.2

Command to execute:
docker compose up -d