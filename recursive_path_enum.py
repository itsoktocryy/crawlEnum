import requests
import re
import urllib.parse as urlparse

target = "https://app.hackthebox.com/"
target_links = []

def extract_links(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))

def crawl(url):
    href_links = extract_links(url)
    for link in href_links:
        link = urlparse.urljoin(url, link)

        if '#' in link:
            link = link.split('#')[0]
        
        if target in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)

crawl(target)
