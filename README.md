# Netrias apiclient

A Python module for interacting with
[Netrias](https://www.netrias.com) APIs for biomedical data
harmonization. Also a location for contact info and reference
documentation.

Generously supported by ARPA-A via funding from the [Biomedical Data
Fabric (BDF)
Toolbox](https://arpa-h.gov/explore-funding/programs/arpa-h-bdf-toolbox)
program.

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
$ ./scripts/harmonize-terms about

    CLI tooling for client scripting of the Netrias harmonization API

    Copyright 2024-25 Netrias LLC
$ ./scripts/harmonize-terms --help
 Usage: harmonize-terms [OPTIONS] COMMAND [ARGS]...

╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                 │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.          │
│ --help                        Show this message and exit.                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ about       CLI tooling for client scripting of the Netrias harmonization API                                           │
│ harmonize                                                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Overview

OpenAPI / Swagger documentation is usually deployed at
https://apiserver.netriasbdf.cloud/docs





