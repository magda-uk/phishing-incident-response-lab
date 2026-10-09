# 🔰 Phishing Incident Response Lab (Email Triage & Artefacts)
<p align="left">
  <img src="https://img.shields.io/badge/Operations-Blue_Team-0052CC?style=flat-square&labelColor=black">
  <img src="https://img.shields.io/badge/Automation-Python_3-3776AB?style=flat-square&logo=python&logoColor=white&labelColor=black">
  <img src="https://img.shields.io/badge/Status-Active_Development-28a745?style=flat-square&labelColor=black">
  <img src="https://img.shields.io/badge/Documentation-Markdown-000000?style=flat-square&logo=markdown&logoColor=white">
</p>


This repository serves as a dedicated laboratory for analysing phishing campaigns, malicious artefacts, and end‑to‑end incident response workflows. It is designed to demonstrate practical, real‑world Blue Team skills focused on email security, threat actor infrastructure analysis, and safe triage methodologies.

Phishing remains a primary initial access vector, but it is often just the first step in a broader attack chain (incorporating Spoofing, Credential Harvesting, and MFA Fatigue). This lab moves beyond theory, applying strict SOC evidence-handling procedures to investigate live, real-world malicious emails.

## 🟨 Incident Triage Dashboard

The core of this repository consists of detailed, step-by-step incident reports, categorized by threat severity to demonstrate a full spectrum of SOC analysis, from critical credential harvesting to benign commercial spam.

- 🔴 **[Case: Santander / inFakt Invoice Campaign](./cases/santander-invoice-phishing/incident-report.md)** <img src="https://img.shields.io/badge/Severity-High-critical?style=flat-square&labelColor=black" align="center">

  Full investigation of a mass-targeted credential harvesting campaign. Includes email header analysis, extraction of malicious routing hops, external domain IoCs (`limes-plus.com`), and safe static analysis of a fraudulent PDF invoice used for social engineering.

- 🟠 **[Case: NHS / Medicare Credential Harvesting](./cases/nhs-medicare-phishing/incident-report.md)** <img src="https://img.shields.io/badge/Severity-Medium-FF8C00?style=flat-square&labelColor=black" align="center">

  Detailed credential harvesting investigation targeting victims with a fake "Free Medicare Kit" lure. Analyzes advanced evasion techniques, including the abuse of legitimate Google Cloud Storage (`storage.googleapis.com`) for payload hosting, DGA return-path routing, and manual extraction of Base64-tracked URLs hidden within HTML attributes.

- 🟢 **[Case: Optics Email Marketing (Grayware)](./cases/commercial-grayware-glasses/incident-report.md)** <img src="https://img.shields.io/badge/Severity-Low_/_Spam-28a745?style=flat-square&labelColor=black" align="center">

  Routine triage of a bulk email campaign. Demonstrates the ability to quickly filter out false positives and non-malicious commercial grayware by identifying legitimate marketing platforms (Mautic) and clean routing infrastructure, preventing alert fatigue.



## 🐍 Python Automation Engine (Bulk Triage)

To streamline the initial analysis phase and eliminate repetitive tasks, this laboratory features a custom-built Python automation toolkit designed to process raw evidence in bulk:

- **`eml_parser.py`**: Safely parses raw `.eml` files, extracting core metadata, headers (Return-Path, Subject, From, Message-ID), and identifying attachments.
- **`ioc_extractor.py`**: Utilizes advanced Regular Expressions (RegEx) to automatically scan text contents and harvest Indicators of Compromise (IoCs), including IPv4 addresses, URLs/domains, and email addresses.
- **`triage.py`**: The orchestration script. It loops through the `raw_emails/` queue, runs the parser and extractor sequentially, and generates a structured master investigation report (`artifacts/triage_report.json`).


## 🟨 Tools & Investigative Methodology

These investigations utilise standard SOC analyst toolsets to extract Indicators of Compromise (IoCs) and validate threat intelligence:
- **Email Header Inspection:** Outlook / Thunderbird raw header extraction.
- **DNS & Routing Validation:** MxToolbox (SPF, DKIM, DMARC, IP reputation).
- **Artefact Detonation & Sandbox:** ANY.RUN, Hybrid Analysis, Joe Sandbox.
- **File & URL Reputation:** VirusTotal.
- **Deobfuscation:** CyberChef.



## 🟨 Security & Evidence Handling

To maintain a secure laboratory environment, all investigations adhere to strict incident response protocols:
- All artefacts are handled exclusively within isolated environments or via **GitHub’s safe static preview**.
- No local execution of attachments or scripts.
- Raw `.eml` files and malicious PDFs are strictly quarantined locally and ignored via `.gitignore`.





## 🟨 Repository Structure

```text
phishing-incident-response-lab/
│
├── automation/                          # Custom Python triage tools
│   ├── eml_parser.py
│   ├── ioc_extractor.py
│   └── triage.py
│
├── cases/                               # Consolidated Incident Reports
│   ├── santander-invoice-phishing/      # High Severity
│   │   ├── incident-report.md
│   │   ├── santander-iocs.json
│   │   └── images/
│   │
│   ├── nhs-medicare-phishing/           # Medium Severity
│   │   ├── incident-report.md
│   │   └── images/
│   │
│   └── commercial-grayware-glasses/     # Low Severity (Grayware)
│       └── incident-report.md
│
└── raw_emails/                          # (Local Quarantine) Live .eml files
```
## ♻️ Active Development Roadmap

This laboratory is continuously updated with new artefacts and automated triage capabilities. 

Current priorities include:

* Developing Python automation scripts to parse raw .eml files and auto-extract IoCs (Completed & Testing).

* Expanding incident reports to cover QR code phishing (Quishing) and Business Email Compromise (BEC) attempts.

* Mapping Credential Harvesting campaigns to subsequent MFA Fatigue attacks.

* Integrating Sigma rules to detect malicious email forwarding and inbox rules.


## 🟩Connect with me

[![Magda Dominguez LinkedIn](https://img.shields.io/badge/Magda_Dominguez-Connect_on_LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=000000)](https://www.linkedin.com/in/magda-d-infosec)

I am actively seeking a Cyber Security / SOC / Security Design role where I can bring my structured troubleshooting, log analysis, and secure architecture skills to a dedicated security team.