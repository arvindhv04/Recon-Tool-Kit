import argparse
import sys
import time
import logging
from datetime import datetime
from subenum import find_subdomains
from portscan import scan_ports
from whois_lookup import get_whois
from bannergrab import grab_banner
from dns_lookup import get_dns_info
from web_tech import detect_web_technologies
from vulnerability_scan import check_vulnerabilities
from web_vulnerability_scanner import scan_website_vulnerabilities
from web_vuln_report import generate_html_report
from report_gen import generate_report


target = input("Enter target domain: ")

print("Running reconnaissance...")

subdomains = find_subdomains(target)
open_ports = scan_ports(target)
whois_info = get_whois(target)
banners = {port: grab_banner(target, port) for port in open_ports}
dns_info = get_dns_info(target)
web_technologies = detect_web_technologies(target)
vulnerabilities = check_vulnerabilities(target, open_ports)

print("Starting web vulnerability scan...")
web_vulns = scan_website_vulnerabilities(f"https://{target}", max_depth=2, max_pages=50)

# Generate HTML report for web vulnerabilities
if web_vulns and web_vulns.get('vulnerabilities'):
    html_report_file = generate_html_report(web_vulns, f"web_vuln_report_{target}.html")
    print(f"Web vulnerability HTML report generated: {html_report_file}")

report_data = {
    "target": target,
    "subdomains": subdomains,
    "open_ports": open_ports,
    "whois_info": whois_info,
    "banners": banners,
    "dns_info": dns_info,
    "web_technologies": web_technologies,
    "vulnerabilities": vulnerabilities,
    "web_vulnerabilities": web_vulns
}

generate_report(report_data)
print("Recon complete. Report saved.")
