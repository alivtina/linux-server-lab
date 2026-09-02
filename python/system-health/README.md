# Python System Health CLI

A small Python command-line utility that reports basic system health information.

## What it does

The script collects:

- Hostname
- Number of CPU cores
- Memory usage
- Disk usage
- Available disk space

It compares memory and disk usage against a configurable threshold and reports `OK` or `WARNING`.

## Technologies

- Python
- psutil
- Linux

## Run

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
