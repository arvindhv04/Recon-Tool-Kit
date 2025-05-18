import json
from datetime import datetime

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # or use str(obj)
        return super().default(obj)

def generate_report(target, subdomains, open_ports, whois_info, banners):
    report = {
        "target": target,
        "subdomains": subdomains,
        "open_ports": open_ports,
        "whois_info": whois_info,
        "banners": banners,
    }

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4, cls=CustomJSONEncoder)
