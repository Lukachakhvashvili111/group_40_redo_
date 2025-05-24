from ftplib import FTP

def check_ftp_anonymous(ip):
    try:
        print(f"[*] Connecting to FTP on {ip}...")
        ftp = FTP(ip)
        ftp.login()  # tries anonymous login by default
        print(f"[+] Anonymous login allowed on {ip}")
        ftp.quit()
    except Exception as e:
        print(f"[-] Anonymous login not allowed on {ip}. Error: {e}")

if __name__ == "__main__":
    target_ip = input("Enter the target IP (e.g. 192.168.56.101): ")
    check_ftp_anonymous(target_ip)
