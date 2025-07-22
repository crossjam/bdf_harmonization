# Common Data Element and Schemas Overview

### What is a Common Data Element?
A **Common Data Element (CDE)** is a standardized, semantically defined data field - think of it as a spreadsheet column header whose meaning is precisely described. CDEs come in two varieties:

1. **With a controlled vocabulary** – also called *permissible values or standards*; only those values are considered valid.
2. **Without a controlled vocabulary** – any free‑text (or numeric) value is acceptable, though structure or validation rules may still apply.

#### Example – CDE *with* permissible values

```jsonc
{
  "embedding_medium": {
    "description": "A material that infiltrates and supports a specimen and preserves its shape and structure for sectioning and microscopy.",
    "permissible_values": [
      "Paraffin wax",
      "Carbowax",
      "Methacrylate",
      "Epoxy Resin (Araldite)",
      "Agar embedding",
      "Celloidin media",
      "Gelatin",
      "Other",
      "None",
      "Unknown"
    ]
  }
}
```

#### Example – CDE *without* permissible values

```jsonc
{
  "participant_id": {
    "description": "A number or string (potentially containing metadata) that uniquely identifies a participant in a study.",
    "permissible_values": []
  }
}
```

> **Analogy:** Treat the CDE (`embedding_medium`) as the column header and its permissible values (e.g., `Carbowax`, `Agar embedding`) as the valid entries in the rows beneath. For a CDE like `participant_id`, the rows can contain any value the data creator provides.

### What is a Schema?

A **schema** is an *ordered collection of CDEs* that work together to describe a particular data‑capture scenario, assay, or clinical study domain.
Think of a schema as the **template for a table**: each CDE defines one column, and the schema specifies which columns belong together, their order, validation rules, and version.

Key attributes of a schema:

| Attribute       | Description                                                                                                   |
| --------------- | ------------------------------------------------------------------------------------------------------------- |
| **Scope**       | The scientific or operational context it covers (e.g., RNA‑Seq metadata, clinical encounters).                |
| **CDE set**     | The complete list of CDEs — including those that reference controlled vocabularies and those that do not.       |
| **Version**     | Semantic version (e.g., `6.0.4`) that signals when CDE definitions or permissible values change.              |
| **Source**      | The authority that curates the schema (NCI, Sage Bionetworks, etc.).                                          |
| **Inheritance** | Schemas can extend or subset larger data models, inheriting parent CDEs but tailoring to a narrower use‑case. |

> **Analogy:** If a CDE is a column header, a *schema* is the entire spreadsheet template - laying out every column, its order, and the allowed values. Versioning guarantees that your data aligns with the same template your collaborators expect.

---

### Core Endpoints

| Task                           | Endpoint              | Purpose                                                                                              |
| ------------------------------ | --------------------- | ---------------------------------------------------------------------------------------------------- |
| **Standardize a single value** | [`/harmonize`](harmonize.md)          | Maps one free‑text string to the best‑matching permissible value of a chosen CDE.                    |
| **Discover the right CDE(s)**     | [`/cde-recommendation`](cde-recommendation.md) | Analyses a table (one or more column headers + values) and suggests the most likely CDE targets for each column. |

> (See dedicated documentation for each endpoint for full request/response details and code snippets.)

### Schemas Currently Deployed

| Schema                     | Version  | CDE Count | Source           |
| -------------------------- | -------- | --------- | ---------------- |
| General Commons (GC)       | 6.0.4    | 245       | NCI              |
| Cancer Data Services (CDS) | 5.0.2    | 250       | NCI              |
| NF‑OSI RNA‑Seq             | *latest* | 69        | Sage Bionetworks |
| NF‑OSI Imaging Assay       | *latest* | 40        | Sage Bionetworks |
| NF‑OSI Clinical Assay      | *latest* | 43        | Sage Bionetworks |
| NF‑OSI ChIP‑Seq            | *latest* | 64        | Sage Bionetworks |

For the raw schema source files, refer to:

* **GC and CDS data model:** [https://github.com/CBIIT/cds-model/blob/main/model-desc/cds-model-props.yml](https://github.com/CBIIT/cds-model/blob/main/model-desc/cds-model-props.yml)
* **NF‑OSI schemas:** [https://github.com/nf-osi/nf-metadata-dictionary](https://github.com/nf-osi/nf-metadata-dictionary)

### Choosing the Right Schema or CDE

1. **Know your target CDE:** Use **/harmonize** to convert free‑text values to valid permissible values.
2. **Unsure which CDE applies:** Use **/cde-recommendation** to get ranked suggestions based on sample column data.

> For examples on how use the endponits seperately and together for various use cases please see the [use case documenation](example-use-cases.md).

### Loading Additional Schemas

Our platform is data model agnostic and can ingest virtually any well‑structured CDE collection. To request an import of your own CDEs and schema please reivew the [submission checklist and instructions](requesting-data-be-added.md).

### Quick Links

* Harmonize endpoint docs → [harmonize.md](harmonize.md)
* CDE Recommendation endpoint docs → [cde-recommendation.md](cde-recommendation.md)
* Example use‑case notebooks → [example-use-cases.md](example-use-cases.md)
* Data‑loading request guide → [requesting-data-be-added.md](requesting-data-be-added.md)

### Changelog

* 2025‑07‑08 – Initial draft of CDE and Schema overview