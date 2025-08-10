#!/usr/bin/env python3
"""
Test script for the enhanced web vulnerability scanner
Demonstrates the new detailed form field information and vulnerability location reporting
"""

from web_vulnerability_scanner import WebVulnerabilityScanner
import json

def test_enhanced_scanner():
    """Test the enhanced scanner with a sample website"""
    
    # Test with a sample website (you can change this to any website you want to test)
    test_url = "https://httpbin.org"
    
    print(f"Testing enhanced web vulnerability scanner with: {test_url}")
    print("=" * 60)
    
    # Create scanner instance
    scanner = WebVulnerabilityScanner(test_url, max_depth=1, max_pages=5)
    
    # Run the scan
    print("Starting scan...")
    report = scanner.run_full_scan()
    
    # Display results
    print("\n" + "=" * 60)
    print("SCAN RESULTS")
    print("=" * 60)
    
    print(f"Target: {report['scan_info']['target']}")
    print(f"Pages scanned: {report['scan_info']['total_pages_scanned']}")
    print(f"Vulnerabilities found: {report['scan_info']['total_vulnerabilities']}")
    
    # Display vulnerability summary
    summary = report['summary']
    print(f"\nVulnerability Summary:")
    print(f"  High: {summary['high_severity']}")
    print(f"  Medium: {summary['medium_severity']}")
    print(f"  Low: {summary['low_severity']}")
    
    # Display detailed vulnerability information
    if report['vulnerabilities']:
        print(f"\nDetailed Vulnerabilities:")
        print("-" * 40)
        
        for i, vuln in enumerate(report['vulnerabilities'], 1):
            print(f"\n{i}. {vuln['type']}")
            print(f"   URL: {vuln['url']}")
            print(f"   Severity: {vuln['severity']}")
            print(f"   Description: {vuln['description']}")
            
            # Show detailed location information
            if 'location' in vuln:
                print(f"   Location: {vuln['location']}")
            
            if 'parameter' in vuln:
                print(f"   Parameter: {vuln['parameter']}")
                if 'parameter_type' in vuln:
                    print(f"   Parameter Type: {vuln['parameter_type']}")
            
            if 'form_context' in vuln and vuln['form_context']:
                print(f"   Form Context:")
                form_ctx = vuln['form_context']
                if 'form_action' in form_ctx:
                    print(f"     Action: {form_ctx['form_action']}")
                if 'form_method' in form_ctx:
                    print(f"     Method: {form_ctx['form_method']}")
                if 'field_id' in form_ctx and form_ctx['field_id']:
                    print(f"     Field ID: {form_ctx['field_id']}")
                if 'field_class' in form_ctx and form_ctx['field_class']:
                    print(f"     Field Classes: {', '.join(form_ctx['field_class'])}")
                if 'field_placeholder' in form_ctx and form_ctx['field_placeholder']:
                    print(f"     Placeholder: {form_ctx['field_placeholder']}")
                if 'field_required' in form_ctx:
                    print(f"     Required: {form_ctx['field_required']}")
            
            if 'evidence' in vuln:
                print(f"   Evidence: {vuln['evidence']}")
            
            print("-" * 40)
    else:
        print("\nNo vulnerabilities found!")
    
    # Display forms discovered
    if report['forms_discovered']:
        print(f"\nForms Discovered:")
        print("-" * 40)
        
        for url, forms in report['forms_discovered'].items():
            print(f"\nURL: {url}")
            for j, form in enumerate(forms, 1):
                print(f"  Form {j}:")
                print(f"    Action: {form['action']}")
                print(f"    Method: {form['method']}")
                if form['id']:
                    print(f"    ID: {form['id']}")
                if form['class']:
                    print(f"    Classes: {', '.join(form['class'])}")
                
                print(f"    Fields ({len(form['fields'])}):")
                for field in form['fields']:
                    print(f"      - {field['name']} ({field['type']})")
                    if field['id']:
                        print(f"        ID: {field['id']}")
                    if field['placeholder']:
                        print(f"        Placeholder: {field['placeholder']}")
                    if field['required']:
                        print(f"        Required: Yes")
                print()
    else:
        print("\nNo forms discovered!")
    
    # Save detailed report to file
    output_file = "enhanced_scanner_report.json"
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\nDetailed report saved to: {output_file}")
    print("=" * 60)

if __name__ == "__main__":
    test_enhanced_scanner()
