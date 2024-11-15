# packet_sniffer.py

from scapy.all import sniff, IP

def packet_sniffer(callback):
    def process_packet(packet):
        if packet.haslayer(IP):
            src = packet[IP].src
            dst = packet[IP].dst
            proto = packet[IP].proto
            # Use callback to send formatted packet details to GUI
            callback(f"Packet: {src} -> {dst}, Protocol: {proto}")

    # Start sniffing, filter for IP packets only, and process without storing
    sniff(prn=process_packet, filter="ip", store=0)
