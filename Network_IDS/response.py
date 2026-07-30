"""
response.py

Implements automatic response actions for the IDS.

Features
--------
1. Block attacker IP
2. Prevent duplicate firewall rules
3. Unblock attacker IP
4. Keep list of blocked IPs
5. Works on Windows and Linux
"""

import os
import platform
import subprocess
from datetime import datetime

# -----------------------------
# Store blocked IPs
# -----------------------------

blocked_ips = set()

# -----------------------------
# Log Response
# -----------------------------

def log_response(message):

    now = datetime.now().strftime("%H:%M:%S")

    print(f"[{now}] {message}")

# -----------------------------
# Windows Firewall
# -----------------------------

def block_windows(ip):

    rule_name = f"NIDS_Block_{ip}"

    cmd = [
        "netsh",
        "advfirewall",
        "firewall",
        "add",
        "rule",
        f"name={rule_name}",
        "dir=in",
        "action=block",
        f"remoteip={ip}"
    ]

    try:

        subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        blocked_ips.add(ip)

        log_response(f"Blocked {ip} using Windows Firewall")

    except Exception as e:

        log_response(str(e))

# -----------------------------
# Linux IPTables
# -----------------------------

def block_linux(ip):

    cmd = [
        "sudo",
        "iptables",
        "-A",
        "INPUT",
        "-s",
        ip,
        "-j",
        "DROP"
    ]

    try:

        subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        blocked_ips.add(ip)

        log_response(f"Blocked {ip} using IPTables")

    except Exception as e:

        log_response(str(e))

# -----------------------------
# Block IP
# -----------------------------

def block_ip(ip):

    if ip in blocked_ips:

        return False

    system = platform.system()

    if system == "Windows":

        block_windows(ip)

    elif system == "Linux":

        block_linux(ip)

    else:

        log_response("Operating System not supported")

        return False

    return True

# -----------------------------
# Unblock Windows
# -----------------------------

def unblock_windows(ip):

    rule_name = f"NIDS_Block_{ip}"

    cmd = [
        "netsh",
        "advfirewall",
        "firewall",
        "delete",
        "rule",
        f"name={rule_name}"
    ]

    try:

        subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        blocked_ips.discard(ip)

        log_response(f"Removed Firewall Rule for {ip}")

    except Exception as e:

        log_response(str(e))

# -----------------------------
# Unblock Linux
# -----------------------------

def unblock_linux(ip):

    cmd = [
        "sudo",
        "iptables",
        "-D",
        "INPUT",
        "-s",
        ip,
        "-j",
        "DROP"
    ]

    try:

        subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        blocked_ips.discard(ip)

        log_response(f"Removed IPTables Rule for {ip}")

    except Exception as e:

        log_response(str(e))

# -----------------------------
# Unblock IP
# -----------------------------

def unblock_ip(ip):

    system = platform.system()

    if system == "Windows":

        unblock_windows(ip)

    elif system == "Linux":

        unblock_linux(ip)

# -----------------------------
# Get Blocked IP List
# -----------------------------

def get_blocked_ips():

    return list(blocked_ips)

# -----------------------------
# Clear All Rules
# -----------------------------

def clear_all_blocks():

    for ip in list(blocked_ips):

        unblock_ip(ip)

    blocked_ips.clear()

# -----------------------------
# Response Trigger
# -----------------------------

def respond_to_attack(ip, attack):

    log_response(f"Attack Detected : {attack}")

    if block_ip(ip):

        log_response(f"Automatic Response Executed for {ip}")

    else:

        log_response(f"{ip} was already blocked")

# -----------------------------
# Testing
# -----------------------------

if __name__ == "__main__":

    print()

    print("Testing Response Module")

    print("-" * 50)

    ip = "192.168.1.100"

    respond_to_attack(ip, "SYN Flood")

    print()

    print("Blocked IPs")

    print(get_blocked_ips())

    print()

    clear_all_blocks()

    print("All Rules Removed")