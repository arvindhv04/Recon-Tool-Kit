import json
import os
from datetime import datetime

def generate_html_report(web_vuln_data, output_file="web_vulnerability_report.html"):
    """Generate an HTML report for web vulnerability scan results"""
    
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Vulnerability Scan Report</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }}
        .header {{
            text-align: center;
            border-bottom: 3px solid #e74c3c;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        .header h1 {{
            color: #2c3e50;
            margin: 0;
            font-size: 2.5em;
        }}
        .scan-info {{
            background: #ecf0f1;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
        }}
        .scan-info h2 {{
            color: #34495e;
            margin-top: 0;
        }}
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }}
        .info-item {{
            background: white;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #3498db;
        }}
        .info-label {{
            font-weight: bold;
            color: #7f8c8d;
            font-size: 0.9em;
        }}
        .info-value {{
            color: #2c3e50;
            font-size: 1.1em;
            margin-top: 5px;
        }}
        .summary {{
            background: #ecf0f1;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
        }}
        .summary h2 {{
            color: #34495e;
            margin-top: 0;
        }}
        .severity-stats {{
            display: flex;
            gap: 20px;
            margin-top: 15px;
        }}
        .severity-item {{
            flex: 1;
            text-align: center;
            padding: 20px;
            border-radius: 8px;
            color: white;
            font-weight: bold;
        }}
        .high {{
            background: #e74c3c;
        }}
        .medium {{
            background: #f39c12;
        }}
        .low {{
            background: #27ae60;
        }}
        .vulnerabilities {{
            margin-bottom: 30px;
        }}
        .vuln-section {{
            margin-bottom: 30px;
        }}
        .vuln-section h3 {{
            color: #34495e;
            border-bottom: 2px solid #bdc3c7;
            padding-bottom: 10px;
        }}
        .vuln-item {{
            background: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 15px;
            border-left: 4px solid #e74c3c;
        }}
        .vuln-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }}
        .vuln-type {{
            font-weight: bold;
            color: #e74c3c;
            font-size: 1.1em;
        }}
        .severity-badge {{
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: bold;
            color: white;
        }}
        .severity-badge.high {{
            background: #e74c3c;
        }}
        .severity-badge.medium {{
            background: #f39c12;
        }}
        .severity-badge.low {{
            background: #27ae60;
        }}
        .vuln-details {{
            margin-bottom: 10px;
        }}
        .vuln-details strong {{
            color: #2c3e50;
        }}
        .evidence {{
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            border-radius: 5px;
            padding: 10px;
            margin-top: 10px;
            font-family: monospace;
            font-size: 0.9em;
        }}
        .no-vulns {{
            text-align: center;
            padding: 40px;
            color: #27ae60;
            font-size: 1.2em;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #ecf0f1;
            color: #7f8c8d;
        }}
        @media (max-width: 768px) {{
            .container {{
                padding: 15px;
            }}
            .severity-stats {{
                flex-direction: column;
            }}
            .info-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔒 Web Vulnerability Scan Report</h1>
            <p>Comprehensive security assessment of web application</p>
        </div>
        
        <div class="scan-info">
            <h2>📊 Scan Information</h2>
            <div class="info-grid">
                <div class="info-item">
                    <div class="info-label">Target URL</div>
                    <div class="info-value">{web_vuln_data.get('scan_info', {}).get('target', 'N/A')}</div>
                </div>
                <div class="info-item">
                    <div class="info-label">Scan Date</div>
                    <div class="info-value">{web_vuln_data.get('scan_info', {}).get('scan_date', 'N/A')}</div>
                </div>
                <div class="info-item">
                    <div class="info-label">Pages Scanned</div>
                    <div class="info-value">{web_vuln_data.get('scan_info', {}).get('total_pages_scanned', 0)}</div>
                </div>
                <div class="info-item">
                    <div class="info-label">Total Vulnerabilities</div>
                    <div class="info-value">{web_vuln_data.get('scan_info', {}).get('total_vulnerabilities', 0)}</div>
                </div>
            </div>
        </div>
        
        <div class="summary">
            <h2>📈 Vulnerability Summary</h2>
            <div class="severity-stats">
                <div class="severity-item high">
                    <div style="font-size: 2em;">{web_vuln_data.get('summary', {}).get('high_severity', 0)}</div>
                    <div>High Severity</div>
                </div>
                <div class="severity-item medium">
                    <div style="font-size: 2em;">{web_vuln_data.get('summary', {}).get('medium_severity', 0)}</div>
                    <div>Medium Severity</div>
                </div>
                <div class="severity-item low">
                    <div style="font-size: 2em;">{web_vuln_data.get('summary', {}).get('low_severity', 0)}</div>
                    <div>Low Severity</div>
                </div>
            </div>
        </div>
        
        <div class="vulnerabilities">
            <h2>🚨 Detailed Vulnerabilities</h2>
    """
    
    if not web_vuln_data.get('vulnerabilities'):
        html_content += """
            <div class="no-vulns">
                <h3>✅ No Vulnerabilities Found</h3>
                <p>Congratulations! No security vulnerabilities were detected during this scan.</p>
            </div>
        """
    else:
        # Group vulnerabilities by type
        vuln_types = {}
        for vuln in web_vuln_data.get('vulnerabilities', []):
            vuln_type = vuln.get('type', 'Unknown')
            if vuln_type not in vuln_types:
                vuln_types[vuln_type] = []
            vuln_types[vuln_type].append(vuln)
        
        for vuln_type, vulns in vuln_types.items():
            html_content += f"""
            <div class="vuln-section">
                <h3>{vuln_type}</h3>
            """
            
            for vuln in vulns:
                severity_class = vuln.get('severity', 'LOW').lower()
                html_content += f"""
                <div class="vuln-item">
                    <div class="vuln-header">
                        <div class="vuln-type">{vuln.get('type', 'Unknown')}</div>
                        <span class="severity-badge {severity_class}">{vuln.get('severity', 'LOW')}</span>
                    </div>
                    <div class="vuln-details">
                        <strong>URL:</strong> {vuln.get('url', 'N/A')}<br>
                        <strong>Description:</strong> {vuln.get('description', 'N/A')}<br>
                """
                
                # Add specific fields based on vulnerability type
                if vuln.get('parameter'):
                    html_content += f'<strong>Parameter:</strong> {vuln.get("parameter")}<br>'
                if vuln.get('payload'):
                    html_content += f'<strong>Payload:</strong> {vuln.get("payload")}<br>'
                if vuln.get('form_action'):
                    html_content += f'<strong>Form Action:</strong> {vuln.get("form_action")}<br>'
                if vuln.get('method'):
                    html_content += f'<strong>Method:</strong> {vuln.get("method")}<br>'
                if vuln.get('header'):
                    html_content += f'<strong>Header:</strong> {vuln.get("header")}<br>'
                if vuln.get('value'):
                    html_content += f'<strong>Value:</strong> {vuln.get("value")}<br>'
                
                html_content += """
                    </div>
                """
                
                if vuln.get('evidence'):
                    html_content += f"""
                    <div class="evidence">
                        <strong>Evidence:</strong> {vuln.get('evidence')}
                    </div>
                    """
                
                html_content += """
                </div>
                """
            
            html_content += """
            </div>
            """
    
    html_content += f"""
        </div>
        
        <div class="footer">
            <p>Report generated by Recon-Tool-Kit on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p>This report is for security assessment purposes only. Always obtain proper authorization before testing.</p>
        </div>
    </div>
</body>
</html>
    """
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return output_file

if __name__ == "__main__":
    # Example usage
    sample_data = {
        "scan_info": {
            "target": "https://example.com",
            "scan_date": "2024-01-01 12:00:00",
            "total_pages_scanned": 25,
            "total_vulnerabilities": 3
        },
        "vulnerabilities": [
            {
                "type": "SQL Injection",
                "url": "https://example.com/search?q=test",
                "parameter": "q",
                "payload": "' OR '1'='1",
                "severity": "HIGH",
                "description": "SQL injection vulnerability found in parameter 'q'",
                "evidence": "Error message containing 'sql syntax' detected"
            }
        ],
        "summary": {
            "high_severity": 1,
            "medium_severity": 0,
            "low_severity": 0
        }
    }
    
    output_file = generate_html_report(sample_data)
    print(f"HTML report generated: {output_file}")
