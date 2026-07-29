# Python Network Intrusion Detection System (IDS)

## Overview

This project is a Python-based **Network Intrusion Detection System (NIDS)** designed to monitor live network traffic, detect suspicious or potentially malicious activities, and generate real-time security alerts. The IDS captures packets using the **Scapy** library, analyzes them based on predefined detection rules, logs detected threats, and visualizes attack statistics using graphical charts.

The system provides a simple and educational implementation of an intrusion detection solution, making it suitable for cybersecurity learning, academic projects, and basic network security monitoring.

## Features

* Real-time network packet capture and analysis
* Monitors network traffic for a configurable duration (default: 30 seconds)
* Detects common suspicious activities, including:

  * TCP SYN Flood attacks
  * ICMP (Ping) Flood attacks
  * Access attempts to sensitive ports (FTP, SSH, Telnet, SMB, and RDP)
* Generates instant alerts when suspicious behavior is detected
* Automatically responds by blocking malicious IP addresses (Windows Firewall or Linux iptables)
* Stores detected attacks in a CSV log file
* Visualizes attack statistics using bar charts and pie charts
* Easy to modify and extend with custom detection rules

## Technologies Used

* Python 3
* Scapy
* Pandas
* Matplotlib
* Windows Firewall / Linux iptables

## Project Workflow

1. Capture live network packets.
2. Inspect each packet for suspicious patterns.
3. Compare traffic against predefined IDS rules.
4. Generate alerts for detected threats.
5. Block malicious source IP addresses.
6. Save attack information into a CSV file.
7. Display graphical summaries of detected attacks.

## Detection Rules

The IDS currently detects:

* Excessive TCP SYN packets indicating possible SYN Flood or port scanning.
* Excessive ICMP packets indicating possible Ping Flood attacks.
* Connection attempts to commonly targeted ports:

  * Port 21 (FTP)
  * Port 22 (SSH)
  * Port 23 (Telnet)
  * Port 445 (SMB)
  * Port 3389 (Remote Desktop)

These rules can be expanded by adding new signatures or traffic analysis logic.

## Output

The program produces:

* Real-time intrusion alerts
* Automatic response by blocking attacker IP addresses
* Attack logs stored in `attack_logs.csv`
* Bar chart showing the number of detected attacks
* Pie chart illustrating the distribution of attack types

## Requirements

Install the required Python packages before running the project:

```bash
pip install scapy pandas matplotlib
```

Run the program with administrator/root privileges to allow packet capturing and firewall rule creation.

## Educational Purpose

This project demonstrates the basic concepts of a Network Intrusion Detection System (NIDS), including packet inspection, rule-based threat detection, alert generation, automated response, logging, and data visualization. It is intended for educational use, cybersecurity practice, and academic coursework.

## Future Improvements

* Machine learning-based anomaly detection
* Email or SMS alert notifications
* Web-based monitoring dashboard
* Database integration for long-term log storage
* Real-time attack visualization
* Support for additional intrusion detection signatures
* Integration with SIEM platforms
* Detection of ARP spoofing, DNS attacks, and HTTP-based threats

## Disclaimer

This project is intended for educational and research purposes only. It should be used only on networks and systems that you own or have explicit authorization to monitor. The authors are not responsible for any misuse of this software.
