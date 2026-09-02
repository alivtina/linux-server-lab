import os
import psutil


def get_hostname():
    return os.uname().nodename


def get_cpu_cores():
    return os.cpu_count()


def get_memory():
    return psutil.virtual_memory()


def get_disk_usage():
    return psutil.disk_usage("/")


def get_system_info():
    memory = get_memory()
    disk = get_disk_usage()

    system = {
        "hostname": get_hostname(),
        "cpu_cores": get_cpu_cores(),
        "memory_percent": memory.percent,
        "disk_percent": disk.percent,
        "disk_free_gb": disk.free / (1024 ** 3),
    }

    return system


def check_usage(percent, threshold):
    if percent > threshold:
        return "WARNING"
    else:
        return "OK"


def main():
    threshold = 80

    system = get_system_info()

    results = {
        "memory": check_usage(system["memory_percent"], threshold),
    }

    try:
        results["disk"] = check_usage(system["disk_percent"], threshold)
    except KeyError:
        print("Disk information unavailable")

    print("System Health")
    print("-------------")
    print(f"Hostname: {system['hostname']}")
    print(f"CPU cores: {system['cpu_cores']}")
    print(f"Memory: {system['memory_percent']}% [{results['memory']}]")

    disk_status = results.get("disk")

    if disk_status:
        print(f"Disk: {system['disk_percent']}% [{disk_status}]")
        print(f"Disk free: {system['disk_free_gb']:.2f} GB")


if __name__ == "__main__":
    main()
