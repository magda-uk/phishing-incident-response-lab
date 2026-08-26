phishing-incident-response-lab (Email Triage & Artifacts)

Focus: End-to-end phishing incident response, header analysis, and malicious artifact triage.

Content:

Email header investigation (SPF, DKIM, DMARC alignment, and routing hops).

Python automation script to parse .eml files and extract suspicious URLs and file hashes.

Sandbox detonation reports (VirusTotal, Any.Run, Hybrid Analysis) documenting discovered Indicators of Compromise (IoCs).

=========================================================================================================================

# Phishing Incident Response Lab

This repository contains my dedicated laboratory for analysing phishing emails, malicious artefacts, and end‑to‑end incident response workflows.  
It complements my SOC Analyst Portfolio by showcasing specialised IR skills focused on email security.

## 🎯 Purpose
To demonstrate practical skills in:
- Email header analysis (SPF, DKIM, DMARC)
- Malicious artefact triage (PDF, HTML, EML)
- URL and attachment analysis
- Sandbox investigation (ANY.RUN, Joe Sandbox)
- IoC extraction and reporting
- Python automation for email triage

## 📁 Repository Structure
```
phishing-incident-response-lab/
│
├── headers/
│   ├── spoofing-analysis.md
│   ├── compromised-account.md
│
├── artifacts/
│   ├── pdf-malicious.md
│   ├── html-smuggling.md
│   ├── eml-analysis.md
│
├── automation/
│   ├── eml-parser.py
│   ├── ioc-extractor.py
│   ├── spf-dkim-validator.py
│
├── case-studies/
│   ├── credential-harvesting.md
│   ├── invoice-themed-phishing.md
│   ├── bec-attempt.md
```


## 🔧 Tools Used
- MxToolbox
- ANY.RUN
- Joe Sandbox
- Python
- Outlook / Thunderbird
- CyberChef

## 📌 Notes
This repository will expand with new phishing cases, artefact analyses, and automation scripts.
