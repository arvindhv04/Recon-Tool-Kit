SCAN_CONFIG = {
    "default_timeout": 3,
    "max_workers": 50,
    "retry_attempts": 2,
    "delay_between_requests": 0.1
}

PORT_CONFIG = {
    "common_ports": {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 80: "HTTP",
        110: "POP3", 143: "IMAP", 443: "HTTPS", 993: "IMAPS", 995: "POP3S",
        3306: "MySQL", 5432: "PostgreSQL", 27017: "MongoDB", 6379: "Redis",
        8080: "HTTP-Alt", 8443: "HTTPS-Alt", 3389: "RDP", 5900: "VNC"
    },
    "high_risk_ports": [21, 23, 3389, 5900],
    "medium_risk_ports": [22, 25, 110, 143],
    "ssl_ports": [443, 993, 995, 8443]
}

SUBDOMAIN_CONFIG = {
    "common_subdomains": [
        'www', 'mail', 'ftp', 'admin', 'blog', 'dev', 'test', 'staging',
        'api', 'cdn', 'ns1', 'ns2', 'smtp', 'pop', 'imap', 'webmail',
        'support', 'help', 'docs', 'wiki', 'forum', 'shop', 'store',
        'app', 'mobile', 'secure', 'vpn', 'remote', 'portal', 'cpanel',
        'webdisk', 'autodiscover', 'autoconfig', 'm', 'mobile', 'wap'
    ],
    "sources": {
        "crt_sh": "https://crt.sh/?q=%25.{domain}&output=json",
        "hackertarget": "https://api.hackertarget.com/hostsearch/?q={domain}",
        "virustotal": "https://virustotal.com/vtapi/v2/domain/report?apikey={api_key}&domain={domain}"
    }
}

BANNER_CONFIG = {
    "version_patterns": [
        "apache", "nginx", "iis", "tomcat", "jetty", "dovecot", "postfix",
        "pure-ftpd", "vsftpd", "openssh", "mysql", "postgresql", "redis",
        "wordpress", "joomla", "drupal", "magento", "shopify"
    ],
    "security_headers": [
        "x-frame-options", "x-content-type-options", "x-xss-protection",
        "strict-transport-security", "content-security-policy",
        "x-powered-by", "server", "x-aspnet-version"
    ],
    "vulnerability_indicators": [
        "debug", "test", "dev", "staging", "beta", "alpha",
        "anonymous", "guest", "default", "admin", "root"
    ]
}

REPORT_CONFIG = {
    "output_formats": ["json", "html", "txt"],
    "default_output_dir": "reports",
    "include_timestamp": True,
    "max_findings_display": 10
}

SECURITY_CONFIG = {
    "risk_levels": {
        "LOW": {
            "color": "green",
            "description": "Minimal security concerns"
        },
        "MEDIUM": {
            "color": "orange", 
            "description": "Moderate security concerns"
        },
        "HIGH": {
            "color": "red",
            "description": "Significant security concerns"
        }
    },
    "recommendations": {
        "HIGH": [
            "Close unnecessary high-risk ports",
            "Implement strong authentication",
            "Use VPN for remote access",
            "Enable firewall rules",
            "Regular security audits"
        ],
        "MEDIUM": [
            "Review open ports and close unnecessary ones",
            "Implement security headers",
            "Regular security audits",
            "Update software versions",
            "Monitor access logs"
        ],
        "LOW": [
            "Regular security monitoring",
            "Keep systems updated",
            "Implement security best practices",
            "Document security procedures"
        ]
    }
}

LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(levelname)s - %(message)s",
    "file": "recon_tool.log",
    "max_file_size": 10 * 1024 * 1024,
    "backup_count": 5
}

API_CONFIG = {
    "virustotal_api_key": "",
    "shodan_api_key": "",
    "censys_api_id": "",
    "censys_api_secret": ""
}

USER_AGENT = "Recon-Tool-Kit/2.0 (Security Research Tool)"

RATE_LIMIT_CONFIG = {
    "requests_per_second": 10,
    "delay_between_requests": 0.1,
    "max_concurrent_requests": 5
} 