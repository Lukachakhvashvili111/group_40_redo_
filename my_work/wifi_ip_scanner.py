import subprocess
import re
import time

def get_local_subnet_base():
    result = subprocess.check_output("ipconfig", shell=True).decode()
    match = re.search(r"IPv4 Address[.\s]*:\s*(\d+\.\d+\.\d+)\.\d+", result)
    return match.group(1) if match else None

def ping_all_ips(subnet_base):
    print(f"Scanning {subnet_base}.0/24 ...")
    for i in range(1, 255):
        ip = f"{subnet_base}.{i}"
        subprocess.Popen(f"ping -n 1 -w 100 {ip}", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(5)  # Wait for ARP table to fill

def get_active_ips():
    output = subprocess.check_output("arp -a", shell=True).decode()
    entries = re.findall(r"(\d+\.\d+\.\d+\.\d+)\s+([a-fA-F0-9:-]{17}|[a-fA-F0-9\-]{17})", output)
    return entries

def main():
    print("📡 WiFi IP Scanner - Devices Around You\n")
    subnet = get_local_subnet_base()
    if not subnet:
        print("Could not determine local network.")
        return

    ping_all_ips(subnet)
    devices = get_active_ips()

    print(f"\nFound {len(devices)} active devices:\n")
    for ip, mac in devices:
        print(f"IP: {ip} | MAC: {mac}")

if __name__ == "__main__":
    main()
