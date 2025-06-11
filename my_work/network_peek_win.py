import os
import subprocess
import re
from time import sleep

def get_local_subnet():
    result = subprocess.check_output("ipconfig", shell=True).decode()
    match = re.search(r"IPv4 Address[.\s]*:\s*(\d+\.\d+\.\d+)\.\d+", result)
    if match:
        base_ip = match.group(1)
        return base_ip
    return None

def ping_sweep(base_ip):
    print(f"Pinging devices on {base_ip}.0/24 ...")
    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        subprocess.Popen(f"ping -n 1 -w 100 {ip}", stdout=subprocess.DEVNULL)
    sleep(5)  # Allow ARP table to fill

def get_connected_devices():
    print("Checking ARP table...")
    output = subprocess.check_output("arp -a", shell=True).decode()
    ips = re.findall(r"\d+\.\d+\.\d+\.\d+", output)
    filtered = [ip for ip in ips if not ip.startswith("224.") and not ip.endswith(".255")]
    return list(set(filtered))

def get_nearby_wifi():
    print("Scanning for nearby WiFi networks...")
    try:
        output = subprocess.check_output("netsh wlan show networks", shell=True).decode(errors="ignore")
        ssids = re.findall(r"SSID \d+ : (.+)", output)
        return list(set(ssids))
    except subprocess.CalledProcessError:
        return []

def main():
    print("=== Network Peek (Windows) ===\n")
    subnet_base = get_local_subnet()
    if not subnet_base:
        print("Could not find local subnet.")
        return

    ping_sweep(subnet_base)
    devices = get_connected_devices()
    print(f"\n📶 Devices on your WiFi: {len(devices)}")
    for ip in devices:
        print(f" - {ip}")

    wifi_list = get_nearby_wifi()
    print(f"\n📡 Nearby WiFi Networks ({len(wifi_list)}):")
    for ssid in wifi_list:
        print(f" - {ssid}")

if __name__ == "__main__":
    main()
