import tkinter as tk
from device_scanner import scan_network
import queue

class NetworkMonitorGUI:
    def __init__(self, root, packet_queue):
        self.root = root
        self.packet_queue = packet_queue

        # Frames for device list and packet data
        self.device_frame = tk.Frame(root)
        self.device_frame.pack(side="left", fill="y", padx=10, pady=10)
        tk.Label(self.device_frame, text="Connected Devices", font=("Arial", 14)).pack()

        self.packet_frame = tk.Frame(root)
        self.packet_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        tk.Label(self.packet_frame, text="Packet Transfer", font=("Arial", 14)).pack()

        # Text box for displaying packet data
        self.packet_text = tk.Text(self.packet_frame, width=50, height=20)
        self.packet_text.pack()

        # Start device list update loop and packet display loop
        self.update_device_list()
        self.display_packets()

    def update_device_list(self):
        # Clear current devices
        for widget in self.device_frame.winfo_children()[1:]:
            widget.destroy()

        # Scan and display devices
        devices = scan_network()
        for ip, mac in devices:
            tk.Label(self.device_frame, text=f"{ip} ({mac})").pack()
        self.root.after(5000, self.update_device_list)

    def display_packets(self):
        # Check for packets in the queue and display one at a time
        if not self.packet_queue.empty():
            packet_info = self.packet_queue.get()
            self.packet_text.insert("end", f"{packet_info}\n")
            self.packet_text.see("end")  # Scroll to the end

        # Schedule the next packet display check
        self.root.after(1000, self.display_packets)  # 1-second delay for each packet

    def start_gui_loop(self):
        self.root.mainloop()
