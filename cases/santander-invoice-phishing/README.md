# Incident Report: Santander Spoofed Security Update
<p align="left">
  <img src="https://img.shields.io/badge/Status-Investigated-00AEEF??style=flat-square&labelColor=black">
  <img src="https://img.shields.io/badge/Severity-High-critical?style=flat-square&labelColor=black">
  <img src="https://img.shields.io/badge/Vector-Email-9b59ff??style=flat-square&labelColor=black">
  <img src="https://img.shields.io/badge/MITRE_ATT%26CK-T1566.001_(Phishing)-4B0082?style=flat-square&labelColor=black">
  <img src="https://img.shields.io/badge/Artefact-Malicious_PDF-1a0066??style=flat-square&labelColor=black">
</p>

## 🔹Executive Summary
This case involves a real-world phishing campaign impersonating Santander ("SantanderEquipo, Inc."). The attacker leveraged a legitimate Polish invoicing service (`infakt.pl`) to spoof the delivery mechanism and bypass basic spam filters. The primary objective is credential harvesting via a malicious external link, using a fabricated PDF invoice as a psychological trigger to create urgency.

## 🔹Email & Header Triage
*   **Subject:** Invoice Actualizacion de seguridad de cuenta
*   **From:** SantanderEquipo, Inc. <uzytkownicy@infakt.pl>
*   **Reply-To:** mouhisenm333@icloud.com
*   **Message-ID:** `<80e64edf394b9cc28266b09e9d20a56ea30a3c649e5a52772410d4044594@mail.app.infakt.pl>`
*   **Recipients:** Multiple unrelated victims (Mass-targeting).

* **Email Overview & Headers:**
![Email overview](./images/email-overview.png)
![Header details](./images/email-header.png)

* **Spoofing & Evasion Indicators:**
  *   **Domain Mismatch:** The sender domain (`infakt.pl`) completely contradicts the display name (Santander).
  *   **Suspicious Reply-To:** Diverts replies to a personal iCloud email, a classic operational security failure by the threat actor.

## 🔹Indicators of Compromise (IOCs)
Extracted artifacts identified during the initial triage for threat intelligence lookups and SIEM log searches.

| IOC Type | IOC Value | Source | Description | Risk Level |
| :--- | :--- | :--- | :--- | :--- |
| **Sender Email** | `uzytkownicy@infakt.pl` | Email Header | Compromised or abused legitimate invoicing service | High |
| **Reply-To** | `mouhisenm333@icloud.com` | Email Header | Attacker-controlled personal email address | High |
| **Message-ID** | `<80e64edf394b9cc28266b09...>` | Email Header | Unique message identifier | Medium |
| **URL (Visible)** | `http://limes-plus.com/` | Email Body | Fake security update landing page | High |
| **Domain** | `limes-plus.com` | Email Body | Root domain with no Santander affiliation | High |
| **IP Address** | `172.67.213.19` | VirusTotal / DNS | Resolved IP of the malicious domain | High |
| **Attachment Name**| `Invoice Actualizacion de seguridad de cuenta.pdf` | Attachment | Suspicious attachment acting as a social engineering lure | High |
| **Attachment Hash**| `8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92`* | Attachment | SHA256 hash of the PDF attachment | High |

*\* Note: The provided SHA-256 hash is a simulated placeholder. The original malicious artefact was permanently destroyed post-analysis in accordance with strict laboratory quarantine protocols.*

## 🔹URL & Infrastructure Analysis
The email body instructs the user to update their account security by visiting an external link.

- **Deobfuscation & Defanging (CyberChef):**
  To safely analyze and document the malicious link, the raw URL was processed through CyberChef.
  *   **Raw URL:** `http://limes-plus.com/`
  *   **Defanged Output:** `hxxp://limes-plus[.]com/`

   ![CyberChef Defang URL](./images/defang.png)

- **HTTP Header & Infrastructure Analysis:**
  Direct interrogation of the landing page's HTTP response (`hxxps://limes-plus[.]com/index.php/lp/en`) revealed critical infrastructure details:
  
  *   **Compromised Legitimate Server:** The HTML meta tags explicitly returned `generator: Open Journal Systems 3.5.0.5`. This confirms the domain is a legitimate academic publishing platform that has been compromised by the threat actor to host the phishing directory.
  
  ![HTML Meta Tags - OJS Generator](./images/html-meta-ojs.png)

  *   **CDN Masking:** HTTP headers (`server: cloudflare`) indicate the infrastructure is routed through Cloudflare, masking the true origin IP and providing a layer of evasion against automated security scanners. The server is running `PHP/8.2.34` powered by `LiteSpeed`.

  ![HTTP Headers - Cloudflare & LiteSpeed](./images/http-headers-cloudflare.png)

- **Threat Intelligence (VirusTotal & Evasion):**
  *   **VirusTotal Scan:** The root domain currently has a clean reputation score (0/93 malicious detections). 

  ![VirusTotal - Clean Domain Score](./images/virustotal-clean-score.png)

  *   **Analyst Assessment:** This lack of detection highlights a critical security evasion tactic. By hijacking a legitimate academic domain with an established positive reputation, the attacker successfully bypassed signature-based secure email gateways (SEGs) and automated URL filters. Relying strictly on OSINT reputation in this case would result in a false negative.
  *   **Sandbox Behavior:** Expected sandbox detonation behavior involves redirection to a credential-harvesting form masking as a banking portal. Sandbox captures should prioritize the final landing page HTML and secondary domains loaded during redirection.
  
## 🔹Attachment Triage (PDF)
*   **Filename:** `Invoice Actualizacion de seguridad de cuenta.pdf`
*   **Role:** Social Engineering Artefact

* **PDF Preview (Safe View):**


![PDF preview](./images/pdf-preview-github.png)


* **Static Analysis & VirusTotal Findings:**
  *   **Content:** The document mimics a Polish invoice generated via inFakt.pl but contains deliberately fabricated, nonsensical data (e.g., Seller: SpotifyRenew, Inc., Buyer: sbbdbs). 
  *   **VirusTotal Scan:** The PDF file was analyzed in VirusTotal using its SHA-256 hash. The results indicate that the file contains no active exploits or malware payloads (e.g., malicious macros or embedded scripts).
  *   **Conclusion:** The file's sole purpose is to reinforce the email's narrative, confusing the victim and increasing the likelihood of interaction with the phishing link.

## 🔹Defensive Recommendations
1.  **Network Blocking:** Blacklist the root domain `limes-plus.com` on all firewalls and web proxies.
2.  **Email Quarantine:** Implement a mail gateway rule to drop inbound traffic containing the Reply-To address `mouhisenm333@icloud.com`.
3.  **Log Review:** Query SIEM/Proxy logs for any internal IP addresses that successfully connected to the malicious URL to identify potential compromises.

## 🔹Let's connect

[![Magda Dominguez LinkedIn](https://img.shields.io/badge/Magda_Dominguez-Connect_on_LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=000000)](https://www.linkedin.com/in/magda-d-infosec)