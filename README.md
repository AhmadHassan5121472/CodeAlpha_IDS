# Python Network Intrusion Detection System (NIDS)

## Overview

This project implements a Python-based Network Intrusion Detection System (NIDS) that monitors live network traffic, detects suspicious or malicious activities using rule-based detection, generates alerts, automatically responds to attacks by blocking malicious IP addresses, logs events, and visualizes attack statistics through graphs.

The application provides a modern graphical interface built with CustomTkinter for real-time monitoring and management.

---

## Features

- Real-time packet capturing
- Monitor network traffic for 30 seconds
- Detect TCP SYN Flood attacks
- Detect ICMP Flood attacks
- Detect Port Scanning
- Detect connections to suspicious ports
- Automatic attacker IP blocking
- CSV attack logging
- Interactive GUI
- Live attack table
- Attack statistics
- Bar Graph
- Pie Chart
- Line Graph
- Top Attacker Graph

---

## Technologies Used

- Python
- Scapy
- CustomTkinter
- Matplotlib
- Pandas

---

## Installation

```bash
pip install -r requirements.txt
```

Run as Administrator

```bash
python main.py
```

---

## Detection Rules

| Attack | Description |
|----------|-------------|
| SYN Flood | Excessive SYN packets |
| ICMP Flood | Large number of ICMP packets |
| Port Scan | Multiple SYN requests |
| Suspicious Ports | FTP SSH Telnet SMB RDP |

---

## Response Mechanism

When an intrusion is detected the IDS

- Generates an alert
- Saves attack details
- Blocks attacker IP
- Updates graphs
- Displays attack in GUI

---

## Output

- Live Monitoring
- Attack Logs
- CSV Export
- Real-time Alerts
- Graphical Statistics

---

## Future Improvements

- Email Alerts
- Machine Learning Detection
- Web Dashboard
- Database Storage
- Multi-threading
- Deep Packet Inspection
- Signature Updates
- AI-based Intrusion Detection

---

## Educational Purpose

This project is developed for cybersecurity education and research to demonstrate the concepts of packet capturing, intrusion detection, response mechanisms, logging, and attack visualization.
