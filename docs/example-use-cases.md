

# Advanced Use‑Case Guide – **Auto‑Schema Detection + Bulk Harmonization**

This walk‑through demonstrates how to automate a **complete pipeline**:

1. **Schema discovery** – Use `/cde-recommendation` to score each available schema against your input table and pick the best match.
2. **Column‑level CDE mapping** – Extract the top CDE suggestion for every column from the winning schema.
3. **Value harmonization** – Call `/harmonize` for each non‑null cell to convert free‑text values into permissible values.
4. **Output** – Produce a fully harmonized JSON table you can re‑ingest or export.

> **When to use:** large spreadsheets of unknown provenance, rapid data‑on‑boarding, or batch validations before upload to a data commons.

---

## 1 · Prerequisites

* **API key** issued by Netrias (`x-api-key` header).
* Python ≥ 3.9 with `requests` installed.

```python
pip install requests
```

---

## 2 · End‑to‑End Example Code

```python
import json, requests

# ---------------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------------
API_KEY = "<PUT‑YOUR‑API‑KEY‑HERE>"
CDE_REC_ENDPOINT = "https://api.netriasbdf.cloud/cde-recommendation"
HARMONIZE_ENDPOINT = "https://api.netriasbdf.cloud/harmonize"

# Candidate schemas to evaluate (keep this list updated as new ones roll in)
SCHEMAS = [
    "cds",
    "gc",
    "sage_chipseq",
    "sage_rnaseq",
    "sage_imagingassay",
    "sage_clinicalassay",
]

HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY,
}

# ---------------------------------------------------------------------
# RAW INPUT—replace with your own table (column → list of values)
# ---------------------------------------------------------------------
RAW_DATA = {
    "donorAge": [45, 60, 37],
    "ageMeasure": ["years", None, None],
    "clinicalDiagnosis": ["Melanoma", "Basal Cell Carcinoma", "Benign Nevus"],
    "sexAssigned": ["male", "female", "female"],
    "sampleOrigin": ["Skin Biopsy", "Blood", None],
    "bodyOrgan": ["Skin", "Liver", None],
    # ...more columns here...
}

# ---------------------------------------------------------------------
# HELPERS (You can implement your own scoring function)
# ---------------------------------------------------------------------

def avg_top_similarity(column_map: dict) -> float:
    """Return the mean of the highest similarity score for each column."""
    total, count = 0.0, 0
    for candidates in column_map.values():
        if not candidates:
            continue
        best = max(c["similarity"] for c in candidates)
        total += best
        count += 1
    return total / count if count else 0.0

# ---------------------------------------------------------------------
# STEP 1 · Find the best schema
# ---------------------------------------------------------------------
results = {}
for schema in SCHEMAS:
    payload = {
        "body": json.dumps({
            "target_schema": schema,
            "data": RAW_DATA,
        })
    }
    r = requests.post(CDE_REC_ENDPOINT, headers=HEADERS, json=payload)
    r.raise_for_status()
    body = r.json().get("body", {})
    # Response body may be JSON‑encoded – normalise it
    if isinstance(body, str):
        body = json.loads(body)
    results[schema] = {
        "mapping": body,
        "score": avg_top_similarity(body),
    }

best_schema = max(results, key=lambda s: results[s]["score"])
print(f"Best schema → {best_schema} (score = {results[best_schema]['score']:.3f})")

# ---------------------------------------------------------------------
# STEP 2 · Extract top CDE suggestion per column for the best schema
# ---------------------------------------------------------------------
column_to_cde = {}
for col, suggestions in results[best_schema]["mapping"].items():
    if suggestions:
        column_to_cde[col] = suggestions[0]["target"]  # highest similarity

print("
Column → CDE mapping:
", json.dumps(column_to_cde, indent=2))

# ---------------------------------------------------------------------
# STEP 3 · Harmonize every non‑null value in the table
# ---------------------------------------------------------------------
# In production you would retrieve CDE IDs from a metadata service.
# We use a hard‑coded dictionary here for illustration only.
TARGET_TO_CDE_ID = {
    "SexEnum": 1036,
    "ageUnit": 1003,
    "Tumor": 1042,
    "organ": 1011,
    # ...fill out as needed...
}

harmonized = {}
for col, values in RAW_DATA.items():
    cde_name = column_to_cde.get(col)
    cde_id = TARGET_TO_CDE_ID.get(cde_name)
    if cde_id is None:
        # Skip columns without an ID mapping - this typically indicates its a CDE with NO permissible vlaues
        harmonized[col] = values
        continue

    new_vals = []
    for val in values:
        if val in (None, ""):
            new_vals.append(val)
            continue
        payload = {
            "body": {
                "string_to_harmonize": val,
                "data_commons_id": 1,  # or your specific commons ID
                "cde_id": cde_id,
                "cde_version_id": "6v1",
            }
        }
        r = requests.post(HARMONIZE_ENDPOINT, headers=HEADERS, json=payload)
        r.raise_for_status()
        top = r.json().get("body", {}).get("top_harmonizations", [])
        new_vals.append(top[0]["option"] if top else val)
    harmonized[col] = new_vals

with open("harmonized_data.json", "w") as f:
    json.dump(harmonized, f, indent=2)
print("
Saved harmonized table → harmonized_data.json")
```

### Output Preview

```
Best schema → sage_rnaseq (score = 0.494)

Column → CDE mapping:
{
  "sexAssigned": "SexEnum",
  "donorAge": "ageUnit",
  "clinicalDiagnosis": "Tumor",
  "bodyOrgan": "organ",
  ...
}

Saved harmonized table → harmonized_data.json
```

---

## 3 · Customising the Pipeline

| Need                     | How to adjust                                                                                  |
| ------------------------ | ---------------------------------------------------------------------------------------------- |
| **Add more schemas**     | Append IDs to `SCHEMAS`.                                                                       |
| **Dynamic CDE IDs**      | Query the upcoming `/metadata/cdes` endpoint instead of the static `TARGET_TO_CDE_ID` mapping. |
| **Batch performance**    | Harmonize rows in parallel with `concurrent.futures` or queue API calls.                       |
| **Confidence threshold** | Change the `avg_top_similarity` logic or filter suggestions < 0.3 per column.                  |
| **Fallback strategy**    | Keep original values (as above) or flag them for manual review.                                |

---

## 4 · Key Takeaways

* `/cde-recommendation` can serve as an **auto‑classifier** for unknown tables.
* Feeding its top CDE predictions into `/harmonize` closes the loop, generating fully standardised outputs ready for a data commons.
* All steps are **idempotent**—rerun at any time to pick up schema updates or improved vocabularies.

---

### Changelog

* 2025‑07‑11 – Added advanced use‑case guide for combined Schema → CDE → Value harmonization workflow.
