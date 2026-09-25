# 🔰 Phishing Incident Response Lab (Email Triage & Artefacts)

This repository serves as a dedicated laboratory for analysing phishing campaigns, malicious artefacts, and end‑to‑end incident response workflows. It is designed to demonstrate practical, real‑world Blue Team skills focused on email security, threat actor infrastructure analysis, and safe triage methodologies.

Phishing remains a primary initial access vector. This lab moves beyond theory, applying strict SOC evidence-handling procedures to investigate live, real-world malicious emails.

---

## 🟨 Featured Investigations

The core of this repository consists of detailed, step-by-step analyses of captured phishing attempts. 

* 📄 **[Artefact Triage: Suspicious Santander / inFakt Invoice](./artifacts/suspicious-invoice-santander/pdf-analysis.md)**

  Safe static analysis of a malicious PDF masquerading as a financial document. Includes fraud indicator mapping, social engineering breakdown, and expected sandbox detonation behaviour.
* 📧 **[Campaign Breakdown: Real Phishing Case (Santander/inFakt)](./headers/suspicious-email-real-case.md)**

  Full investigation of the email body, extracting malicious routing hops, external domain IoCs (`limes-plus.com`), and identifying the mass-targeting footprint.
* 🕵️ **[Email Header Analysis: Microsoft Support Spoofing](./headers/spoofing-analysis.md)**

  Deep-dive into a credential harvesting campaign. Demonstrates the identification of forged senders via SPF, DKIM, and DMARC alignment failures, alongside return-path mismatches.

---

## 🟨 Tools & Investigative Methodology

These investigations utilise standard SOC analyst toolsets to extract Indicators of Compromise (IoCs) and validate threat intelligence:

* **Email Header Inspection:** Outlook / Thunderbird raw header extraction.
* **DNS & Routing Validation:** MxToolbox (SPF, DKIM, DMARC, IP reputation).
* **Artefact Detonation & Sandbox:** ANY.RUN, Hybrid Analysis, Joe Sandbox.
* **File & URL Reputation:** VirusTotal.
* **Deobfuscation:** CyberChef.

---

## 🟨 Security & Evidence Handling

To maintain a secure laboratory environment, all investigations adhere to strict incident response protocols:
* All artefacts are handled exclusively within isolated environments or via **GitHub’s safe static preview**.
* No local execution of attachments or scripts.
* Evidence is preserved in structured, quarantined directories.

---

## 🟨 Repository Structure

```text
phishing-incident-response-lab/
│
├── headers/                      # Email routing and spoofing investigations
│   ├── suspicious-email-real-case.md
│   ├── spoofing-analysis.md
│   └── images/
│
├── artifacts/                    # Safe static analysis of malicious files
│   └── suspicious-invoice-santander/
│       ├── Invoice Actualizacion de seguridad de cuenta.pdf
│       ├── pdf-analysis.md
│       └── images/
│
├── automation/                   # (In Development) Python triage tools
│   ├── eml-parser.py
│   └── ioc-extractor.py
│
└── case-studies/                 # (In Development) Campaign mapping
    ├── credential-harvesting.md
    └── mfa-fatigue-scenarios.md
```
---
## ♻️ Active Development Roadmap
This laboratory is continuously updated with new artefacts and automated triage capabilities. 

Current priorities include:

* Integrating Sigma rules to detect malicious email forwarding and inbox rules.

* Developing Python automation scripts to parse raw .eml files and auto-extract IoCs.

* Expanding cases to cover QR code phishing (Quishing) and Business Email Compromise (BEC) attempts.
---