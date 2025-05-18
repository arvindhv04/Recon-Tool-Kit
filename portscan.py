import socket

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
