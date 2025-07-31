import requests
import time
from urllib.parse import urlparse
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def find_subdomains(domain):
    subdomains = set()
    
    try:
        logger.info(f"Querying crt.sh for subdomains of {domain}")
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()
        
        for entry in data:
            name = entry.get('name_value', '').lower()
            if name and domain in name:
                subdomains.add(name)
        
        logger.info(f"Found {len(subdomains)} subdomains from crt.sh")
    except Exception as e:
        logger.error(f"Error querying crt.sh: {e}")
    
    common_subdomains = [
        'www', 'mail', 'ftp', 'admin', 'blog', 'dev', 'test', 'staging',
        'api', 'cdn', 'ns1', 'ns2', 'smtp', 'pop', 'imap', 'webmail',
        'support', 'help', 'docs', 'wiki', 'forum', 'shop', 'store',
        'app', 'mobile', 'secure', 'vpn', 'remote', 'portal'
    ]
    
    try:
        logger.info("Performing DNS bruteforce for common subdomains")
        for sub in common_subdomains:
            test_domain = f"{sub}.{domain}"
            try:
                import socket
                socket.gethostbyname(test_domain)
                subdomains.add(test_domain)
                logger.debug(f"Found subdomain: {test_domain}")
            except socket.gaierror:
                continue
    except Exception as e:
        logger.error(f"Error during DNS bruteforce: {e}")
    
    return sorted(list(subdomains))

def validate_domain(domain):
    try:
        parsed = urlparse(f"http://{domain}")
        return bool(parsed.netloc)
    except:
        return False
