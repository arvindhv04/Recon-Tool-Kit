#!/usr/bin/env python3
"""
Recon-Tool-Kit: Enhanced Network Reconnaissance Tool
A comprehensive tool for gathering intelligence about target domains.
"""

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
from beef_injection import inject_beef_hook
from report_gen import generate_report
import webbrowser

target = input("Enter target domain: ")

print("Running reconnaissance...")

subdomains = find_subdomains(target)
open_ports = scan_ports(target)
whois_info = get_whois(target)
banners = {port: grab_banner(target, port) for port in open_ports}
dns_info = get_dns_info(target)
web_technologies = detect_web_technologies(target)
vulnerabilities = check_vulnerabilities(target, open_ports)

print("Checking for BeEF injection opportunities...")
beef_results = inject_beef_hook(target)

report_data = {
    "target": target,
    "subdomains": subdomains,
    "open_ports": open_ports,
    "whois_info": whois_info,
    "banners": banners,
    "dns_info": dns_info,
    "web_technologies": web_technologies,
    "vulnerabilities": vulnerabilities,
    "beef_injection": beef_results
}

generate_report(report_data)
print("Recon complete. Report saved.")
