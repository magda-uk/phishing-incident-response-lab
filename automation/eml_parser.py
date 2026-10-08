# eml-parser.py
import email
from email import policy
import os

def parse_eml(file_path):
    if not os.path.exists(file_path):
        print(f"[-] Error: File {file_path} not found")
        return None

    print(f"[*] Analysing: {file_path}\n" + "-"*40)

    # Open and read the .eml file applying the standard email policy
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        msg = email.message_from_file(f, policy=policy.default)

    # 1. Extract Metadata and Key Headers
    headers_to_extract = ['Subject', 'From', 'To', 'Date', 'Return-Path', 'Message-ID']
    extracted_data = {"headers": {}, "body": "", "attachments": []}

    print("[+] MAIN HEADERS:")
    for header in headers_to_extract:
        val = msg.get(header, 'Not found')
        extracted_data["headers"][header] = val
        print(f"    {header}: {val}")

    # 2. Extract Message Body and Attachments
    for part in msg.walk():
        # Skip multipart container parts
        if part.is_multipart():
            continue
            
        content_type = part.get_content_type()
        content_disposition = str(part.get("Content-Disposition"))

        # Extract text (could be plain text or HTML, where phishing URLs often hide)
        if "attachment" not in content_disposition:
            if content_type == "text/plain" or content_type == "text/html":
                payload = part.get_payload(decode=True)
                if payload:
                    text = payload.decode(part.get_content_charset() or 'utf-8', errors='ignore')
                    extracted_data["body"] += text

        # Log attachment filenames (e.g., malicious PDFs)
        if "attachment" in content_disposition or part.get_filename():
            filename = part.get_filename()
            if filename:
                extracted_data["attachments"].append(filename)

    print("\n[+] ATTACHMENTS FOUND:")
    if extracted_data["attachments"]:
        for att in extracted_data["attachments"]:
            print(f"    - {att}")
    else:
        print("    None")

    print("\n[+] EXTRACTED BODY LENGTH:")
    print(f"    {len(extracted_data['body'])} characters ready for IoC analysis.")

    return extracted_data

if __name__ == "__main__":
    # To test this, create a simple text file named 'test.eml' in the same folder
    # or point the path to one of the emails in your 'headers/' folder
    test_file = "headers/suspicious-email-real-case.eml"
    
    # Uncomment the following line and create a test file to run it
    # parse_eml(test_file)