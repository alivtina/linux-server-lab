#!/bin/bash

source scripts/health-check.sh

assert_exit_code() {
    expected=$1
    actual=$2

    if [ "$actual" -eq "$expected" ]; then
        echo "[PASS] Expected $expected, got $actual"
    else
        echo "[FAIL] Expected $expected, got $actual"
        exit 1
    fi
}

check_disk_usage 44
assert_exit_code 0 "$?"

check_disk_usage 85
assert_exit_code 0 "$?"

check_disk_usage 95
assert_exit_code 1 "$?"

echo "All tests passed"
