import socket

def port_scanner(target, ports):
    print(f"Scanning {target}...")
    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                if sock.connect_ex((target, port)) == 0:
                    open_ports.append(port)
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
    return open_ports

target = input("Enter target IP address: ")
ports = range(1, 1025)  # Scanning first 1024 ports
result = port_scanner(target, ports)
print(f"Open ports on {target}: {result}")
