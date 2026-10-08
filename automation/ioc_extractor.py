import re

def extract_iocs(text_content):
    """
    Scans a block of text (email body or headers) 
    and extracts Indicators of Compromise (IoCs) using Regex.
    """
    print("[*] Starting IoC extraction...\n" + "-"*40)
    
    iocs = {
        "ipv4": [],
        "urls": [],
        "emails": []
    }

    # 1. Regex for IPv4 Addresses (Basic)
    # Filters standard IP format (e.g., 192.168.1.1)
    ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    
    # 2. Regex for full URLs (http / https)
    # Catches links like https://limes-plus.com/ or variations with parameters
    url_pattern = r'(?i)\b(?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’])'
    
    # 3. Regex for Email Addresses
    # Crucial for catching malicious "Reply-To" addresses (e.g., mouhisenm333@icloud.com)
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

    # Execute searches and remove duplicates using set()
    iocs["ipv4"] = list(set(re.findall(ipv4_pattern, text_content)))
    
    # The complex URL regex may return tuples; extract only the first group (the full URL)
    urls_raw = re.findall(url_pattern, text_content)
    if urls_raw:
        # Depending on the regex engine, it sometimes returns lists of tuples. We ensure we extract the string.
        iocs["urls"] = list(set([match[0] if isinstance(match, tuple) else match for match in urls_raw]))
    
    iocs["emails"] = list(set(re.findall(email_pattern, text_content)))

    # Print the results
    print("[+] IP Addresses found:")
    for ip in iocs["ipv4"]:
        print(f"    - {ip}")
        
    print("\n[+] URLs / Domains found:")
    for url in iocs["urls"]:
        print(f"    - {url}")
        
    print("\n[+] Email Addresses found:")
    for email in iocs["emails"]:
        print(f"    - {email}")

    return iocs

# --- Script Testing ---
if __name__ == "__main__":
    # Simulate the text that eml-parser.py would have returned from the email that I got.
    simulated_parser_text = """
    Return-Path: <uzytkownicy@infakt.pl>
    Reply-To: mouhisenm333@icloud.com
    Subject: Invoice Actualizacion de seguridad de cuenta
    
    Estimado cliente,
    Por favor actualice su cuenta visitando https://limes-plus.com/login inmediatamente.
    Si tiene dudas contacte a support@santander-fake.com.
    IP de origen detectada en cabeceras: 185.199.108.153
    """
    
    results = extract_iocs(simulated_parser_text)