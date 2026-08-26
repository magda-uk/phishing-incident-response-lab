# 🛡️ Phishing Incident Response Lab (Email Triage & Artefacts)

This repository contains my dedicated laboratory for analysing phishing emails, malicious artefacts, and end‑to‑end incident response workflows.  
It complements my SOC Analyst Portfolio by showcasing specialised Blue Team skills focused on email security, artefact triage, and investigative methodology.

---

## 🎯 Purpose

To demonstrate practical, real‑world skills in:

- Email header analysis (SPF, DKIM, DMARC alignment, routing hops)
- Malicious artefact triage (PDF, HTML, EML)
- URL and attachment analysis
- Sandbox investigation (ANY.RUN, VirusTotal, Hybrid Analysis)
- IoC extraction and reporting
- Python automation for email triage and artefact parsing

Phishing remains one of the most common initial access vectors, making these skills essential within modern SOC environments.

---

## 🔵 Blue Team Focus

This project forms part of my ongoing development within the **Blue Team (BLT)**, where my primary focus includes:

- Detection engineering  
- Investigation and incident response  
- Artefact triage  
- Email security and phishing analysis  
- Evidence handling and documentation  

Although BLT is my main area of interest, I also explore complementary fields such as:

- Threat hunting  
- Malicious artefact analysis  
- Detection logic and rule creation  
- Technical documentation of incidents  

This repository reflects that blend:  
**real phishing cases** documented using BLT methodology, including email header analysis, artefact triage, and safe static examination of suspicious PDFs.

---

## 📁 Repository Structure
```
phishing-incident-response-lab/
│
├── headers/
│   ├── suspicious-email-real-case.md
│   ├── spoofing-analysis.md
│   ├── README.md
│   └── images/
│       ├── email-overview.png
│       └── email-header.png
│
├── artifacts/
│   └── suspicious-invoice-santander/
│       ├── Invoice Actualizacion de seguridad de cuenta.pdf
│       ├── pdf-analysis.md
│       ├── README.md
│       └── images/
│           └── pdf-preview-github.png
│
├── automation/   (planned)
│   ├── eml-parser.py
│   ├── ioc-extractor.py
│   ├── spf-dkim-validator.py
│
├── case-studies/ (planned)
│   ├── credential-harvesting.md
│   ├── invoice-themed-phishing.md
│   ├── bec-attempt.md
```

---
## 🧰 Tools Used (current and planned)

These tools form part of the laboratory’s workflow for email triage, artefact analysis and phishing investigation:

- MxToolbox (SPF, DKIM, DMARC, DNS lookups)
- ANY.RUN (dynamic sandbox detonation)
- VirusTotal (file and URL reputation)
- Hybrid Analysis (static and dynamic artefact analysis)
- CyberChef (decoding, deobfuscation, data extraction)
- Python (automation scripts for EML parsing and IoC extraction)
- Outlook / Thunderbird (email header inspection)


---

## 🔒 Security Approach

- All artefacts opened **only via GitHub’s safe preview**  
- No local execution of attachments  
- Analysis follows SOC triage methodology  
- Evidence stored in structured folders  
- Markdown documentation for reproducibility  

---
## 📌 Progress So Far
This laboratory is currently in its early stages.
So far, I have completed:

✔  A full analysis of a real phishing email I received

✔  Documentation of spoofing indicators

✔  Email header investigation (routing hops, sender metadata, domain inspection)

✔  Safe triage of the attached PDF artefact

✔  Structured documentation following SOC methodology

✔ A clean and professional folder structure for future cases

---
## 📈 Planned Work

- Add HTML and EML artefact triage cases  
- Add a “Case Index” section  
- Expand with further phishing scenarios (QR phishing, credential harvesting, MFA fatigue)  
- Add Sigma rules for detection  
- Add YARA rules for artefact triage  
- Add Python automation scripts for EML parsing and IoC extraction  
- Add sandbox detonation reports for dynamic analysis  
