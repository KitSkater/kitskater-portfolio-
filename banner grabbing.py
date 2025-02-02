import socket

def banner_grabber(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)
            sock.connect((target, port))
            banner = sock.recv(1024).decode().strip()
            return banner
    except Exception:
        return "No banner or connection failed."

target = input("Enter target IP address: ")
port = int(input("Enter port number: "))
banner = banner_grabber(target, port)
print(f"Banner for {target}:{port} -> {banner}")
