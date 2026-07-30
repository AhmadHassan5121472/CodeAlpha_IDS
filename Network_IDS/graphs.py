"""
graphs.py

Network Intrusion Detection System
----------------------------------

Features
--------
1. Bar Chart
2. Pie Chart
3. Line Chart
4. Top Attacker Chart
5. Dashboard Summary
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

LOG_FILE = "attack_logs.csv"


# -------------------------------------
# Read CSV
# -------------------------------------

def load_logs():

    if not os.path.exists(LOG_FILE):

        print("No attack log found.")

        return None

    try:

        df = pd.read_csv(LOG_FILE)

        if df.empty:

            print("No attacks detected.")

            return None

        return df

    except Exception as e:

        print(e)

        return None


# -------------------------------------
# Bar Chart
# -------------------------------------

def bar_chart():

    df = load_logs()

    if df is None:

        return

    attacks = df["Attack Type"].value_counts()

    plt.figure(figsize=(9,6))

    attacks.plot(kind="bar")

    plt.title("Detected Attack Types")

    plt.xlabel("Attack Type")

    plt.ylabel("Number of Attacks")

    plt.grid(axis="y")

    plt.tight_layout()

    plt.show()


# -------------------------------------
# Pie Chart
# -------------------------------------

def pie_chart():

    df = load_logs()

    if df is None:

        return

    attacks = df["Attack Type"].value_counts()

    plt.figure(figsize=(7,7))

    plt.pie(
        attacks,
        labels=attacks.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Attack Distribution")

    plt.tight_layout()

    plt.show()


# -------------------------------------
# Line Chart
# -------------------------------------

def line_chart():

    df = load_logs()

    if df is None:

        return

    counts = []

    total = 0

    for _ in range(len(df)):

        total += 1

        counts.append(total)

    plt.figure(figsize=(10,5))

    plt.plot(
        counts,
        marker="o",
        linewidth=2
    )

    plt.title("Detected Alerts Over Time")

    plt.xlabel("Alert Number")

    plt.ylabel("Total Alerts")

    plt.grid(True)

    plt.tight_layout()

    plt.show()


# -------------------------------------
# Top Attacker Graph
# -------------------------------------

def attacker_chart():

    df = load_logs()

    if df is None:

        return

    attackers = df["Source IP"].value_counts().head(10)

    plt.figure(figsize=(10,6))

    attackers.plot(kind="bar")

    plt.title("Top Attacking IP Addresses")

    plt.xlabel("Source IP")

    plt.ylabel("Number of Alerts")

    plt.grid(axis="y")

    plt.tight_layout()

    plt.show()


# -------------------------------------
# Dashboard Summary
# -------------------------------------

def dashboard():

    df = load_logs()

    if df is None:

        return

    print()

    print("=" * 60)

    print("NETWORK IDS SUMMARY")

    print("=" * 60)

    print()

    print("Total Alerts :", len(df))

    print()

    print("Attack Types")

    print()

    print(df["Attack Type"].value_counts())

    print()

    print("Top Attackers")

    print()

    print(df["Source IP"].value_counts())

    print()

    print("=" * 60)


# -------------------------------------
# Show Everything
# -------------------------------------

def show_graphs():

    dashboard()

    bar_chart()

    pie_chart()

    line_chart()

    attacker_chart()


# -------------------------------------
# Test
# -------------------------------------

if __name__ == "__main__":

    show_graphs()