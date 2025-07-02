import json
import os
import sys

from typing import List
from typing_extensions import Annotated

import httpx
import typer

from dotenv import load_dotenv
from httpx import HTTPStatusError, RequestError
from loguru import logger

from apiclient.api_types import (
    HarmonizationEnvelope,
    HarmonizationRequest,
    HarmonizationResponse,
    HarmonizationResults,
    HarmonizationVariation,
)

HARMONIZATION_DEFAULT_API_URL = "https://apiserver.netriasbdf.cloud/v1/harmonize"

app = typer.Typer()

def harmonize(req: HarmonizationRequest,
              api_url: str,
              api_key: str,
              ssl_verify: True
              ):
    
    request_headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json',
        }

    # print(req.model_dump())

    logger.info("API URL: {}", api_url)

    try:
        res = httpx.post(api_url,
                         data=req.model_dump_json(),
                         headers=request_headers,
                         timeout=60,
                         verify=True,)

        res.raise_for_status()

    except HTTPStatusError as e:
        logger.error("Received apiserver error response ({}) from {}",
                     e.response.status_code, e.request.url)
        typer.echo(e.response.text)
        raise typer.Exit(code=1)

    except RequestError as e:
        typer.echo(f"Error: Network problem occurred while requesting {e.request.url} - {e}", err=True)
        raise typer.Exit(code=1)

    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)
        raise typer.Exit(code=1)

    return HarmonizationResponse(**res.json()['body'])

@app.command()
def about():
    """CLI tooling for client scripting of the Netrias harmonization API
    """

    print("""
    CLI tooling for client scripting of the Netrias harmonization API

    Copyright 2024-25 Netrias LLC
    """)

              
@app.command(name="harmonize")
def harmonize_command(cde: int, variations: List[str],
              api_url: Annotated[str, typer.Option(help="URL of harmonizaton API endpoint")] = "",
              api_key: Annotated[str, typer.Option(help="API key for harmonizaton API endpoint")] = "",
              ssl_verify: bool = True,
              ):


    if not api_url:
        api_url = os.environ.get("HARMONIZATION_API_URL",
                                 HARMONIZATION_DEFAULT_API_URL)
    
    if not api_key:
        api_key = os.environ.get("HARMONIZATION_API_KEY", "")

    def build_request(variation, cde):
        return HarmonizationRequest(
            body=HarmonizationVariation(
                string_to_harmonize=variation,
                cde_id=cde,
                data_commons_id=1,
                cde_version_id="v1"
            )
        )

    requests = [build_request(variation, cde) for variation in variations]
    
    responses = [harmonize(r, api_url, api_key, ssl_verify) for r in requests]
                 
                           
    # json.dump(harmonizations, fp=sys.stdout)
    json.dump([r.model_dump() for r in responses], fp=sys.stdout)
    # print(file=sys.stdout)


def main() -> None:
    load_dotenv()
    app()

