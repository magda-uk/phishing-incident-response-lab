# 🔰 Phishing Incident Response Lab (Email Triage & Artefacts)

This repository serves as a dedicated laboratory for analysing phishing campaigns, malicious artefacts, and end‑to‑end incident response workflows. It is designed to demonstrate practical, real‑world Blue Team skills focused on email security, threat actor infrastructure analysis, and safe triage methodologies.

Phishing remains a primary initial access vector, but it is often just the first step in a broader attack chain (incorporating Spoofing, Credential Harvesting, and MFA Fatigue). This lab moves beyond theory, applying strict SOC evidence-handling procedures to investigate live, real-world malicious emails.

---

## 🟨 Featured Incident Reports

The core of this repository consists of detailed, step-by-step incident reports of captured phishing attempts, consolidated into single pane-of-glass investigations.

- 📧 **[Case: Santander / inFakt Invoice Campaign](./cases/santander-invoice-phishing/incident-report.md)**
  Full investigation of a mass-targeted credential harvesting campaign. Includes email header analysis, extraction of malicious routing hops, external domain IoCs (`limes-plus.com`), and safe static analysis of a fraudulent PDF invoice used for social engineering.

- 🕵️ **[Case: Microsoft Support Spoofing](./cases/microsoft-support-spoofing/incident-report.md)**
  Deep-dive into a credential harvesting lure. Demonstrates the identification of forged senders via SPF, DKIM, and DMARC alignment failures, alongside return-path mismatches and IP reputation analysis.

---

## 🟨 Tools & Investigative Methodology

These investigations utilise standard SOC analyst toolsets to extract Indicators of Compromise (IoCs) and validate threat intelligence:
- **Python Automation:** Custom scripts to parse raw `.eml` files and auto-extract IP, URL, and email IoCs.
- **Email Header Inspection:** Outlook / Thunderbird raw header extraction.
- **DNS & Routing Validation:** MxToolbox (SPF, DKIM, DMARC, IP reputation).
- **Artefact Detonation & Sandbox:** ANY.RUN, Hybrid Analysis, Joe Sandbox.
- **File & URL Reputation:** VirusTotal.
- **Deobfuscation:** CyberChef.

---

## 🟨 Security & Evidence Handling

To maintain a secure laboratory environment, all investigations adhere to strict incident response protocols:
- All artefacts are handled exclusively within isolated environments or via **GitHub’s safe static preview**.
- No local execution of attachments or scripts.
- Raw `.eml` files and malicious PDFs are strictly quarantined locally and ignored via `.gitignore`.

---

## 🟨 Repository Structure

```text
phishing-incident-response-lab/
│
├── automation/                      # Custom Python triage tools
│   ├── eml_parser.py
│   ├── ioc_extractor.py
│   └── triage.py
│
├── cases/                           # Consolidated Incident Reports
│   ├── santander-invoice-phishing/
│   │   ├── incident-report.md
│   │   ├── santander-iocs.json
│   │   └── images/
│   │
│   ├── microsoft-support-spoofing/
│   │   ├── incident-report.md
│   │   └── images/
│   │
│   ├── credential-harvesting-scenarios/  # (In Development)
│   ├── mfa-fatigue-scenarios/            # (In Development)
│   ├── quishing-campaigns/               # (In Development)
│   └── bec-attempts/                     # (In Development)
│
└── raw_emails/                      # (Local Quarantine) Live .eml files
```
## ♻️ Active Development Roadmap

This laboratory is continuously updated with new artefacts and automated triage capabilities. 

Current priorities include:

* Developing Python automation scripts to parse raw .eml files and auto-extract IoCs (Completed & Testing).

* Expanding incident reports to cover QR code phishing (Quishing) and Business Email Compromise (BEC) attempts.

* Mapping Credential Harvesting campaigns to subsequent MFA Fatigue attacks.

* Integrating Sigma rules to detect malicious email forwarding and inbox rules.

---

`> whoami`
**Magda Dominguez** • Cyber & Data Specialist (CISMP | SC-900)

`> connect`
[LinkedIn](www.linkedin.com/in/magda-d-infosec) | [GitHub](https://github.com/magda-uk)