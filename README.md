# Wi-Fi Scanner Tool
Wi-Fi Scanner Tool

A simple Python-based Wi-Fi scanner tool for detecting and displaying details of nearby Wi-Fi networks. This tool uses the scapy library to capture and analyze Wi-Fi beacon frames, providing information such as SSID, BSSID, and channel for each detected network.
Features

    Network Scanning: Detects and lists Wi-Fi networks in the vicinity.
    Beacon Information: Extracts and displays SSID, BSSID, and channel information.
    Customizable: Easy to modify and extend for additional features or integration with other tools.

Prerequisites

    Python 3.x
    scapy library

Installation

    Clone the Repository:

    bash

git clone https://github.com/USERNAME/wifi-scanner.git
cd wifi-scanner

Install Dependencies:

bash

    pip install scapy

Usage

    Set Your Network Interface to Monitor Mode:

    Make sure your network interface is in monitor mode. You can use tools like airmon-ng to enable monitor mode:

    bash

sudo airmon-ng start wlan0

Replace wlan0 with your network interface.

Run the Scanner:

bash

    sudo python wifi_scanner.py wlan0mon

    Replace wlan0mon with the monitor mode interface name.

Notes

    Ethical Use: Ensure you have permission to scan networks. Unauthorized access to networks is illegal and unethical.
    Compatibility: This tool is designed for Linux environments. Compatibility with other operating systems may vary.

License

This project is licensed under the MIT License - see the LICENSE file for details.
Author

    codedoctor
