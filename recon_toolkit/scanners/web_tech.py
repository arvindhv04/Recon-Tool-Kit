import requests
import re
from urllib.parse import urljoin

def detect_web_technologies(domain):
    technologies = {
        "server": "",
        "cms": "",
        "frameworks": [],
        "languages": [],
        "databases": [],
        "analytics": [],
        "security": []
    }
    
    try:
        url = f"http://{domain}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        server = response.headers.get('Server', '')
        if server:
            technologies["server"] = server
        
        content = response.text.lower()
        
        if 'wordpress' in content or 'wp-content' in content:
            technologies["cms"] = "WordPress"
        elif 'joomla' in content:
            technologies["cms"] = "Joomla"
        elif 'drupal' in content:
            technologies["cms"] = "Drupal"
        elif 'magento' in content:
            technologies["cms"] = "Magento"
        
        if 'jquery' in content:
            technologies["frameworks"].append("jQuery")
        if 'bootstrap' in content:
            technologies["frameworks"].append("Bootstrap")
        if 'react' in content:
            technologies["frameworks"].append("React")
        if 'angular' in content:
            technologies["frameworks"].append("Angular")
        if 'vue' in content:
            technologies["frameworks"].append("Vue.js")
        
        if 'php' in content or 'php' in server.lower():
            technologies["languages"].append("PHP")
        if 'asp.net' in content or 'asp.net' in server.lower():
            technologies["languages"].append("ASP.NET")
        if 'python' in content:
            technologies["languages"].append("Python")
        if 'java' in content:
            technologies["languages"].append("Java")
        
        if 'mysql' in content:
            technologies["databases"].append("MySQL")
        if 'postgresql' in content:
            technologies["databases"].append("PostgreSQL")
        if 'mongodb' in content:
            technologies["databases"].append("MongoDB")
        
        if 'google-analytics' in content or 'gtag' in content:
            technologies["analytics"].append("Google Analytics")
        if 'facebook' in content and 'pixel' in content:
            technologies["analytics"].append("Facebook Pixel")
        
        if 'cloudflare' in content or 'cf-ray' in response.headers:
            technologies["security"].append("Cloudflare")
        if 'incapsula' in content:
            technologies["security"].append("Incapsula")
        
    except:
        pass
    
    return technologies 