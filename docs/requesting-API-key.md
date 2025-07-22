# API Key Provisioning Guide

## Overview

All requests to the **Harmonize** and **CDE Recommendation** endpoints require an `x-api-key` header. Developers must obtain this key from Netrias before integrating our services into client applications or workflows.

## Who Can Request a Key?

* BDF Performers.
* NIH Staff.
* For third‑party integrators, a mutual NDA and data‑use agreement must be in place first.

## Request Process

1. **Prepare your details** – Collect the following information:

   | Field                              | Why we need it                                                            |
   | ---------------------------------- | ------------------------------------------------------------------------- |
   | **Name**                           | Identify the responsible individual.                                      |
   | **Organization / Team**            | Helps us assign the correct quota.                                        |
   | **Intended use‑case**              | Brief description (e.g., “Prototype UI for clinical data harmonization”). |
   | **Estimated call volume**          | Requests per day (rough order‑of‑magnitude).                              |

2. **Submit your request** – Email the above details to **Netrias** at **[bdf_strides@netrias.com](mailto:bdf_strides@netrias.com)** with subject line **“API Key Request – Netrias BDF”**.

3. **Approval & issuance** – Netrias will confirm receipt within *1 business day* and issue:

   * Your **API key**.
   * **Expiration / rotation schedule** (default: keys will **not** automatically expire at the 12 month mark but we will email you to cofirm you are still using it).

4. **Store the key securely**

   * **Never** commit keys to source control.
   * Prefer environment variables or AWS Secrets Manager.
   * Rotate immediately if you suspect compromise.

5. **Start integrating** – Pass the key in the `x-api-key` header for every request.

## Key Lifecycle Management

| Action                | Contact                                                 | Typical SLA                           |
| --------------------- | ------------------------------------------------------- | ------------------------------------- |
| **Rotate / Revoke**   | Email [bdf_strides@netrias.com](mailto:bdf_strides@netrias.com)   | 4 business hours                      |
| **Report compromise** | Same as above                                           | Immediate – key disabled upon receipt |

## Error Codes Related to API Keys

| HTTP status             | Meaning                 | Recommended Fix                                         |
| ----------------------- | ----------------------- | ------------------------------------------------------- |
| `401 Unauthorized`      | Missing or invalid key. | Ensure the header is set and copy is correct.           |

## Changelog

* 2025‑07‑08 – Initial draft of API Key Provisioning Guide.
