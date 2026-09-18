import argparse
from urllib.parse import urlparse

from .reporting.json_report import generate_report
from .scanners.banners import grab_banner
from .scanners.dns import get_dns_info
from .scanners.ports import scan_ports
from .scanners.subdomains import find_subdomains
from .scanners.vulnerabilities import check_vulnerabilities
from .scanners.web_tech import detect_web_technologies
from .scanners.web_vulnerabilities import scan_website_vulnerabilities
from .scanners.whois import get_whois


def normalize_target(target):
    target = target.strip()
    if "://" in target:
        target = urlparse(target).hostname or target
    return target.rstrip("/")


def run_scan(target):
    target = normalize_target(target)
    if not target:
        raise ValueError("A target domain is required")

    print("Running reconnaissance...")
    subdomains = find_subdomains(target)
    open_ports = scan_ports(target)
    whois_info = get_whois(target)
    banners = {port: grab_banner(target, port) for port in open_ports}
    dns_info = get_dns_info(target)
    web_technologies = detect_web_technologies(target)
    vulnerabilities = check_vulnerabilities(target, open_ports)

    print("Starting web vulnerability scan...")
    web_vulnerabilities = scan_website_vulnerabilities(
        f"https://{target}", max_depth=2, max_pages=50
    )

    report_data = {
        "target": target,
        "subdomains": subdomains,
        "open_ports": open_ports,
        "whois_info": whois_info,
        "banners": banners,
        "dns_info": dns_info,
        "web_technologies": web_technologies,
        "vulnerabilities": vulnerabilities,
        "web_vulnerabilities": web_vulnerabilities,
    }
    generate_report(report_data)
    print("Recon complete. Report saved to report.json.")
    return report_data


def main():
    parser = argparse.ArgumentParser(description="Run reconnaissance against a domain")
    parser.add_argument("target", nargs="?", help="Domain or URL to scan")
    args = parser.parse_args()
    target = args.target or input("Enter target domain: ")
    run_scan(target)


if __name__ == "__main__":
    main()
