from scapy.all import sniff # type: ignore

def packet_sniffer(interface):
    def process_packet(packet):
        if packet.haslayer("IP"):
            print(f"Packet: {packet[IP].src} -> {packet[IP].dst}")
    
    print(f"Sniffing on interface: {interface}")
    sniff(iface=interface, prn=process_packet, store=False)

interface = input("Enter network interface (e.g., eth0, wlan0): ")
packet_sniffer(interface)
