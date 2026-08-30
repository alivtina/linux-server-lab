#!/bin/bash

hostname=$(hostname)
os=$(awk -F= '/^PRETTY_NAME=/ {print $2}' /etc/os-release | tr -d '"')
kernel=$(uname -r)
uptime=$(uptime -p)
memory=$(free -h | awk '/^Mem:/ {print $7}')
disk=$(df -h / | awk 'NR==2 {print $5}')
ip_addr=$(ip route get 1.1.1.1 | awk '{print $7}')
cpu_count=$(lscpu | awk '/^CPU\(s\):/ {print $2}')

echo "System Information"
echo "------------------"
echo "Hostname: $hostname"
echo "OS: $os"
echo "Kernel: $kernel"
echo "Uptime: $uptime"
echo "Memory Available: $memory"
echo "Disk Usage (/): $disk"
echo "IP Address: $ip_addr"
echo "CPU Cores: $cpu_count"
