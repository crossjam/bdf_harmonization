# Harmonize Endpoint Documentation

## Overview

The **Harmonize** endpoint takes a free‑text string along with contextual metadata and returns up to 5 top candidate controlled‑vocabulary values ("Permissible Values") ranked by confidence, for a chosen comon data element (CDE).
Use this route when you need to map arbitrary user input to a CDE's permissible value.

## HTTP Request

```
POST {BASE_URL}/harmonize
```

> **Production base URL**: `https://api.netriasbdf.cloud`
> Replace `{BASE_URL}` with the appropriate environment (e.g. `https://staging‑api…`) when testing.

### Required Headers

| Header         | Example Value      | Description                           |
| -------------- | ------------------ | ------------------------------------- |
| `Content-Type` | `application/json` | Payload must be JSON‑encoded.         |
| `x-api-key`    | `abcdef123456`     | Your issued API key.                  |

### Request Body

The body **must** be a JSON object with a single top‑level key, `body`, whose value is another JSON object containing the parameters shown below.

```jsonc
{
  "body": {
    "string_to_harmonize": "aselection",   // REQUIRED – free text input
    "data_commons_id": 1,                  // REQUIRED – integer ID of the data commons 
    "cde_id": 1001,                        // REQUIRED – integer ID of the CDE to match against
    "cde_version_id": "1"               // REQUIRED – version identifier for the CDE set (must be set to 1)
  }
}
```

| Field                 | Type      | Description                                                                 |
| --------------------- | --------- | --------------------------------------------------------------------------- |
| `string_to_harmonize` | `string`  | Raw text to be normalized. **Must be defined by cient.**                    |
| `data_commons_id`     | `integer` | Identifier of the target data commons (**must be set to 1**).                    |
| `cde_id`              | `integer` | Identifier of the Common Data Element vocabulary. **Must be defined by cient.**|
| `cde_version_id`      | `string`  | Specific version of the CDE to query (**must be set to 1**). |

### Successful Response (`200 OK`)

```json
{
  "statusCode": 200,
  "body": {
    "status": "success",
    "top_harmonizations": [
      {
        "option": "polyAselection",
        "confidence_score": 0.48
      },
      {
        "option": "lncRNAenrichment",
        "confidence_score": 0.24
      },
      ...
    ]
  }
}
```

| Field                | Type               | Description                                                                                                                                                                      |
| -------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `status`             | `string`           | `"success"` for successful resolutions.                                                                                                                                          |
| `top_harmonizations` | `array` of objects | Sorted *descending* by `confidence_score`. Each object contains: <br>• `option` – the candidate permissible value <br>• `confidence_score` – float 0‑1 representing model confidence |

> **Note**: The list length defaults to *five* options. This may be smaller depending on internal ranking thresholds.

### Error Responses

| HTTP status                 | When it happens                          | Sample payload                                                        |
| --------------------------- | ---------------------------------------- | --------------------------------------------------------------------- |
| `400 Bad Request`           | Missing or malformed parameters          | `{ "status": "error", "message": "string_to_harmonize is required" }` |
| `401 Unauthorized`          | Invalid or missing `x-api-key`           | `{ "status": "error", "message": "Unauthorized" }`                    |
| `404 Not Found`             | `cde_id`/`cde_version_id` does not exist | `{ "status": "error", "message": "CDE not found" }`                   |
| `500 Internal Server Error` | Unexpected failure                       | `{ "status": "error", "message": "Internal server error" }`           |

### Example – Python

```python
import requests, json

url = "https://api.netriasbdf.cloud/harmonize"
headers = {
    "Content-Type": "application/json",
    "x-api-key": "<YOUR_API_KEY>"
}
payload = {
    "body": {
        "string_to_harmonize": "aselection",
        "data_commons_id": 1,
        "cde_id": 1001,
        "cde_version_id": "1"
    }
}
resp = requests.post(url, headers=headers, json=payload)
print(resp.json())
```

### Example – cURL

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -H "x-api-key: <YOUR_API_KEY>" \
  -d '{"body":{"string_to_harmonize":"aselection","data_commons_id":1,"cde_id":1001,"cde_version_id":"1"}}' \
  https://api.netriasbdf.cloud/harmonize
```

## Rate Limits

*TODO – clarify rate‑limit policy (requests per minute/hour and burst behaviour).*

## Changelog

* 2025‑07‑08 – Initial external documentation draft.

