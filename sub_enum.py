import requests

target = "hackthebox.com"

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

with open("subdomains.txt", 'r') as wordlist:
    for line in wordlist:
        word = line.strip()
        try_url = word + "." + target
        response = request(try_url)
        if response:
            print("[+] Discovered subdomain ->  " + try_url)
