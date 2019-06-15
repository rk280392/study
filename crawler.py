import requests


def req(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.InvalidURL:
        pass
    except UnicodeError:
        pass

target_url = 'wifi-soft.com'
discovered_domains = []

with open("subdomains-wodlist.txt","r") as wordlist_file:
    for line in wordlist_file:
        test_url = line.strip() + '.' + target_url
        response = req(test_url)
        if response:
            print("[+] discoverd some domain ---> " + test_url)
            discovered_domains.append(test_url)
print(discovered_domains)

with open("files-and-dirs-wordlist.txt","r") as common_dirs:
    for line in common_dirs:
        test_url2 = target_url + '/' + line
        response = req(test_url2)
        if response:
            print("[+] discovered directories --> " + test_url2)
