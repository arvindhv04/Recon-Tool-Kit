import socket
import dns.resolver
import dns.reversename
import dns.zone
import dns.query

def get_dns_info(domain):
    dns_info = {
        "a_records": [],
        "aaaa_records": [],
        "mx_records": [],
        "ns_records": [],
        "txt_records": [],
        "cname_records": [],
        "ptr_records": []
    }
    
    try:
        answers = dns.resolver.resolve(domain, 'A')
        dns_info["a_records"] = [str(rdata) for rdata in answers]
    except:
        pass
    
    try:
        answers = dns.resolver.resolve(domain, 'AAAA')
        dns_info["aaaa_records"] = [str(rdata) for rdata in answers]
    except:
        pass
    
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        dns_info["mx_records"] = [str(rdata.exchange) for rdata in answers]
    except:
        pass
    
    try:
        answers = dns.resolver.resolve(domain, 'NS')
        dns_info["ns_records"] = [str(rdata) for rdata in answers]
    except:
        pass
    
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        dns_info["txt_records"] = [str(rdata) for rdata in answers]
    except:
        pass
    
    try:
        answers = dns.resolver.resolve(domain, 'CNAME')
        dns_info["cname_records"] = [str(rdata) for rdata in answers]
    except:
        pass
    
    return dns_info 