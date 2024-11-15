import tkinter as tk
from gui import NetworkMonitorGUI
from packet_sniffer import packet_sniffer
import threading
import queue

# Queue to store packets for controlled display
packet_queue = queue.Queue()

# Callback function to add packets to the queue
def packet_callback(packet_info):
    packet_queue.put(packet_info)

# Start the main GUI application
root = tk.Tk()
root.title("Network Monitor")
root.geometry("800x500")

# Initialize GUI with packet queue
gui = NetworkMonitorGUI(root, packet_queue)

# Start packet sniffer in a separate thread
sniffer_thread = threading.Thread(target=packet_sniffer, args=(packet_callback,))
sniffer_thread.daemon = True  # Daemonize thread to close with GUI
sniffer_thread.start()

# Start GUI loop
gui.start_gui_loop()
