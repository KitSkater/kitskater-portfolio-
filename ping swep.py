import subprocess

def ping_sweep(subnet):
    active_hosts = []
    for i in range(1, 255):  # Adjust for your subnet range
        ip = f"{subnet}.{i}"
        response = subprocess.run(["ping", "-c", "1", "-W", "1", ip], stdout=subprocess.DEVNULL)
        if response.returncode == 0:
            print(f"Active: {ip}")
            active_hosts.append(ip)
    return active_hosts

subnet = input("Enter subnet (e.g., 192.168.1): ")
active_hosts = ping_sweep(subnet)
print(f"Active hosts in {subnet}.x: {active_hosts}")
