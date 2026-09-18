import socket
import argparse
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging

logger = logging.getLogger(__name__)

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 80: "HTTP",
    110: "POP3", 143: "IMAP", 443: "HTTPS", 993: "IMAPS", 995: "POP3S",
    3306: "MySQL", 5432: "PostgreSQL", 27017: "MongoDB", 6379: "Redis",
    8080: "HTTP-Alt", 8443: "HTTPS-Alt", 3389: "RDP", 5900: "VNC",
    22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 80: "HTTP",
    110: "POP3", 143: "IMAP", 443: "HTTPS", 993: "IMAPS", 995: "POP3S",
    3306: "MySQL", 5432: "PostgreSQL", 27017: "MongoDB", 6379: "Redis",
    8080: "HTTP-Alt", 8443: "HTTPS-Alt", 3389: "RDP", 5900: "VNC"
}

def scan_port(host, port, timeout=2):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        
        if result == 0:
            service = COMMON_PORTS.get(port, "Unknown")
            logger.info(f"Port {port}/tcp ({service}) is open")
            return port, service
        return None
    except Exception as e:
        logger.debug(f"Error scanning port {port}: {e}")
        return None

def scan_ports(host, ports=None, max_workers=50):
    if ports is None:
        ports = list(COMMON_PORTS.keys())
    
    open_ports = {}
    logger.info(f"Scanning {len(ports)} ports on {host}")
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_port = {
            executor.submit(scan_port, host, port): port 
            for port in ports
        }
        
        for future in as_completed(future_to_port):
            result = future.result()
            if result:
                port, service = result
                open_ports[port] = service
    
    logger.info(f"Found {len(open_ports)} open ports")
    return open_ports

def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except:
        return COMMON_PORTS.get(port, "Unknown")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enhanced port scanner")
    parser.add_argument("host", help="Target host to scan")
    parser.add_argument("-p", "--ports", help="Comma-separated list of ports to scan")
    parser.add_argument("-t", "--timeout", type=int, default=2, help="Timeout in seconds")
    parser.add_argument("-w", "--workers", type=int, default=50, help="Number of worker threads")
    
    args = parser.parse_args()
    
    ports_to_scan = None
    if args.ports:
        try:
            ports_to_scan = [int(p.strip()) for p in args.ports.split(",")]
        except ValueError:
            print("Invalid port format. Use comma-separated integers.")
            exit(1)
    
    print(f"Scanning {args.host}...\n")
    start_time = time.time()
    
    open_ports = scan_ports(args.host, ports_to_scan, args.workers)
    
    if open_ports:
        print("\nOpen ports:")
        for port, service in sorted(open_ports.items()):
            print(f"  Port {port}/tcp ({service}) is open")
    else:
        print("No ports found open.")
    
    elapsed = time.time() - start_time
    print(f"\nScan completed in {elapsed:.2f} seconds")