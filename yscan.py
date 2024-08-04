# wifi_scanner.py
# Author: codedoctor
# This script scans for Wi-Fi networks and prints details about detected beacons.
# Note: Unauthorized access to computer networks is illegal and unethical. Use responsibly.

from scapy.all import *
import argparse

# Banner to display when the script runs
def print_banner():
    banner = """
    =========================================================
    |              .-^-.-^-.-^-.-^-.-^-.-^-.-^-.-^-.-^-.-^-.-^-.              |
    |              |  _   _   _   _   _   _   _   _   _   _   |              |
    |              | | | | | | | | | | | | | | | | | | | | | | |              |
    |              | | |_| | | |_| |_| | | |_| | | | | | | |_| |              |
    |              | |     | |     | | | |     | | | | | |     |              |
    |              | |     | |     | | | |     | | | | | |     |              |
    |              | |     | |     | | | |     | | | | | |     |              |
    |              | |     | |     | | | |     | | | | | |     |              |
    |              | |     | |     | | | |     | | | | | |     |              |
    |              | |     | |     | | | |     | | | | | |     |              |
    |              |  _   _   _   _   _   _   _   _   _   _   |              |
    |              |              Wi-Fi Scanner              |              |
    |              |               by codedoctor              |              |
    =========================================================
    """
    print(banner)

def packet_handler(packet):
    if packet.haslayer(Dot11Beacon):
        ssid = packet[Dot11Elt].info.decode(errors='ignore')
        bssid = packet[Dot11].addr2
        channel = packet[Dot11Elt:3].info.decode(errors='ignore')
        print(f"SSID: {ssid}, BSSID: {bssid}, Channel: {channel}")

def main(interface):
    print_banner()
    print("Starting Wi-Fi Scanner...")
    try:
        sniff(iface=interface, prn=packet_handler, timeout=30)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Wi-Fi Scanner")
    parser.add_argument("interface", help="Network interface to use for scanning")
    args = parser.parse_args()
    main(args.interface)

