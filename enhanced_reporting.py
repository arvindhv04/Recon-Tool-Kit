import json
import csv
import xml.etree.ElementTree as ET
from datetime import datetime

def generate_csv_report(report_data, filename="recon_report.csv"):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Category', 'Finding', 'Details'])
        
        for subdomain in report_data["subdomains"]:
            writer.writerow(['Subdomain', subdomain, ''])
        
        for port in report_data["open_ports"]:
            writer.writerow(['Open Port', port, report_data["open_ports"][port]])
        
        for vuln in report_data["vulnerabilities"]["open_services"]:
            writer.writerow(['Vulnerability', 'Open Service', vuln])

def generate_xml_report(report_data, filename="recon_report.xml"):
    root = ET.Element("reconnaissance_report")
    
    scan_info = ET.SubElement(root, "scan_info")
    target = ET.SubElement(scan_info, "target")
    target.text = report_data["target"]
    
    subdomains = ET.SubElement(root, "subdomains")
    for subdomain in report_data["subdomains"]:
        sub = ET.SubElement(subdomains, "subdomain")
        sub.text = subdomain
    
    ports = ET.SubElement(root, "open_ports")
    for port in report_data["open_ports"]:
        port_elem = ET.SubElement(ports, "port")
        port_elem.set("number", str(port))
        port_elem.set("service", report_data["open_ports"][port])
    
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def generate_summary_report(report_data, filename="summary.txt"):
    with open(filename, 'w') as f:
        f.write("RECONNAISSANCE SUMMARY REPORT\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Target: {report_data['target']}\n")
        f.write(f"Scan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write(f"SUBDOMAINS FOUND: {len(report_data['subdomains'])}\n")
        for subdomain in report_data['subdomains']:
            f.write(f"  - {subdomain}\n")
        
        f.write(f"\nOPEN PORTS: {len(report_data['open_ports'])}\n")
        for port, service in report_data['open_ports'].items():
            f.write(f"  - Port {port} ({service})\n")
        
        f.write(f"\nVULNERABILITIES FOUND: {len(report_data['vulnerabilities']['open_services'])}\n")
        for vuln in report_data['vulnerabilities']['open_services']:
            f.write(f"  - {vuln}\n") 