from subenum import find_subdomains
from portscan import scan_ports
from whois_lookup import get_whois
from bannergrab import grab_banner
from report_gen import generate_report

target = input("Enter target domain: ")
subdomains = find_subdomains(target)
open_ports = scan_ports(target)
whois_info = get_whois(target)
banners = {port: grab_banner(target, port) for port in open_ports}
generate_report(target, subdomains, open_ports, whois_info, banners)
print("Recon complete. Report saved.")
