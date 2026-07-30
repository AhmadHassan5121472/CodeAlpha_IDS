"""
logger.py

Network Intrusion Detection System
----------------------------------

Features
--------
1. Save alerts into CSV
2. Export logs
3. Read logs
4. Search logs
5. Clear logs
6. Count attacks
7. Display summary
"""

import csv
import os
from collections import Counter

LOG_FILE = "attack_logs.csv"

# -----------------------------------
# Create CSV File
# -----------------------------------

def initialize_logger():

    if not os.path.exists(LOG_FILE):

        with open(LOG_FILE, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    "Time",
                    "Source IP",
                    "Attack Type"
                ]
            )

# -----------------------------------
# Save Alert
# -----------------------------------

def save_alert(time, ip, attack):

    initialize_logger()

    with open(LOG_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                time,
                ip,
                attack
            ]
        )

# -----------------------------------
# Read Logs
# -----------------------------------

def read_logs():

    initialize_logger()

    logs = []

    with open(LOG_FILE, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            logs.append(row)

    return logs

# -----------------------------------
# Search by IP
# -----------------------------------

def search_ip(ip):

    results = []

    logs = read_logs()

    for row in logs:

        if row["Source IP"] == ip:

            results.append(row)

    return results

# -----------------------------------
# Search by Attack
# -----------------------------------

def search_attack(name):

    results = []

    logs = read_logs()

    for row in logs:

        if row["Attack Type"] == name:

            results.append(row)

    return results

# -----------------------------------
# Total Alerts
# -----------------------------------

def total_alerts():

    logs = read_logs()

    return len(logs)

# -----------------------------------
# Count Attack Types
# -----------------------------------

def attack_statistics():

    logs = read_logs()

    attacks = []

    for row in logs:

        attacks.append(
            row["Attack Type"]
        )

    return Counter(attacks)

# -----------------------------------
# Delete Log File
# -----------------------------------

def clear_logs():

    if os.path.exists(LOG_FILE):

        os.remove(LOG_FILE)

    initialize_logger()

# -----------------------------------
# Export Logs
# -----------------------------------

def export_logs(filename):

    logs = read_logs()

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "Time",
                "Source IP",
                "Attack Type"
            ]
        )

        for row in logs:

            writer.writerow(
                [
                    row["Time"],
                    row["Source IP"],
                    row["Attack Type"]
                ]
            )

# -----------------------------------
# Print Summary
# -----------------------------------

def print_summary():

    stats = attack_statistics()

    print()

    print("=" * 45)

    print("IDS ATTACK SUMMARY")

    print("=" * 45)

    print()

    print("Total Alerts :", total_alerts())

    print()

    for attack, count in stats.items():

        print(f"{attack} : {count}")

# -----------------------------------
# Print All Logs
# -----------------------------------

def print_logs():

    logs = read_logs()

    print()

    print("=" * 70)

    print("RECORDED ALERTS")

    print("=" * 70)

    for row in logs:

        print(
            row["Time"],
            row["Source IP"],
            row["Attack Type"]
        )

# -----------------------------------
# Test
# -----------------------------------

if __name__ == "__main__":

    initialize_logger()

    save_alert(
        "12:30:01",
        "192.168.1.100",
        "SYN Flood"
    )

    save_alert(
        "12:30:20",
        "192.168.1.101",
        "ICMP Flood"
    )

    save_alert(
        "12:31:10",
        "192.168.1.100",
        "Port Scan"
    )

    print_logs()

    print()

    print_summary()

    print()

    print(search_ip("192.168.1.100"))

    print()

    export_logs("backup_logs.csv")

    print()

    print("Logs exported successfully.")