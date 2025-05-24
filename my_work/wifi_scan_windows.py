import subprocess
import re

def scan_wifi_windows():
    try:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'networks', 'mode=Bssid'], encoding='utf-8')
    except subprocess.CalledProcessError:
        print("Failed to run netsh command.")
        return

    networks = result.split('\n')
    current_ssid = None
    security = None

    for line in networks:
        ssid_match = re.match(r'\s*SSID\s+\d+\s*:\s*(.*)', line)
        if ssid_match:
            if current_ssid:
                print(f"SSID: {current_ssid}\tSecurity: {security}")
            current_ssid = ssid_match.group(1).strip()
            security = None

        sec_match = re.match(r'\s*Authentication\s*:\s*(.*)', line)
        if sec_match:
            security = sec_match.group(1).strip()

    # Print last network
    if current_ssid:
        print(f"SSID: {current_ssid}\tSecurity: {security}")

if __name__ == "__main__":
    scan_wifi_windows()
