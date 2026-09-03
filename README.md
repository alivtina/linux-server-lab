# Linux Server Lab

Hands-on DevOps practice environment covering Linux administration, networking, Bash scripting, Python, Git/GitHub, Docker, CI/CD, and virtualization.

The project is built and tested on an Ubuntu Server virtual machine running on a QEMU/KVM host with Arch Linux.

## Skills Demonstrated

| Area            | Technologies / Skills                                                   |
| --------------- | ----------------------------------------------------------------------- |
| Linux           | Ubuntu Server, Arch Linux, CLI, package management, troubleshooting     |
| Networking      | TCP/IP, ports, localhost, NAT, SSH, `tcpdump`                           |
| Shell           | Bash scripting, ShellCheck, command-line automation                     |
| Programming     | Python, pytest                                                          |
| Version Control | Git, GitHub                                                             |
| Containers      | Docker, Docker Compose, Dockerfiles, non-root containers, health checks |
| CI/CD           | GitHub Actions, automated testing, Docker builds, artifacts, deployment |
| Virtualization  | QEMU/KVM, libvirt, virt-manager, VirtualBox                             |

## Repository Structure

```text
linux-server-lab/
├── .github/
│   └── workflows/
│       └── ci.yml
├── docker/
│   ├── app-demo/
│   ├── compose-demo/
│   ├── dockerfile-demo/
│   ├── website/
│   └── README.md
├── docs/
├── python/
│   └── system-health/
│       ├── Dockerfile
│       ├── README.md
│       ├── requirements.txt
│       └── system.py
├── scripts/
├── tests/
│   └── test_system_health.py
├── troubleshooting/
├── .dockerignore
├── .gitignore
└── README.md
```

## Linux Administration

The lab uses an Ubuntu Server virtual machine for practicing common Linux administration tasks.

Examples include:

* inspecting system information
* monitoring CPU, memory, and disk usage
* working with processes and services
* managing files and permissions
* package management
* troubleshooting system issues
* working with SSH
* investigating network connections

### System Information Script

`scripts/system-info.sh` reports:

* hostname
* operating system
* kernel version
* uptime
* available memory
* disk usage
* CPU core count

## Networking

Networking fundamentals were practiced using both the host system and virtual machines.

Topics include:

* TCP/IP
* IP addresses
* ports
* localhost
* NAT
* SSH
* client/server communication
* packet inspection with `tcpdump`

The networking exercises focus on understanding what happens when applications communicate over a network rather than only memorizing networking terminology.

## Bash

Bash is used for system administration and automation tasks.

The repository includes shell scripts for:

* system information
* health checks
* automated checks used by CI

Shell scripts are validated with ShellCheck in GitHub Actions.

## Python System Health CLI

`python/system-health/` contains a Python command-line application that reports basic system health information.

The application collects:

* hostname
* username
* CPU core count
* memory usage
* available memory
* disk usage
* available disk space

It supports both human-readable and JSON output.

Example:

```bash
python system.py
```

JSON output:

```bash
python system.py --json
```

The application also includes:

* logging
* usage threshold checks
* automated tests with pytest
* Docker containerization
* non-root container execution

### Testing

Python tests are located in:

```text
tests/test_system_health.py
```

The tests verify application behavior such as:

* resource usage status checks
* CPU core detection

Tests are executed locally with:

```bash
pytest
```

and automatically in GitHub Actions.

## Docker

The repository contains several Docker exercises progressing from basic Dockerfiles to multi-container applications.

### Dockerfile Demo

Basic Docker image building and container execution.

### Website

A simple containerized website used to practice:

* Dockerfiles
* port mapping
* container lifecycle
* HTTP access

### Compose Demo

A multi-container setup used to practice Docker Compose and service communication.

### Python System Health Container

The Python system health application is packaged as a Docker image.

The image:

* uses `python:3.12-slim`
* installs application dependencies
* runs as a non-root `appuser`
* executes the Python application as the container's main process

Example:

```bash
docker build -t system-health:dev python/system-health
docker run --rm system-health:dev
```

The application runs as a non-root user inside the container.

### Container Health Checks

The long-running HTTP application uses a Docker `HEALTHCHECK` to distinguish between a running container and a healthy application.

The Python system-health CLI does not use a Docker health check because it is a short-lived command-line application: it performs its check and exits.

## Git and GitHub

Git is used throughout the project to track changes and maintain the repository.

Typical workflow:

```bash
git status
git diff
git add
git commit
git push
```

The repository is hosted on GitHub and serves as a portfolio of practical DevOps work.

## CI/CD

GitHub Actions is used to automatically validate the project when changes are pushed or pull requests are created.

The CI pipeline currently performs:

1. ShellCheck validation
2. Bash tests
3. Python dependency installation
4. Python tests with pytest
5. Build artifact creation
6. Docker image build
7. Docker container execution
8. Application verification
9. Deployment to an Ubuntu Server self-hosted runner
10. Deployment verification

### Pipeline Overview

```text
Git push / Pull Request
          │
          ▼
    GitHub Actions
          │
          ├── ShellCheck
          │
          ├── Bash tests
          │
          ├── Python tests
          │
          ├── Build artifact
          │
          ├── Docker build
          │
          ├── Docker run
          │
          └── Deployment
                 │
                 ▼
          Ubuntu Server VM
                 │
                 ▼
       Deployment verification
```

The Docker CI job also verifies the containerized HTTP application using its health check and HTTP requests.

The Python system-health Docker image is independently built and executed in CI.

## Deployment

The CI pipeline creates a build artifact containing the shell scripts and deploys it to an Ubuntu Server virtual machine.

Deployment includes:

* downloading the CI artifact
* extracting the files
* setting executable permissions
* verifying that the expected scripts exist and are executable

The deployment environment is an Ubuntu Server VM running under QEMU/KVM.

## Virtualization

The lab environment uses:

* QEMU/KVM
* libvirt
* virt-manager
* Ubuntu Server virtual machines
* Arch Linux host

Virtualization is used to create an isolated environment for Linux administration, networking, CI/CD, and deployment practice.

## Troubleshooting

The `troubleshooting/` directory contains notes from problems encountered during the lab.

Examples include:

* networking issues
* Docker runtime problems
* file permission problems
* Python runtime issues
* CI/CD troubleshooting

The goal is to document not only successful configurations but also how problems were investigated and resolved.

## Current Focus

The project is being developed progressively toward practical junior DevOps skills.

Current areas include:

* Linux administration
* networking
* Bash
* Python
* Docker
* Git/GitHub
* GitHub Actions
* CI/CD
* virtualization

Planned areas include:

* AWS
* Infrastructure as Code with Terraform
* Kubernetes
* monitoring and logging
* DevOps security
* more realistic deployment projects

## Goal

The long-term goal of this lab is to develop practical skills required for junior DevOps, Cloud, Platform, and related infrastructure roles while building a portfolio of reproducible hands-on projects.

