<p align="center">
  <a href="https://netrias.com">
    <img src="docs/images/NETRIAS Logotype_Full Color RGB.png" height="150">
  </a>
</p>

<div align="center">

# Netrias Harmonization API & Tooling

> **Turn messy biomedical metadata into clean, standards‑compliant records in just a few lines of code.**

![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

</div>

The Netrias Harmonization platform provides REST endpoints, a Python CLI, and a prototype user interface for:

* **CDE discovery** – automatically find the best Common Data Element (CDE) for an arbitrary table column.
* **Value harmonization** – map free‑text cell values to controlled vocabularies.
* **End‑to‑end pipelines** – batch‑convert entire spreadsheets into standards‑ready JSON.

---

## 📚 Documentation Tour

Follow this sequence for a smooth on‑boarding. Each step links to a dedicated page with examples and API snippets.

| Step | Topic                     | File                                                                               | Why read it first?                                              |
| :--: | ------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------- |
|   1  | **What We Harmonize**     | [`what-we-harmonize.md`](docs/what-we-harmonize.md)                                     | Learn the core concepts & data models (CDEs + Schemas).         |
|   2  | **Request an API Key**    | [`requesting-API-key.md`](docs/requesting-API-key.md)                                   | Get your credentials to call the service.                       |
|   3  | **Install the CLI Tool**       | [`apiclient.md`](docs/apiclient.md)                                                     | Quick local setup for scripting & command‑line experimentation. |
|   4  | **Install the UI Tool**       | [`data-chord.md`](docs/data-chord.md)                                                     | No-code user interface for guided harmoization. |
|   5  | **CDE Recommendation** | [`cde-recommendation.md`](docs/cde-recommendation.md)                                   | Discover which CDEs match your columns.                  |
|   6  | **Value Harmonization**   | [`harmonize.md`](docs/harmonize.md)                                                     | Convert raw values into permissible values.                      |
|   7  | **Advanced Pipeline**     | [`example-use-cases.md`](docs/example-use-cases.md)                                     | Automate steps 4‑5 end‑to‑end on a whole table.                 |
|   8  | **Swagger / OpenAPI**     | [https://apiserver.netriasbdf.cloud/docs](https://apiserver.netriasbdf.cloud/docs) | Interactive playground & full endpoint reference.               |
|   9  | **Submit Your Own CDEs**  | [`requesting-data-be-added.md`](docs/requesting-data-be-added.md)                       | How to get your custom data loaded into the platform.        |

> **Tip:** Bookmark the Swagger docs - they’re always up to date with the latest versions and error codes.

---

## 🚀 No Code Quick Start

### 1 · Install the Python client

```bash
pip install git+https://github.com/netrias/bdf_harmonization
```

### 2 · Request an API key

See [`requesting-API-key.md`](requesting-API-key.md) and email the necessary info to us. Store the key and URL in an environment variable:

```bash
export NETRIAS_API_KEY="<YOUR_KEY>"
export HARMONIZATION_API_URL="https://apiserver.netriasbdf.cloud/v1/harmonize"
```

### 3 · Harmonize a value in one command

```bash
apc harmonize 1006 "nf" | jq .
```

*(Maps the string “nf” against the **diagnosis** CDE in Sage Bionetworks' Neurofibromatosis (NF) data model and prints the ranked options.)*

## 🛣️ Roadmap

* 🔍 **/mapping** endpoints for programmatic CDE‑ID lookup.
* 🔄 **Versioned CDE support** - store multiple historical CDE releases and let clients specify which version to harmonize against.
* 🗂️ **Bulk upload** of TSV/CSV/Excel files.


---

## 💰 Funding

Generously supported by ARPA-H via funding from the [Biomedical Data Fabric (BDF) Toolbox](https://arpa-h.gov/explore-funding/programs/arpa-h-bdf-toolbox) program.

---

## 🤝 Contributing

We gladly accept pull requests that improve docs, examples, or client code. Please open an issue first if you plan a large change.

---

## 📜 License

© 2025 Netrias LLC - Released under the Apache 2.0 license.
