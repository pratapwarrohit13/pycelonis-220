import logging
from datetime import datetime
from io import BytesIO
from typing import Any, Dict, List, Optional, Union

from pydantic.v1 import Field

from pycelonis_core.base.base_model import (PyCelonisBaseEnum,
                                            PyCelonisBaseModel)
from pycelonis_core.client.client import Client
from pycelonis_core.utils.ml_workbench import TRACKING_LOGGER

logger = logging.getLogger(TRACKING_LOGGER)


class PqlQueryType(PyCelonisBaseEnum):
    DIMENSION = "DIMENSION"
    FILTER = "FILTER"
    TABLE = "TABLE"
    PREAMBLE = "PREAMBLE"


class DiagnosticSeverity(PyCelonisBaseEnum):
    ERROR = "Error"
    WARNING = "Warning"
    INFORMATION = "Information"
    HINT = "Hint"


class FrontendHandledBackendError(PyCelonisBaseModel):
    frontend_error_key: Optional['str'] = Field(alias="frontendErrorKey")
    error_information: Optional['Any'] = Field(alias="errorInformation")


class ExceptionReference(PyCelonisBaseModel):
    reference: Optional['str'] = Field(alias="reference")
    message: Optional['str'] = Field(alias="message")
    short_message: Optional['str'] = Field(alias="shortMessage")


class PqlBasicBatchParams(PyCelonisBaseModel):
    batch: Optional['List[Optional[PqlBasicParams]]'] = Field(alias="batch")


class PqlBasicParams(PyCelonisBaseModel):
    query: Optional['str'] = Field(alias="query")
    query_type: Optional['PqlQueryType'] = Field(alias="queryType")
    data_model_id: Optional['str'] = Field(alias="dataModelId")


class PqlDiagnosticsBatchResponse(PyCelonisBaseModel):
    message: Optional['str'] = Field(alias="message")
    results: Optional['List[Optional[PqlDiagnosticsResponse]]'] = Field(alias="results")


class PqlDiagnosticsResponse(PyCelonisBaseModel):
    message: Optional['str'] = Field(alias="message")
    diagnostics: Optional['List[Optional[Diagnostic]]'] = Field(alias="diagnostics")


class Diagnostic(PyCelonisBaseModel):
    range: Optional['Range'] = Field(alias="range")
    severity: Optional['DiagnosticSeverity'] = Field(alias="severity")
    code: Optional['str'] = Field(alias="code")
    source: Optional['str'] = Field(alias="source")
    message: Optional['str'] = Field(alias="message")
    related_information: Optional['List[Optional[DiagnosticRelatedInformation]]'] = Field(alias="relatedInformation")


class Position(PyCelonisBaseModel):
    line: Optional['int'] = Field(alias="line")
    character: Optional['int'] = Field(alias="character")


class Range(PyCelonisBaseModel):
    start: Optional['Position'] = Field(alias="start")
    end: Optional['Position'] = Field(alias="end")


class DiagnosticRelatedInformation(PyCelonisBaseModel):
    location: Optional['Location'] = Field(alias="location")
    message: Optional['str'] = Field(alias="message")


class Location(PyCelonisBaseModel):
    uri: Optional['str'] = Field(alias="uri")
    range: Optional['Range'] = Field(alias="range")


class PqlParseTreeResponse(PyCelonisBaseModel):
    message: Optional['str'] = Field(alias="message")
    root: Optional['PqlParseTreeNodeTransport'] = Field(alias="root")


class PqlParseTreeNodeTransport(PyCelonisBaseModel):
    rule_name: Optional['str'] = Field(alias="ruleName")
    begin: Optional['Position'] = Field(alias="begin")
    end: Optional['Position'] = Field(alias="end")
    children: Optional['List[Optional[PqlParseTreeNodeTransport]]'] = Field(alias="children")


FrontendHandledBackendError.update_forward_refs()
ExceptionReference.update_forward_refs()
PqlBasicBatchParams.update_forward_refs()
PqlBasicParams.update_forward_refs()
PqlDiagnosticsBatchResponse.update_forward_refs()
PqlDiagnosticsResponse.update_forward_refs()
Diagnostic.update_forward_refs()
Position.update_forward_refs()
Range.update_forward_refs()
DiagnosticRelatedInformation.update_forward_refs()
Location.update_forward_refs()
PqlParseTreeResponse.update_forward_refs()
PqlParseTreeNodeTransport.update_forward_refs()


class PqlLanguageService:
    @staticmethod
    def post_api_lsp_publish_diagnostics_batch(
        client: Client, request_body: PqlBasicBatchParams
    ) -> PqlDiagnosticsBatchResponse:
        logger.debug(
            f"Request: 'POST' -> '/pql-language/api/lsp/publishDiagnostics/batch'",
            extra={
                "request_type": "POST",
                "path": "/pql-language/api/lsp/publishDiagnostics/batch",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/pql-language/api/lsp/publishDiagnostics/batch",
            request_body=request_body,
            parse_json=True,
            type_=PqlDiagnosticsBatchResponse,
        )

    @staticmethod
    def post_api_lsp_parse_tree(client: Client, request_body: PqlBasicParams) -> PqlParseTreeResponse:
        logger.debug(
            f"Request: 'POST' -> '/pql-language/api/lsp/parseTree'",
            extra={
                "request_type": "POST",
                "path": "/pql-language/api/lsp/parseTree",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/pql-language/api/lsp/parseTree",
            request_body=request_body,
            parse_json=True,
            type_=PqlParseTreeResponse,
        )

