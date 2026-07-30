"""
detection.py

Rule-based detection engine for the Network Intrusion Detection System.
"""

from scapy.layers.inet import IP, TCP, ICMP
from collections import defaultdict
from datetime import datetime

# Import logger
try:
    from logger import save_alert
except ImportError:
    def save_alert(*args):
        pass

# GUI reference
gui_instance = None

# Counters
syn_counter = defaultdict(int)
icmp_counter = defaultdict(int)

# Statistics
attack_stats = {
    "SYN Flood": 0,
    "ICMP Flood": 0,
    "Port Scan": 0,
    "Suspicious Port": 0
}

# Thresholds
SYN_THRESHOLD = 20
ICMP_THRESHOLD = 15

# Suspicious ports
SUSPICIOUS_PORTS = [21, 22, 23, 445, 3389]


# --------------------------------------
# Set GUI Reference
# --------------------------------------

def set_gui(gui):
    global gui_instance
    gui_instance = gui


# --------------------------------------
# Generate Alert
# --------------------------------------

def generate_alert(ip, attack):

    current_time = datetime.now().strftime("%H:%M:%S")

    print(f"[ALERT] {attack} detected from {ip}")

    attack_stats[attack] += 1

    save_alert(current_time, ip, attack)

    if gui_instance:

        gui_instance.after(
            0,
            lambda: gui_instance.add_alert(
                current_time,
                ip,
                attack
            )
        )


# --------------------------------------
# Detect Packet
# --------------------------------------

def detect_packet(packet):

    if IP not in packet:
        return

    src_ip = packet[IP].src

    # -------------------------
    # TCP Detection
    # -------------------------

    if TCP in packet:

        tcp = packet[TCP]

        # SYN Flood
        if tcp.flags == "S":

            syn_counter[src_ip] += 1

            if syn_counter[src_ip] == SYN_THRESHOLD:

                generate_alert(
                    src_ip,
                    "SYN Flood"
                )

        # Suspicious Ports
        if tcp.dport in SUSPICIOUS_PORTS:

            generate_alert(
                src_ip,
                "Suspicious Port"
            )

        # Port Scan
        if syn_counter[src_ip] >= 10:

            if syn_counter[src_ip] % 10 == 0:

                generate_alert(
                    src_ip,
                    "Port Scan"
                )

    # -------------------------
    # ICMP Detection
    # -------------------------

    if ICMP in packet:

        icmp_counter[src_ip] += 1

        if icmp_counter[src_ip] == ICMP_THRESHOLD:

            generate_alert(
                src_ip,
                "ICMP Flood"
            )


# --------------------------------------
# Get Statistics
# --------------------------------------

def get_statistics():
    return attack_stats


# --------------------------------------
# Reset Counters
# --------------------------------------

def reset_statistics():

    global syn_counter
    global icmp_counter

    syn_counter = defaultdict(int)
    icmp_counter = defaultdict(int)

    for key in attack_stats:
        attack_stats[key] = 0


# --------------------------------------
# Test Module
# --------------------------------------

if __name__ == "__main__":

    print("Detection module loaded successfully.")