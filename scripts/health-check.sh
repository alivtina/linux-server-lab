#!/bin/bash

exit_code=0

# --- Functions ---

check_disk_usage() {
    disk=$1

    if [ "$disk" -lt 80 ]; then
        echo "[PASS] Root filesystem usage: ${disk}%"
	return 0
    elif [ "$disk" -lt 90 ]; then
        echo "[WARN] Root filesystem usage: ${disk}%"
	return 0
    else
        echo "[FAIL] Root filesystem usage: ${disk}%"
	return 1
    fi
}

# --- Main program ---

if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then

    echo "=== Server Health Check ==="

    # --- SSH Service Check ---
    if systemctl is-active --quiet ssh; then
        echo "[PASS] SSH service is running"
    else
        echo "[FAIL] SSH service is not running"
        exit_code=1
    fi

    # --- Disk Usage Check ---
    disk=$(df -h / | awk 'NR==2 {print $5}' | tr -d '%')
    if ! check_disk_usage "$disk"; then
	exit_code=1
    fi

    # --- Network Check ---
    if ping -c 1 -W 2 1.1.1.1 > /dev/null 2>&1; then
        echo "[PASS] Network connectivity"
    else
        echo "[FAIL] Network connectivity"
        exit_code=1
    fi

    exit "$exit_code"
fi
