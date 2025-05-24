import os
import platform
import socket
from ipaddress import ip_network
from concurrent.futures import ThreadPoolExecutor

def get_local_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def ping(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    # suppress output
    command = f"ping {param} 1 {ip} >nul 2>&1" if platform.system().lower() == "windows" else f"ping {param} 1 {ip} > /dev/null 2>&1"
    return os.system(command) == 0

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        result = sock.connect_ex((ip, port))
        return result == 0
    except:
        return False
    finally:
        sock.close()

def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        if scan_port(ip, port):
            open_ports.append(port)
    return open_ports

def scan_network(network, ports):
    print(f"Scanning network: {network}...")
    live_hosts = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = list(executor.map(lambda ip: (ip, ping(str(ip))), network.hosts()))
        for ip, alive in results:
            if alive:
                live_hosts.append(str(ip))

    print(f"\nFound {len(live_hosts)} live hosts.\n")
    for ip in live_hosts:
        print(f"Scanning ports on {ip}...")
        open_ports = scan_ports(ip, ports)
        if open_ports:
            print(f" Open ports: {', '.join(str(p) for p in open_ports)}")
        else:
            print(" No common open ports found.")
        print("-" * 30)

if __name__ == "__main__":
    local_ip = get_local_ip()
    subnet = ".".join(local_ip.split('.')[:3]) + ".0/24"
    network = ip_network(subnet, strict=False)

    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]

    print(f"Your IP: {local_ip}")
    print("Scanning the local network...\n")

    scan_network(network, common_ports)
