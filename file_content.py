import requests
import re
import urllib.parse

def request(url):
    try:
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.InvalidURL:
        pass
    except UnicodeError:
        pass
target_links = []
target_url = 'https://zsecurity.org'

def extract_links_from(url):
    response = requests.get(target_url)
    resp = response.content.decode('UTF-8')
    return re.findall('(?:href=")(.*?)"', resp)

def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urllib.parse.urljoin(url, link)
        if "#" in link:
            link = link.split('#')[0]
            
        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)
    
crawl(target_url)
