from pydantic import BaseModel


class HarmonizationVariation(BaseModel):
    string_to_harmonize: str
    data_commons_id: int = 1
    cde_id: int = -1
    cde_version_id: str = "v1"

    model_config = {
        "json_schema_extra": {
            "examples": [{"string_to_harmonize": "NB", "data_commons_id": -1, "cde_id": 100, "cde_version_id": -1}]
        }
    }


class HarmonizationRequest(BaseModel):
    body: HarmonizationVariation

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"body": {"string_to_harmonize": "NB", "data_commons_id": -1, "cde_id": 100, "cde_version_id": -1}}
            ]
        }
    }


class HarmonizedTerm(BaseModel):
    option: str = ""
    confidence_score: float = 0.0


class HarmonizationResponse(BaseModel):
    variation: str = ""
    top_harmonizations: list[HarmonizedTerm] = []
    cde_id: int = -1
    cde_key: str = ""


class HarmonizationResults(BaseModel):
    body: HarmonizationResponse

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "body": {
                        "variation": "original variation term",
                        "cde_id": -1,
                        "cde_key": "cde100",
                        "top_harmonizations": [],
                    }
                }
            ]
        }
    }


class HarmonizationEnvelope(BaseModel):
    body: HarmonizationRequest | HarmonizationResponse

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"body": {"string_to_harmonize": "NB", "data_commons_id": -1, "cde_id": 100, "cde_version_id": -1}}
            ]
        }
    }
