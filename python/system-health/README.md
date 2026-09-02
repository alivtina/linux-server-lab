# Python System Health CLI

A small Python command-line utility that reports basic system health information.

## What it does

The script collects:

* Hostname
* Username
* Number of CPU cores
* Memory usage
* Available memory
* Disk usage
* Available disk space

It compares memory and disk usage against a configurable threshold and reports `OK` or `WARNING`.

The CLI supports two output modes:

* Human-readable output
* JSON output for automation and other tools

## Technologies

* Python
* psutil
* Linux
* JSON

## Run

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Human-readable output

```bash
python system.py
```

Example:

```text
System Health
-------------
Hostname: HAL
User: aalivtina
CPU cores: 16
Memory usage: 91.0% [WARNING]
Memory available: 1.03 GB
Disk usage: 39.4% [OK]
Disk free: 56.30 GB
```

### JSON output

Use `--json` to output system information as JSON:

```bash
python system.py --json
```

Example:

```json
{
    "hostname": "HAL",
    "username": "aalivtina",
    "cpu_cores": 16,
    "memory_percent": 91.0,
    "memory_available_gb": 1.03,
    "disk_percent": 39.4,
    "disk_free_gb": 56.30,
    "memory_status": "WARNING",
    "disk_status": "OK"
}
```

JSON output can be consumed by other scripts, automation tools, monitoring systems, or APIs.

## Skills demonstrated

* Python functions
* Dictionaries
* Conditional logic
* Command-line arguments
* JSON serialization
* Modules and imports
* System information retrieval
* Basic health checks
* Formatted output
