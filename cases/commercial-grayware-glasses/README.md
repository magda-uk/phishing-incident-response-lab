# Incident Report / Triage Note: Commercial Grayware (Optics Marketing Campaign)


<p align="left">
  <img src="https://img.shields.io/badge/Status-Classified_as_Grayware-00AEEF?style=flat-square&labelColor=black">
  <img src="https://img.shields.io/badge/Severity-Low-28a745?style=flat-square&labelColor=black">
  <img src="https://img.shields.io/badge/Classification-Email_Marketing-9b59ff?style=flat-square&labelColor=black">
  <img src="https://img.shields.io/badge/Platform-Mautic_Marketing-A9A9A9?style=flat-square&labelColor=black">
</p>

## 🟢 Executive Summary
During bulk triage operations, an incoming email promoting a commercial discount on eyewear ("Por solo 60€: renueva tus gafas...") was processed. 

Unlike active credential harvesting campaigns, static analysis and header inspection confirmed this email to be commercial **Grayware** (unsolicited marketing spam) rather than a malicious threat. 

## 🟢 Email & Header Triage
-   **Subject:** Por solo 60€: renueva tus gafas por menos de lo que imaginas
-   **From:** Doble Pack Gafas `<info@crm.lightofwork.com>`
-   **To:** Victim Address (`mdxxxxxx@yahoo.es`)
-   **Return-Path:** `<msprvs1=20730e3251QZP=bounces-17005-9@crm.lightofwork.com>`
-   **Message-ID:** `<8a7028ab01c4ef3f0e5229f6724b69f0@crm.lightofwork.com>`

* **Infrastructure Observations:**
  *   **Mass-Mailing Platform:** The `Return-Path` pattern (`msprvs1=...bounces-...`) indicates the use of an external Email Service Provider (ESP) or bulk distribution infrastructure.
  *   **Domain Consistency:** Unlike spoofed phishing lures, the sender domain (`lightofwork.com`) matches the routing and infrastructure domains.

## 🟢 Link & Source Code Analysis
Inspection of the raw HTML source code revealed the tracking and redirection structure:
-   **Sample Link:** `href="https://m1.lightofwork.com/email/view/6ab8ba8bde91e012057680"`
-   **Attribution:** The presence of `mautic:disable-tracking="true"` attributes in the code confirms the use of **Mautic**, an open-source marketing automation platform. 

## 🟢 Conclusion & Recommendation
*   **Classification:** False positive / Non-malicious commercial spam. 
*   **Action:** No threat containment or indicator blocking required. Recommended for standard newsletter unsubscription or user-level spam reporting if unwanted.


## 🟢 Connect with me
[![Magda Dominguez LinkedIn](https://img.shields.io/badge/Magda_Dominguez-Connect_on_LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=000000)](https://www.linkedin.com/in/magda-d-infosec)

I am actively seeking a Cyber Security / SOC / Security Design role where I can bring my structured troubleshooting, log analysis, and secure architecture skills to a dedicated security team.