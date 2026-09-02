# Linux Server Lab

Hands-on Linux and DevOps lab for building practical system administration, scripting, containerization, networking, and automation skills.

The repository documents exercises and small projects built while progressing from Linux administration toward DevOps engineering.

## Projects

### Docker Practice

Hands-on Docker exercises covering:

- Docker images and containers
- Dockerfiles and image layers
- Build cache and build context
- `.dockerignore`
- Container networking and DNS
- Port publishing
- Bind mounts and named volumes
- Docker Compose
- Environment variables
- Container healthchecks
- Non-root containers

**Examples:**

- [Docker practice](docker/README.md)
- [Compose demo](docker/compose-demo/)
- [Dockerfile examples](docker/dockerfile-demo/)
- [Containerized Python application](docker/app-demo/)

### Linux Administration

Practical exercises covering:

- Linux filesystem
- Users and groups
- Permissions
- Processes and services
- SSH
- Networking
- Package management
- System monitoring
- Bash scripting
- Troubleshooting

### Automation & CI

The repository also contains Bash scripts and GitHub Actions workflows used to automate checks and validate the project.

## Skills Demonstrated

| Area | Technologies / Skills |
|---|---|
| Operating systems | Linux, Ubuntu Server |
| Shell | Bash, command line |
| Version control | Git, GitHub |
| Containers | Docker, Docker Compose |
| Networking | TCP/IP fundamentals, container networking, DNS |
| Automation | Bash, GitHub Actions |
| Virtualization | QEMU/KVM, libvirt |

## Environment

- **Host:** Arch Linux
- **Server:** Ubuntu Server
- **Virtualization:** QEMU/KVM + libvirt
- **Tools:** Git, Docker, Bash

## Repository Structure

```text
linux-server-lab/
├── .github/
│   └── workflows/
├── docker/
├── python/
│   └── system-health/
├── scripts/
├── tests/
├── troubleshooting/
├── .dockerignore
├── .gitignore
└── README.md
