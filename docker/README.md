# Docker Practice

Hands-on Docker lab built as part of the Linux Server Lab.

The examples demonstrate how to build, run, configure, network, and troubleshoot containers using Docker and Docker Compose.

## What This Lab Demonstrates

* Docker images and containers
* Container lifecycle and `docker exec`
* Dockerfiles and image layers
* Build cache and build context
* `.dockerignore`
* `CMD` and `ENTRYPOINT`
* Container networking and Docker DNS
* Port publishing
* Bind mounts and named volumes
* Environment variables
* Container healthchecks
* Running containers as a non-root user
* Docker Compose

## Projects

### 1. Containerized Python Application

**Directory:** [`app-demo/`](app-demo/)

A small Python HTTP application packaged into a Docker image.

The application demonstrates:

* Building a custom Docker image
* Copying application code into an image
* Publishing container ports
* Environment variables
* Running as a non-root user
* Docker `HEALTHCHECK`
* HTTP health endpoint

#### Build

```bash
cd app-demo
docker build -t app-demo .
```

#### Run

```bash
docker run -d \
  --name app-demo \
  -p 8080:8000 \
  -e APP_ENV=production \
  app-demo
```

#### Test

```bash
curl http://localhost:8080/
```

Expected:

```text
Hello from Docker! Environment: production
```

Healthcheck:

```bash
curl http://localhost:8080/health
```

Expected:

```text
OK
```

Check container health:

```bash
docker ps
```

The container should eventually show:

```text
(healthy)
```

Remove the container:

```bash
docker rm -f app-demo
```

#### Run with Docker Compose

The application can also be started using Docker Compose.

```bash
docker compose -f docker/app-demo/compose.yaml up -d
```

Check the service:

```bash
docker compose -f docker/app-demo/compose.yaml ps
```

Test the application:

```bash
curl http://localhost:8080/
```

Test the health endpoint:

```bash
curl http://localhost:8080/health
```

Stop the application:

```bash
docker compose -f docker/app-demo/compose.yaml down
```

The Compose configuration demonstrates:

* Building an image from a Dockerfile
* Port publishing
* Environment variable configuration
* Container restart policy
* Docker healthchecks
* Managing the application lifecycle with Docker Compose

---

### 2. Docker Compose Demo

**Directory:** [`compose-demo/`](compose-demo/)

A two-service Docker Compose environment consisting of:

* `web` — Nginx
* `app` — Alpine Linux

Both services are connected to the same Compose network.

```text
Host
  |
  | localhost:8080
  v
web (nginx)
  |
  | Docker Compose network
  | http://web
  v
app (alpine)
  |
  v
named volume
/data
```

The example demonstrates:

* Multiple containers managed with Compose
* Service-to-service communication
* Docker DNS / service discovery
* Port publishing
* Named volumes
* Environment variables
* Container lifecycle with Compose

#### Start

From the repository root:

```bash
docker compose -f docker/compose-demo/compose.yaml up -d
```

Check the services:

```bash
docker compose -f docker/compose-demo/compose.yaml ps
```

Test access from the host:

```bash
curl http://localhost:8080
```

Test communication between containers:

```bash
docker compose -f docker/compose-demo/compose.yaml exec app wget -qO- http://web
```

Stop the services:

```bash
docker compose -f docker/compose-demo/compose.yaml down
```

The named volume remains after `down` unless `-v` is used.

---

### 3. Dockerfile Examples

**Directory:** [`dockerfile-demo/`](dockerfile-demo/)

Small Dockerfiles used to practice individual Dockerfile instructions and image-building concepts.

Examples include:

* `FROM`
* `RUN`
* `COPY`
* `CMD`
* `ENTRYPOINT`
* Image layers
* Build cache
* Build context

#### Example: package a Bash script into an image

`Dockerfile.copy` packages the existing `system-info.sh` script from the repository into an Ubuntu-based image.

Build from the repository root:

```bash
docker build \
  -f docker/dockerfile-demo/Dockerfile.copy \
  -t system-info-demo:v1 .
```

Run:

```bash
docker run --rm system-info-demo:v1
```

The container executes the system information script and displays information such as the hostname, kernel, memory, disk usage, IP address, and CPU count.

---

### 4. Website Bind Mount

**Directory:** [`website/`](website/)

A minimal HTML page used to demonstrate Docker bind mounts.

A bind mount maps a directory or file from the host into a container.

This allows changes made on the host to be immediately visible inside the container without rebuilding the image.

## Key Concepts Practiced

| Concept               | Demonstrated in               |
| --------------------- | ----------------------------- |
| Images and containers | All examples                  |
| Dockerfiles           | `dockerfile-demo`, `app-demo` |
| Build cache           | `dockerfile-demo`             |
| Build context         | `dockerfile-demo`             |
| `.dockerignore`       | `app-demo`                    |
| Port publishing       | `app-demo`, `compose-demo`    |
| Container networking  | `compose-demo`                |
| Docker DNS            | `compose-demo`                |
| Named volumes         | `compose-demo`                |
| Bind mounts           | `website`                     |
| Environment variables | `app-demo`, `compose-demo`    |
| Healthchecks          | `app-demo`                    |
| Non-root containers   | `app-demo`                    |
| Docker Compose        | `app-demo`, `compose-demo`    |

## Learning Outcome

After completing these exercises, I can independently:

* Build a Docker image from a Dockerfile
* Run and manage containers
* Publish container ports
* Pass configuration through environment variables
* Persist data with Docker volumes
* Connect containers through Docker networks
* Use Docker Compose to manage services
* Debug basic container networking problems
* Add and verify container healthchecks
* Run an application container as a non-root user
* Inspect images, containers, networks, and volumes
* Test containerized applications from the host and between containers
* Automate Docker image builds and application tests with GitHub Actions
