import os
import platform
import time

def simulate_usb_payload():
    """A simulated educational USB payload for authorized use only."""
    print("This is a demonstration of an authorized USB payload simulation.")

    # Simulate performing an action (e.g., opening a file or message)
    if platform.system() == "Windows":
        os.system('msg * "This is a test payload. Educate users on securing USB ports!"')
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system('notify-send "Penetration Testing" "This is a test payload. Secure your endpoints!"')
    else:
        print("Unsupported operating system for this demonstration.")

if __name__ == "__main__":
    # Delay to simulate time for a USB to be recognized
    print("Simulating USB payload... Plugging in USB...")
    time.sleep(2)
    simulate_usb_payload()
