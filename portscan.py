import socket
import argparse

def scan_ports(host):
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 8080]
    open_ports = []
    for port in common_ports:
        try:
            sock = socket.create_connection((host, port), timeout=1)
            open_ports.append(port)
            sock.close()
        except:
            continue
    return open_ports
    if __name__ == "__main__":

        def get_service_name(port):
            try:
                return socket.getservbyport(port)
            except:
                return "Unknown"

        parser = argparse.ArgumentParser(description="Simple port scanner")
        parser.add_argument("host", help="Target host to scan")
        args = parser.parse_args()

        print(f"Scanning {args.host}...\n")
        open_ports = scan_ports(args.host)
        if open_ports:
            print("Open ports:")
            for port in open_ports:
                service = get_service_name(port)
                print(f"  Port {port}/tcp ({service}) is open")
        else:
            print("No common ports open.")