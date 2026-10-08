# Santander phishing case — URL analysis with CyberChef

## 1. Context

The phishing email impersonates Santander and instructs the recipient to “update their account security” by clicking a link:

`https://limes-plus.com/`

This URL is the primary lure used to harvest credentials or deliver further malicious content.

---

## 2. Defang and refang

**Defanged URL (for safe handling):**

`hxxps://limes-plus[.]com/`

In CyberChef:

- Operation: `Find / Replace`
- Replace `.` with `[.]`
- Replace `https` with `hxxps`

---

## 3. Parse URL and extract domain

Using CyberChef:

- Operation: `Parse URL`

Result:

- **Scheme:** `https`
- **Host:** `limes-plus.com`
- **Path:** `/`
- **Query:** *(none)*

Root domain:

- `limes-plus.com`

This does not match any legitimate Santander domain (e.g. `santander.co.uk`, `santander.com`).

---

## 4. Indicators of phishing

- Host is unrelated to Santander.
- Generic domain name with no clear brand association.
- Used in a context of “security update” and “account verification”.
- Delivered via a spoofed sender claiming to be “SantanderEquipo, Inc.”.

---

## 5. IoCs (URL)

- **URL (defanged):** `hxxps://limes-plus[.]com/`
- **Root domain:** `limes-plus.com`
- **Scheme:** `https`
- **Path:** `/`

---

## 6. Conclusion

The URL `https://limes-plus.com/` is a clear phishing indicator: it is unrelated to Santander, used in a credential‑harvesting context, and delivered via a spoofed sender in a fraudulent email.
