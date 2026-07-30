"""
packet_capture.py

Captures live network traffic for 30 seconds and
passes every packet to the detection engine.
"""

from scapy.all import sniff
import threading
import time

from detection import detect_packet, set_gui

# Monitoring duration (seconds)
CAPTURE_TIME = 30


def packet_callback(packet):
    """
    Called automatically for every captured packet.
    """
    detect_packet(packet)


def progress_bar(gui):
    """
    Updates GUI progress bar.
    """

    gui.progress.set(0)

    for i in range(CAPTURE_TIME):

        percent = (i + 1) / CAPTURE_TIME

        gui.progress.set(percent)

        gui.status.configure(
            text=f"Status : Monitoring... {i + 1}/{CAPTURE_TIME} sec"
        )

        time.sleep(1)

    gui.progress.set(1)

    gui.status.configure(
        text="Status : Monitoring Finished"
    )


def start_monitoring(gui):
    """
    Starts packet capture.
    """

    # Give detection.py access to the GUI
    set_gui(gui)

    # Start progress bar
    thread = threading.Thread(
        target=progress_bar,
        args=(gui,)
    )

    thread.daemon = True
    thread.start()

    print("=" * 60)
    print("Network Monitoring Started")
    print("=" * 60)

    sniff(
        prn=packet_callback,
        timeout=CAPTURE_TIME,
        store=False
    )

    gui.progress.set(1)

    gui.status.configure(
        text="Status : Monitoring Completed"
    )

    print("=" * 60)
    print("Network Monitoring Completed")
    print("=" * 60)