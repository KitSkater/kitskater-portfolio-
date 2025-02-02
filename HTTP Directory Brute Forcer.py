import requests  # type: ignore
import os

def brute_force_directories(target, wordlist):
    """
    Brute force directories on a target web server.

    :param target: The target URL.
    :param wordlist: A list of directory names to test.
    """
    print(f"Starting directory brute-force attack on: {target}")
    found_directories = []

    for word in wordlist:
        url = f"{target.rstrip('/')}/{word}"
        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
            if response.status_code == 200:
                print(f"Found: {url} (Status Code: {response.status_code})")
                found_directories.append(url)
            elif response.status_code == 403:
                print(f"Forbidden: {url} (Status Code: {response.status_code})")
            elif response.status_code == 404:
                print(f"Not Found: {url} (Status Code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {url}: {e}")
    
    print("\nSummary of found directories:")
    for directory in found_directories:
        print(directory)

def load_wordlist(file_path):
    """
    Load a wordlist from a file.

    :param file_path: The path to the wordlist file.
    :return: A list of directory names.
    """
    if not os.path.isfile(file_path):
        print("Error: File not found!")
        return []

    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

if __name__ == "__main__":
    target = input("Enter target URL (e.g., http://example.com): ").strip()
    wordlist_option = input("Load wordlist from a file? (yes/no): ").strip().lower()

    if wordlist_option == "yes":
        file_path = input("Enter the wordlist file path: ").strip()
        wordlist = load_wordlist(file_path)
        if not wordlist:
            print("No words loaded. Exiting...")
            exit(1)
    else:
        # Default wordlist for testing purposes
        wordlist = ["admin", "login", "test", "config", "dashboard"]

    brute_force_directories(target, wordlist)

