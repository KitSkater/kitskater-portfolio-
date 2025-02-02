import itertools
password = "abcderf"
def brute_force(password, charset, max_length):
    for length in range(1, max_length + 1):
        for attempt in itertools.product(charset, repeat=length):
            attempt = ''.join(attempt)
            print(f"Trying password: {attempt}")
            if attempt == password:
                print(f"Password found: {attempt}")
                return
    print("Password not found.")