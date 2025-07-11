## API Key Provisioning Guide

### Overview

All requests to the **Harmonize** and **CDE Recommendation** endpoints require an `x-api-key` header. Developers must obtain this key from Netrias before integrating our services into client applications or workflows.

### Who Can Request a Key?

* BDF Performers.
* NIH Staff.
* For third‑party integrators, a mutual NDA and data‑use agreement must be in place first.

### Request Process

1. **Prepare your details** – Collect the following information:

   | Field                              | Why we need it                                                            |
   | ---------------------------------- | ------------------------------------------------------------------------- |
   | **Name**                           | Identify the responsible individual.                                      |
   | **Organization / Team**            | Helps us assign the correct quota.                                        |
   | **Intended use‑case**              | Brief description (e.g., “Prototype UI for clinical data harmonization”). |
   | **Estimated call volume**          | Requests per day (rough order‑of‑magnitude).                              |

2. **Submit your request** – Email the above details to **Netrias** at **[apikey@netrias.com](mailto:apikeys@netrias.com)** with subject line **“API Key Request – Netrias BDF”**.

3. **Approval & issuance** – Netrias will confirm receipt within *1 business day* and issue:

   * Your **API key**.
   * **Initial rate‑limit allocation** (defaults: 300 req/min, 50 req/sec burst – subject to change).
   * **Expiration / rotation schedule** (default: keys remain active for 6 months).

4. **Store the key securely** –

   * **Never** commit keys to source control.
   * Prefer environment variables or AWS Secrets Manager.
   * Rotate immediately if you suspect compromise.

5. **Start integrating** – Pass the key in the `x-api-key` header for every request.

### Key Lifecycle Management

| Action                | Contact                                                 | Typical SLA                           |
| --------------------- | ------------------------------------------------------- | ------------------------------------- |
| **Rotate / Revoke**   | Email [apikey@netrias.com](mailto:apikey@netrias.com)   | 4 business hours                      |
| **Increase quota**    | Same as above                                           | 1 business day                        |
| **Report compromise** | Same as above                                           | Immediate – key disabled upon receipt |

### Error Codes Related to API Keys

| HTTP status             | Meaning                 | Recommended Fix                                         |
| ----------------------- | ----------------------- | ------------------------------------------------------- |
| `401 Unauthorized`      | Missing or invalid key. | Ensure the header is set and copy is correct.           |
| `429 Too Many Requests` | Exceeded rate limit.    | Implement exponential back‑off or request a quota bump. |

### Frequently Asked Questions

* **Q: Can I have separate keys for dev and prod?**
  **A:** Yes. Mention both environments in your email.
* **Q: Do keys expire automatically?**
  **A:** By default after 6 months. We send renewal reminders 2 weeks prior.

### Changelog

* 2025‑07‑08 – Initial draft of API Key Provisioning Guide.
