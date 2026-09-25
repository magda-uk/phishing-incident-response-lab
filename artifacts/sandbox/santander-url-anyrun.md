# Santander phishing case — sandbox expectations (ANY.RUN) for URL

## 1. URL under test

- `https://limes-plus.com/`  
- Defanged: `hxxps://limes-plus[.]com/`

---

## 2. Expected behaviour in sandbox

If detonated in a sandbox (e.g. ANY.RUN):

- Browser opens `limes-plus.com`.
- Possible outcomes:
  - Phishing login page mimicking Santander.
  - Generic credential‑harvesting form.
  - Redirect to another domain hosting the phishing kit.
  - Error page if campaign is inactive.

---

## 3. Artefacts to capture

From sandbox run:

- Final URL after redirections.
- HTML source of the landing page.
- Any embedded scripts or external resources.
- Screenshots of the phishing page.
- Additional IoCs:
  - secondary domains,
  - IP addresses,
  - resource paths.

---

## 4. Integration into incident response

Sandbox output should be used to:

- Enrich IoC list.
- Update detections (e.g. Sigma/YARA for URLs/domains).
- Inform blocking decisions (proxy, mail gateway, EDR).
- Document user‑facing risk (credential theft).

---

## 5. Conclusion

Detonating `https://limes-plus.com/` in a sandbox environment provides additional visibility into the phishing infrastructure behind the spoofed Santander email and helps build more robust detections and response playbooks.
