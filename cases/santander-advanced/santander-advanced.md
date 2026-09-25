# Case study : Santander spoofed security update (advanced analysis)

## 1. Overview

This case study documents an advanced technical analysis of a phishing email impersonating Santander, including:

- header and body analysis,
- URL and domain analysis,
- PDF attachment triage,
- IoC extraction,
- tooling (VirusTotal, CyberChef, sandbox).

---

## 2. Email summary

- **From (display):** SantanderEquipo, Inc.
- **From (address):** uzytkownicy@infakt.pl
- **Subject:** Actualización de seguridad de cuenta
- **Body (key lines):**
  - “estamos actualizando nuestro sistema de seguridad.”
  - “Por favor, actualice su información de cuenta haciendo clic aquí:”
  - Link: `https://limes-plus.com/`
  - “Invoice in PDF format is attached to this message.”

The email combines a “security update” theme with an attached invoice to increase urgency and perceived legitimacy.

---

## 3. Technical artefacts

- **URL:** `https://limes-plus.com/`
- **Domain:** `limes-plus.com`
- **Attachment:** `Invoice Actualizacion de seguridad de cuenta.pdf`
- **Message ID:** `<80e64edf394b9cc28266b09e9d20a56ea30a3c649e5a52772410d4044594@mail.app.infakt.pl>`

---

## 4. Advanced analysis components

- **URL analysis (CyberChef):**
  - Parsed scheme, host, path.
  - Confirmed root domain `limes-plus.com` unrelated to Santander.

- **Domain reputation (VirusTotal):**
  - Checked `limes-plus.com` for known malicious activity.
  - Treated as phishing domain based on context.

- **PDF analysis (VirusTotal + local hashing):**
  - Generated SHA256.
  - Uploaded to VT for static analysis.
  - Identified as fraudulent invoice used for social engineering.

- **Sandbox expectations (ANY.RUN):**
  - URL likely leads to phishing login or credential‑harvesting page.
  - Sandbox run would reveal additional IoCs (secondary domains, IPs, scripts).

---

## 5. IoCs

See `ioc/santander-iocs.json` for structured IoCs, including:

- sender address,
- domains,
- URL,
- attachment filename and hash,
- campaign metadata.

---

## 6. Conclusion

This case demonstrates how a seemingly simple phishing email (“security update” + invoice) can be analysed with BLT‑level tooling:

- VirusTotal for files and domains,
- CyberChef for URL parsing,
- sandbox for behavioural insight,
- structured IoC extraction.

