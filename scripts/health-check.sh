#!/bin/bash

echo "=== Server Health Check ==="

status=0

# --- SSH Service Check ---
if systemctl is-active --quiet ssh; then
    echo "[PASS] SSH service is running"
else
    echo "[FAIL] SSH service is not running"
    status=1
fi

# --- Disk Usage Check ---
disk=$(df -h / | awk 'NR==2 {print $5}' | tr -d '%')

if [ "$disk" -lt 80 ]; then
    echo "[PASS] Root filesystem usage: ${disk}%"
elif [ "$disk" -lt 90 ]; then
    echo "[WARN] Root filesystem usage: ${disk}%"
else
    echo "[FAIL] Root filesystem usage: ${disk}%"
    status=1
fi

# --- Network Check ---
if ping -c 1 -W 2 1.1.1.1 > /dev/null 2>&1; then
    echo "[PASS] Network connectivity"
else
    echo "[FAIL] Network connectivity"
    status=1
fi

exit "$status"

