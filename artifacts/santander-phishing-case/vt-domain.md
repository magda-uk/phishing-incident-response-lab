# Santander phishing case: domain reputation (VirusTotal)

## 1. Domain under analysis

- **Domain:** `limes-plus.com`

This domain appears in the phishing email as the target of the “security update” link.

---

## 2. VirusTotal lookup (conceptual workflow)

Steps:

1. Open VirusTotal.
2. Select “Domain”.
3. Submit: `limes-plus.com`.

Expected outputs:

- **Reputation:** may show “malicious”, “suspicious”, or “unknown”.
- **Detected URLs:** any known malicious URLs under this domain.
- **Communicating files:** malware samples contacting this domain.
- **Relations:** IPs, subdomains, URLs.
- **Historical WHOIS / DNS:** registration details, hosting.

---

## 3. Indicators of risk

Even if VT shows few detections:

- Domain is not associated with Santander.
- Domain appears only in phishing context.
- Domain is used in a “security update” lure.
- Domain is delivered via spoofed sender and fraudulent invoice.

---

## 4. IoCs (domain)

- **Domain:** `limes-plus.com`
- **Category:** phishing / suspicious (based on context).
- **Usage:** credential harvesting / phishing link in email.

---

## 5. Conclusion

Regardless of VirusTotal’s exact score, `limes-plus.com` should be treated as a phishing domain in this case, as it is used in a spoofed Santander email to lure victims into “updating” their account security.
