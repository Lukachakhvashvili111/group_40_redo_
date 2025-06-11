import subprocess
import re
import time

def scan_wifi_networks():
    print("📡 Scanning nearby WiFi networks...\n")
    try:
        result = subprocess.check_output("netsh wlan show networks mode=bssid", shell=True).decode(errors="ignore")
        ssids = re.findall(r'SSID \d+ : (.+)', result)
        unique_ssids = list(set(ssids))
        for ssid in unique_ssids:
            print(f" - {ssid}")
    except Exception as e:
        print("Failed to scan WiFi networks:", e)

def ping_local_range(base_ip):
    print(f"\n🔎 Pinging devices in {base_ip}.0/24 to update ARP cache...\n")
    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        subprocess.Popen(f"ping -n 1 -w 100 {ip}", stdout=subprocess.DEVNULL)
    time.sleep(5)

def get_connected_ips():
    print("🧠 Reading ARP table to find connected devices...\n")
    output = subprocess.check_output("arp -a", shell=True).decode()
    devices = re.findall(r"(\d+\.\d+\.\d+\.\d+)\s+([a-fA-F0-9\-]{17})", output)
    unique_ips = list(set([ip for ip, mac in devices]))
    for ip in unique_ips:
        print(f"📍 Device IP: {ip}")
    print(f"\n✅ Total found: {len(unique_ips)}")

def get_base_ip():
    output = subprocess.check_output("ipconfig", shell=True).decode()
    match = re.search(r"IPv4 Address[.\s]*:\s*(\d+\.\d+\.\d+)\.\d+", output)
    if match:
        return match.group(1)
    else:
        return None

def main():
    print("==== WiFi Device Scanner (Windows) ====\n")
    scan_wifi_networks()
    base_ip = get_base_ip()
    if not base_ip:
        print("Could not detect base IP. Are you connected to WiFi?")
        return
    ping_local_range(base_ip)
    get_connected_ips()

if __name__ == "__main__":
    main()
