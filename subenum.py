import requests

def find_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        res = requests.get(url, timeout=5)
        data = res.json()
        subdomains = {entry['name_value'] for entry in data}
        return list(subdomains)
    except Exception as e:
        return []
