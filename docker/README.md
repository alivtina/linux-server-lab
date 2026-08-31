# Docker Practice

This directory contains hands-on Docker exercises completed as part of the Linux Server Lab.

## Topics Covered

* Docker images and containers
* Container lifecycle
* `docker run`, `docker start`, and `docker exec`
* Container networking
* Docker bridge networks
* Docker DNS and service discovery
* Port publishing
* Named volumes and persistent data
* Bind mounts
* Dockerfiles
* Image layers and build cache
* Build context and `.dockerignore`
* `CMD` and `ENTRYPOINT`
* Docker Compose
* Environment variables

## Docker Compose Demo

The `compose-demo` directory contains a two-service Docker Compose environment.

```text
Host
  |
  | localhost:8080
  v
web (nginx)
  |
  | Docker internal network
  | http://web
  v
app (Alpine)
  |
  v
named volume (/data)
```

The `web` service is accessible from the host through port `8080`.

The `app` service can communicate with `web` using the Docker Compose service name:

```text
http://web
```

Docker's internal DNS resolves the service name to the container's current IP address.

### Run the demo

```bash
cd compose-demo
docker compose up -d
```

Check the running services:

```bash
docker compose ps
```

Test communication between the containers:

```bash
docker compose exec app wget -qO- http://web
```

Test access from the host:

```bash
curl http://localhost:8080
```

Stop and remove the containers:

```bash
docker compose down
```

The named volume is preserved unless `-v` is used.

## Dockerfile Examples

The `dockerfile-demo` directory contains examples demonstrating:

* `FROM`
* `RUN`
* `COPY`
* `CMD`
* `ENTRYPOINT`
* Docker image layers
* Docker build cache
* Build context

One example packages the existing `system-info.sh` script into a Docker image.

Build it from the repository root:

```bash
docker build \
  -f docker/dockerfile-demo/Dockerfile.copy \
  -t system-info-demo .
```

Run it:

```bash
docker run --rm system-info-demo
```

## Website Bind Mount

The `website` directory contains a simple HTML file used to demonstrate Docker bind mounts.

A bind mount allows a container to access a file or directory directly from the host.

Changes made to the mounted file on the host are immediately visible inside the container.

