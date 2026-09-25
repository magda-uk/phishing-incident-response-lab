# Email Header Analysis 
 # Spoofing Attempt

## 🧩 Overview
This case demonstrates how to identify a spoofed email using header analysis.  
The email claims to be from “Microsoft Support”, but the headers reveal a forged sender.

---

## 📧 Email Summary
- **Subject:** Important security update required  
- **Display Name:** Microsoft Support  
- **From:** security-update@microsoft-support.com  
- **To:** magda@company.com  
- **Attachment:** None  
- **Link:** “Verify your account”

---

## 🕵️ Header Findings

### 1. **SPF: FAIL**
Received-SPF: fail (domain of microsoft-support.com does not designate 185.203.112.55 as permitted sender)
The sending IP is not authorised by the domain.

### 2. **DKIM: None**
Legitimate Microsoft emails always include DKIM signatures.

### 3. **DMARC: FAIL**
The sending IP is not authorised by the domain.

DMARC: fail (p=reject)

The domain explicitly rejects unauthorised senders.

### 4. **Return-Path mismatch**
Return-Path: mailto:noreply@randomhost.ru (randomhost.ru in Bing)
Classic sign of spoofing.

### 5. **Received chain anomaly**
The first hop originates from:

185.203.112.55 (AS: suspicious hosting provider)


---

## 🔍 Analysis
Indicators of spoofing:
- SPF fail  
- DMARC fail  
- No DKIM  
- Return-path mismatch  
- Suspicious sending IP  
- Domain similar to Microsoft but not legitimate  

The email attempts to impersonate Microsoft to deliver a credential-harvesting link.

---

## 🛡 Recommended Response
1. Block sender domain.  
2. Block sending IP.  
3. Add domain to phishing indicators list.  
4. Notify user and security team.  
5. Review logs for any clicks on the link.  

---

## 📝 Conclusion
This is a clear spoofing attempt designed to steal credentials.  
Header analysis alone is sufficient to classify the email as malicious.

---

## 🔺 Author
Magda Dominguez

SOC Analyst (L1-ready) Bristol, UK

Focused on Blue Team operations, detection engineering and log analysis.
