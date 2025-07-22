# 


# Data‑Chord UI – Guided Harmonization Workflow

> **Turn spreadsheets into standardized metadata without writing code.**

|                    |                                                                                             |
| ------------------ | ------------------------------------------------------------------------------------------- |
| **Container**      | [`charmannetrias/data_chord:version_1`](https://hub.docker.com/r/charmannetrias/data_chord) |
| **Endpoints used** | `/cde-recommendation`, `/harmonize`                                                         |
| **Audience**       | Analysts, biologists, or anyone who prefers a point‑and‑click interface over API calls.     |

---

## Quick Start (Docker)

```bash
# 1 • Pull the image
docker pull charmannetrias/data_chord:version_1

# 2 • Run the container (replace the key!)
docker run \
  -e HARMONIZATION_APP_KEY="<YOUR_API_KEY>" \
  -p 8080:8080 \
  charmannetrias/data_chord:version_1
```

*Navigate to* **`http://localhost:8080`** in your browser.
> **Note:** You will need docker installed.

### Environment Variables

| Variable                | Required | Description                                             |
| ----------------------- | -------- | ------------------------------------------------------- |
| `HARMONIZATION_APP_KEY` | ✅        | Your Netrias API key (same header used for REST calls). |
| `PORT`                  | ❌        | Override the default `8080` port if needed.             |

---

## Guided Workflow

1. **Upload file** – Select a CSV or Excel file.<br>*(Max 25 MB; UTF‑8 recommended)*
3. **Column‑to‑Model mapping** – For the selected column you’ll see the top CDE suggestions. Accept the suggestion or override.
4. **Value harmonization** – Click *“Harmonize”* and the UI batch‑calls **`/harmonize`** for every non‑null cell for the selected column.
5. **Review & export** – Preview differences (original vs. AI-harmonized) then download as CSV with or without the harmonization metadata.

---

## Authentication

* The UI forwards your **`HARMONIZATION_APP_KEY`** to the API—no keys are stored server‑side.

---

## Roadmap

* **Session persistence** – resume unfinished harmonizations after refresh
* **Batch CLI wrapper** around the container for headless use

---

## License & Support

The Data Chord UI is released under Apache 2.0. For bug reports or feature requests, open an issue.

### Changelog

* 2025‑07‑22 – Added initial draft .