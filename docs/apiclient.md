# Netrias apiclient

A Python module for interacting with
[Netrias](https://www.netrias.com) APIs for biomedical data
harmonization. 

## Quick Start

First [install uv](https://docs.astral.sh/uv/getting-started/installation/#pypi)

```bash
$ curl -LsSf https://astral.sh/uv/install.sh | sh
# or
$ brew install uv
# or
$ winget install --id=astral-sh.uv  -e
```

Second initialize the repo
```bash
$ git clone https://github.com/netrias/apiclient
$ cd ./apiclient
$ uv sync
```

Third run the client script
```bash
$ uv run apc about

    CLI tooling for client scripting of the Netrias harmonization API

    Copyright 2024-25 Netrias LLC
$ uv run apc --help
 Usage: harmonize-terms [OPTIONS] COMMAND [ARGS]...

╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                                    │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                             │
│ --help                        Show this message and exit.                                                                                  │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ about                CLI tooling for client scripting of the Netrias harmonization API                                                     │
│ harmonize            Harmonize variations against a CDE                                                                                    │
│ cde-recommendation   Recommend CDEs to harmonize tabular data                                                                              │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

# the following assumes you have jq installed
$ uv run apc harmonize 1002 nf | jq .
2025-07-01 19:14:00.414 | INFO     | apiclient:harmonize:39 - API URL: https://apiserver.netriasbdf.cloud/v1/harmonize
[
  {
    "variation": "nf",
    "top_harmonizations": [
      {
        "option": "Neurofibromatosis type 1",
        "confidence_score": 0.43795620437956206
      },
      {
        "option": "NF2-related schwannomatosis",
        "confidence_score": 0.21897810218978103
      },
      {
        "option": "Not Applicable",
        "confidence_score": 0.145985401459854
      },
      {
        "option": "Noonan Syndrome",
        "confidence_score": 0.10948905109489052
      },
      {
        "option": "Schwannomatosis-NOS",
        "confidence_score": 0.08759124087591241
      }
    ],
    "cde_id": 1002,
    "cde_key": "bts:Diagnosis"
  }
]
```





