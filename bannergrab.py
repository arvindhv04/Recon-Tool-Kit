import socket
import sys

def grab_banner(host, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((host, port))
        banner = s.recv(1024).decode(errors='ignore')
        s.close()
        return banner.strip()
    except:
        return "No banner"
        if __name__ == "__main__":
            if len(sys.argv) != 3:
                print(f"Usage: python {sys.argv[0]} <host> <port>")
                sys.exit(1)
            host = sys.argv[1]
            try:
                port = int(sys.argv[2])
            except ValueError:
                print("Port must be an integer.")
                sys.exit(1)
            banner = grab_banner(host, port)
            print(f"Banner from {host}:{port} -> {banner}")