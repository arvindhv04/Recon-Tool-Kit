import json
from datetime import datetime
import os

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

def generate_report(report_data):
    report = {
        "scan_info": {
            "target": report_data["target"],
            "scan_date": datetime.now().isoformat()
        },
        "subdomains": report_data["subdomains"],
        "open_ports": report_data["open_ports"],
        "whois_info": report_data["whois_info"],
        "banners": report_data["banners"],
        "dns_info": report_data["dns_info"],
        "web_technologies": report_data["web_technologies"],
        "vulnerabilities": report_data["vulnerabilities"],
        "beef_injection": report_data["beef_injection"]
    }

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4, cls=CustomJSONEncoder)
