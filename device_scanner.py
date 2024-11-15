# device_scanner.py

import subprocess
import platform

def scan_network():
    connected_devices = []

    try:
        if platform.system() == "Linux":
            # Linux uses arp-scan for local network discovery
            result = subprocess.run(["arp-scan", "-l"], capture_output=True, text=True)
            lines = result.stdout.splitlines()
            for line in lines[2:-4]:  # Skip headers and footer
                columns = line.split()
                if len(columns) >= 2:
                    ip, mac = columns[0], columns[1]
                    connected_devices.append((ip, mac))
        else:
            # Windows/macOS alternative using arp command
            result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
            lines = result.stdout.splitlines()
            for line in lines:
                if line.strip() and "dynamic" in line:
                    parts = line.split()
                    connected_devices.append((parts[0], parts[1]))
    except Exception as e:
        print("Network scan error:", e)

    return connected_devices