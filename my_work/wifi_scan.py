import subprocess
import re

def scan_wifi():
    try:
        # Run iwlist to scan Wi-Fi networks (replace wlan0 with your Wi-Fi interface if different)
        result = subprocess.check_output(['sudo', 'iwlist', 'wlan0', 'scan'], stderr=subprocess.DEVNULL).decode('utf-8')
    except subprocess.CalledProcessError:
        print("Failed to run iwlist scan. Make sure you have sudo privileges and wireless-tools installed.")
        return

    networks = result.split('Cell')
    for net in networks[1:]:
        ssid_search = re.search(r'ESSID:"([^"]+)"', net)
        if ssid_search:
            ssid = ssid_search.group(1)
        else:
            ssid = "Hidden"

        # Check for encryption info
        encryption = "Open"
        if "IE: WPA Version 1" in net:
            encryption = "WPA"
        elif "IE: IEEE 802.11i/WPA2 Version 1" in net:
            encryption = "WPA2"
        elif "Encryption key:on" in net and "IE:" not in net:
            encryption = "WEP"

        print(f"SSID: {ssid}\tSecurity: {encryption}")

if __name__ == "__main__":
    scan_wifi()
