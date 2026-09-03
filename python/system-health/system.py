import sys
import json
import os
import logging
import psutil
import getpass

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="system-health.log"
)

logger = logging.getLogger(__name__)


def get_hostname():
    return os.uname().nodename


def get_username():
    return getpass.getuser()


def get_cpu_cores():
    return os.cpu_count()


def get_memory():
    return psutil.virtual_memory()


def get_disk_usage():
    return psutil.disk_usage("/")


def check_usage(percent, threshold):
    if percent > threshold:
        return "WARNING"
    return "OK"


def main():
    threshold = 80

    logger.info("System health check started")

    hostname = get_hostname()
    username = get_username()
    cpu_cores = get_cpu_cores()

    memory = get_memory()
    memory_gb = memory.available / (1024 ** 3)

    disk_usage = get_disk_usage()
    disk_free_gb = disk_usage.free / (1024 ** 3)

    system = {
        "hostname": hostname,
        "username": username,
        "cpu_cores": cpu_cores,
        "memory_percent": memory.percent,
        "memory_available_gb": memory_gb,
        "disk_percent": disk_usage.percent,
        "disk_free_gb": disk_free_gb,
    }

    memory_status = check_usage(system["memory_percent"], threshold)
    disk_status = check_usage(system["disk_percent"], threshold)

    if memory_status == "WARNING":
        logger.warning(
            "Memory usage: %.1f%% [%s]",
            system["memory_percent"],
            memory_status
        )
    else:
        logger.info(
            "Memory usage: %.1f%% [%s]",
            system["memory_percent"],
            memory_status
        )

    if disk_status == "WARNING":
        logger.warning(
            "Disk usage: %.1f%% [%s]",
            system["disk_percent"],
            disk_status
        )
    else:
        logger.info(
            "Disk usage: %.1f%% [%s]",
            system["disk_percent"],
            disk_status
        )

    system["memory_status"] = memory_status
    system["disk_status"] = disk_status

    if "--json" in sys.argv:
        print(json.dumps(system, indent=4))
    else:
        print("System Health")
        print("-------------")
        print(f"Hostname: {system['hostname']}")
        print(f"User: {system['username']}")
        print(f"CPU cores: {system['cpu_cores']}")
        print(f"Memory usage: {system['memory_percent']}% [{system['memory_status']}]")
        print(f"Memory available: {system['memory_available_gb']:.2f} GB")
        print(f"Disk usage: {system['disk_percent']}% [{system['disk_status']}]")
        print(f"Disk free: {system['disk_free_gb']:.2f} GB")

    logger.info("System health check completed")

if __name__ == "__main__":
    main()
