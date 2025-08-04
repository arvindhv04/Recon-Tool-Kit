#!/usr/bin/env python3

from xss_injection import inject_xss_script, XSSInjector

def test_xss_injector():
    print("=== XSS Injection Test ===\n")
    
    test_domain = "example.com"
    
    print(f"Testing XSS injection on: {test_domain}")
    print("-" * 50)
    
    results = inject_xss_script(test_domain)
    
    print("\n=== Results ===")
    print(f"Target: {results['target']}")
    print(f"Vulnerable pages found: {len(results['vulnerable_pages'])}")
    print(f"Injection results: {len(results['injection_results'])}")
    print(f"Payloads created: {len(results['payloads'])}")
    
    if results['vulnerable_pages']:
        print("\nVulnerable Pages:")
        for i, page in enumerate(results['vulnerable_pages'], 1):
            print(f"  {i}. {page['url']} ({page['type']})")
            if 'vulnerabilities' in page:
                for vuln in page['vulnerabilities']:
                    print(f"     - {vuln['type']}: {vuln['description']}")
    
    if results['injection_results']:
        print("\nInjection Results:")
        for i, result in enumerate(results['injection_results'], 1):
            print(f"  {i}. {result['url']} - {result['status']}")
            if 'payload_type' in result:
                print(f"     Payload: {result['payload_type']}")
    
    if results['payloads']:
        print("\nCreated Payloads:")
        for i, payload in enumerate(results['payloads'], 1):
            print(f"  {i}. {payload['payload_type']}: {payload['payload'][:50]}...")

def test_payloads():
    print("\n=== Testing Available Payloads ===")
    
    injector = XSSInjector()
    payloads = injector.list_available_payloads()
    
    print(f"Available payloads ({len(payloads)}):")
    for i, payload_type in enumerate(payloads, 1):
        payload = injector.xss_payloads[payload_type]
        print(f"  {i}. {payload_type}: {payload}")
    
    random_payload = injector.get_random_payload()
    print(f"\nRandom payload: {random_payload['type']}")
    print(f"Payload: {random_payload['payload']}")

if __name__ == "__main__":
    test_xss_injector()
    test_payloads() 