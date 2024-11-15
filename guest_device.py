import socket
import threading
import time
import random
import queue
from device_scanner import scan_network  # Import device scanning functionality


class GuestDevice:
    def __init__(self, device_name, privilege_level="guest"):
        self.device_name = device_name
        self.privilege_level = privilege_level
        self.packet_queue = queue.Queue()
        self.connected = False
        self.ip_address = self.assign_guest_ip()

    def assign_guest_ip(self):
        # Assign an IP for the guest device (here we are hardcoding or setting randomly)
        # In real cases, this could be dynamically assigned by DHCP or static assignment.
        base_ip = "192.168.1."
        ip_suffix = random.randint(50, 254)
        return f"{base_ip}{ip_suffix}"

    def connect_to_network(self):
        """Simulate the guest device connecting to the network"""
        self.connected = True
        print(
            f"{self.device_name} ({self.ip_address}) connected to the network with {self.privilege_level} privileges.")
        self.perform_guest_actions()

    def disconnect_from_network(self):
        """Simulate the guest device disconnecting from the network"""
        self.connected = False
        print(f"{self.device_name} ({self.ip_address}) disconnected from the network.")

    def perform_guest_actions(self):
        """Perform actions based on the guest's privileges"""
        if self.privilege_level == "guest":
            self.read_only_access()
        else:
            print(f"{self.device_name} has full access, not a guest.")

    def read_only_access(self):
        """Simulate a guest device accessing network info in a read-only manner"""
        while self.connected:
            # Display connected devices
            devices = scan_network()
            print(f"{self.device_name} is viewing connected devices:")
            for ip, mac in devices:
                print(f" - Device IP: {ip}, MAC: {mac}")

            # Simulate reading packet data in a controlled way
            self.view_packet_transfers()

            # Wait a bit before next check
            time.sleep(random.randint(5, 10))

    def view_packet_transfers(self):
        """Simulate viewing packet transfer data as a guest"""
        print(f"{self.device_name} is viewing packet transfers:")
        while not self.packet_queue.empty():
            packet_info = self.packet_queue.get()
            print(f" - {packet_info}")


# Simulate the Guest Device in action
def main():
    guest_device = GuestDevice(device_name="GuestDevice1")

    # Connect the guest device in a separate thread
    connection_thread = threading.Thread(target=guest_device.connect_to_network)
    connection_thread.start()

    # Let the guest device be connected for a period, then disconnect
    time.sleep(30)  # Duration to stay connected
    guest_device.disconnect_from_network()


if __name__ == "__main__":
    main()
