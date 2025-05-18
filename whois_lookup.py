import whois

def get_whois(domain):
    try:
        info = whois.whois(domain)
        return dict(info)
    except:
        return {}
