import socket
import sys
import ssl
import logging
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

def grab_banner(host, port, timeout=3):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        
        sock.connect((host, port))
        
        banner = ""
        try:
            if port in [80, 443, 8080, 8443]:
                sock.send(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
            elif port in [21, 22, 23, 25, 110, 143]:
                pass
            
            data = sock.recv(1024)
            banner = data.decode('utf-8', errors='ignore').strip()
            
        except Exception as e:
            logger.debug(f"Error receiving banner from {host}:{port}: {e}")
        
        sock.close()
        
        if banner:
            return banner
        else:
            return "No banner received"
            
    except socket.timeout:
        return "Connection timeout"
    except ConnectionRefusedError:
        return "Connection refused"
    except Exception as e:
        return f"Error: {str(e)}"

def grab_ssl_banner(host, port, timeout=3):
    try:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        
        with socket.create_connection((host, port), timeout=timeout) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
                banner = f"SSL Certificate: {cert.get('subject', 'Unknown')}"
                return banner
    except Exception as e:
        return f"SSL Error: {str(e)}"

def analyze_banner(banner, port):
    analysis = {
        "version_info": [],
        "security_headers": [],
        "potential_vulnerabilities": []
    }
    
    banner_lower = banner.lower()
    
    version_patterns = [
        "apache", "nginx", "iis", "tomcat", "jetty", "dovecot", "postfix",
        "pure-ftpd", "vsftpd", "openssh", "mysql", "postgresql", "redis"
    ]
    
    for pattern in version_patterns:
        if pattern in banner_lower:
            analysis["version_info"].append(pattern)
    
    if port in [80, 443, 8080, 8443]:
        security_headers = [
            "x-frame-options", "x-content-type-options", "x-xss-protection",
            "strict-transport-security", "content-security-policy"
        ]
        
        for header in security_headers:
            if header in banner_lower:
                analysis["security_headers"].append(header)
    
    if any(word in banner_lower for word in ["debug", "test", "dev", "staging"]):
        analysis["potential_vulnerabilities"].append("Development/Test Environment")
    
    if "anonymous" in banner_lower and port == 21:
        analysis["potential_vulnerabilities"].append("Anonymous FTP Access")
    
    return analysis

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
    
    print(f"Grabbing banner from {host}:{port}")
    
    banner = grab_banner(host, port)
    print(f"Banner: {banner}")
    
    if port in [443, 993, 995, 8443]:
        print("\nTrying SSL banner grab...")
        ssl_banner = grab_ssl_banner(host, port)
        print(f"SSL Banner: {ssl_banner}")
    
    analysis = analyze_banner(banner, port)
    if analysis["version_info"] or analysis["security_headers"] or analysis["potential_vulnerabilities"]:
        print("\nBanner Analysis:")
        if analysis["version_info"]:
            print(f"  Versions detected: {', '.join(analysis['version_info'])}")
        if analysis["security_headers"]:
            print(f"  Security headers: {', '.join(analysis['security_headers'])}")
        if analysis["potential_vulnerabilities"]:
            print(f"  Potential issues: {', '.join(analysis['potential_vulnerabilities'])}")