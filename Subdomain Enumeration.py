import dns.resolver # type: ignore

def subdomain_enum(domain, wordlist):
    for sub in wordlist:
        subdomain = f"{sub}.{domain}"
        try:
            dns.resolver.resolve(subdomain, 'A')
            print(f"Found: {subdomain}")
        except dns.resolver.NXDOMAIN:
            pass
        except Exception as e:
            print(f"Error: {e}")

domain = input("Enter the target domain: ")
wordlist = ["www", "mail", "ftp", "api", "test", "dev"]  # Expand this list
subdomain_enum(domain, wordlist)
