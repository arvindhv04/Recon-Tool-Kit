import socket

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
