# Santander phishing case : PDF attachment analysis (VirusTotal)

## 1. Attached file

- **Filename:** `Invoice Actualizacion de seguridad de cuenta.pdf`
- **Context:** Sent as part of a spoofed Santander “security update” email.
- **Claimed purpose:** “Invoice in PDF format is attached to this message.”

---

## 2. Hashing (local step)

Locally, generate:

- `SHA256` of the PDF.
- Optionally `SHA1` and `MD5`.

Example (Linux):

```bash
sha256sum "Invoice Actualizacion de seguridad de cuenta.pdf"
```
## 3. VirusTotal file analysis (conceptual workflow)
Steps:

1. Upload the PDF to VirusTotal.

2. Review:

- Detection ratio.

- File type and metadata.

- Embedded URLs or domains.

- Behavioural / static analysis.

Expected outcomes for a social‑engineering PDF:

- Often 0 detections (no active malware).

- Metadata may show generic or suspicious generator.

- Content is fraudulent but not technically malicious.

## 4. Indicators of fraud (content‑level)
Even if VT shows no malware:

- Filename uses “Actualización de seguridad de cuenta” to create urgency.

-The PDF is unsolicited and unrelated to any real Santander process.

-The email body instructs the user to trust and open the attachment.

-The invoice data (seller, buyer, service) is nonsensical and clearly fabricated.

## 5. IoCs (file)
- Filename: Invoice Actualizacion de seguridad de cuenta.pdf

- SHA256: <insert real hash here>

- Type: PDF document.

- Usage: social‑engineering artefact in phishing campaign.

## 6. Conclusion
The PDF is a malicious artefact in a phishing campaign, used to add legitimacy and pressure to the spoofed Santander email. Even if VirusTotal reports no malware, the file is fraudulent and should be treated as part of the phishing incident.


---

### `ioc/santander-iocs.json`

```json
{
  "case": "Santander spoofed security update",
  "email": {
    "from_display": "SantanderEquipo, Inc.",
    "from_address": "uzytkownicy@infakt.pl",
    "subject": "Actualización de seguridad de cuenta",
    "message_id": "<80e64edf394b9cc28266b09e9d20a56ea30a3c649e5a52772410d4044594@mail.app.infakt.pl>",
    "date": "2026-08-16T18:04:00"
  },
  "urls": [
    {
      "raw": "https://limes-plus.com/",
      "defanged": "hxxps://limes-plus[.]com/",
      "domain": "limes-plus.com"
    }
  ],
  "domains": [
    "limes-plus.com",
    "infakt.pl"
  ],
  "files": [
    {
      "filename": "Invoice Actualizacion de seguridad de cuenta.pdf",
      "sha256": "<insert_real_sha256_here>",
      "type": "pdf",
      "role": "phishing invoice / social engineering artefact"
    }
  ],
  "campaign": {
    "theme": "Santander account security update",
    "language": "Spanish",
    "lure": "security update + invoice",
    "targets": [
      "sbbdbs",
      "haroldisla29",
      "vanesiina1991",
      "mikelllorensbiosca",
      "victorsuarez11"
    ]
  }
}
```