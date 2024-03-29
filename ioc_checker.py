import requests
import base64
import sys

def check_url_ioc(ioc):
    try:
        ioc_url = f'https://www.virustotal.com/api/v3/urls/{url_id}'
        headers = {'x-apikey': '578e5c341b092c39e4e9880b82e266d1db144f97d7e7bd8fe77e84b222138047', 'id': ioc}
        response = requests.get(ioc_url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as http_err:
        if response.status_code == 404:
            print("The URL does not exist in the VirusTotal database.")
            sys.exit(1)
        else:
            raise http_err

def check_ip_ioc(ioc):
    try:
        ioc_ip = f'https://www.virustotal.com/api/v3/ip_addresses/{ioc}'
        headers = {'x-apikey': '578e5c341b092c39e4e9880b82e266d1db144f97d7e7bd8fe77e84b222138047', 'ip': ioc}
        response = requests.get(ioc_ip, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as http_err:
        if response.status_code == 404:
            print("The IP does not exist in the VirusTotal database.")
            sys.exit(1)
        else:
            raise http_err

def check_domain_ioc(ioc):
    try:
        ioc_domain = f'https://www.virustotal.com/api/v3/domains/{ioc}'
        headers = {'x-apikey': '578e5c341b092c39e4e9880b82e266d1db144f97d7e7bd8fe77e84b222138047', 'domain': ioc}
        response = requests.get(ioc_domain, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as http_err:
        if response.status_code == 404:
            print("The domain does not exist in the VirusTotal database.")
            sys.exit(1)
        else:
            raise http_err


ioc_type = input("Enter one of the following IOC types: URL, IP, or Domain\n")
ioc = input("Enter the IOC: ")
if ioc_type == 'url':
    url_id = base64.urlsafe_b64encode(f"{ioc}".encode()).decode().strip("=")
    url_result = check_url_ioc(url_id)
    print(url_result)
elif ioc_type == "domain":
    domain_result = check_domain_ioc(ioc)
    print(domain_result)
else:
    ip_result = check_ip_ioc(ioc)
    print(ip_result)
