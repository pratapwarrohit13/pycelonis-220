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


class KpiSource(PyCelonisBaseEnum):
    LOCAL = "LOCAL"
    KNOWLEDGE_MODEL = "KNOWLEDGE_MODEL"


class DataPermissionStrategy(PyCelonisBaseEnum):
    AND = "AND"
    OR = "OR"


class FrontendHandledBackendError(PyCelonisBaseModel):
    frontend_error_key: Optional['str'] = Field(alias="frontendErrorKey")
    error_information: Optional['Any'] = Field(alias="errorInformation")


class AnalysisPackageConfig(PyCelonisBaseModel):
    root_node_key: Optional['str'] = Field(alias="rootNodeKey")
    id: Optional['str'] = Field(alias="id")
    parent_node_key: Optional['str'] = Field(alias="parentNodeKey")
    parent_node_id: Optional['str'] = Field(alias="parentNodeId")
    name: Optional['str'] = Field(alias="name")
    data_model_id: Optional['str'] = Field(alias="dataModelId")
    key: Optional['str'] = Field(alias="key")
    root_node_id: Optional['str'] = Field(alias="rootNodeId")
    knowledge_model_key: Optional['str'] = Field(alias="knowledgeModelKey")
    change_default_event_log: Optional['bool'] = Field(alias="changeDefaultEventLog")
    event_log: Optional['str'] = Field(alias="eventLog")
    custom_dimension: Optional['str'] = Field(alias="customDimension")


class AnalysisPackageTransport(PyCelonisBaseModel):
    analysis: Optional['AnalysisTransport'] = Field(alias="analysis")
    kpis: Optional['List[Optional[KpiTransport]]'] = Field(alias="kpis")
    draft: Optional['DraftTransport'] = Field(alias="draft")
    data_model_id: Optional['str'] = Field(alias="dataModelId")
    knowledge_model_key: Optional['str'] = Field(alias="knowledgeModelKey")
    next_draft_creation_date_time: Optional['datetime'] = Field(alias="nextDraftCreationDateTime")
    change_default_event_log: Optional['bool'] = Field(alias="changeDefaultEventLog")
    event_log: Optional['str'] = Field(alias="eventLog")
    custom_dimension: Optional['str'] = Field(alias="customDimension")


class AnalysisTransport(PyCelonisBaseModel):
    permissions: Optional['List[Optional[str]]'] = Field(alias="permissions")
    id: Optional['str'] = Field(alias="id")
    tenant_id: Optional['str'] = Field(alias="tenantId")
    name: Optional['str'] = Field(alias="name")
    key: Optional['str'] = Field(alias="key")
    description: Optional['str'] = Field(alias="description")
    deleted: Optional['bool'] = Field(alias="deleted")
    transport_id: Optional['str'] = Field(alias="transportId")
    last_published_draft_id: Optional['str'] = Field(alias="lastPublishedDraftId")
    auto_save_id: Optional['str'] = Field(alias="autoSaveId")
    process_id: Optional['str'] = Field(alias="processId")
    create_date: Optional['datetime'] = Field(alias="createDate")
    favourite: Optional['bool'] = Field(alias="favourite")
    content_id: Optional['str'] = Field(alias="contentId")
    content_version: Optional['int'] = Field(alias="contentVersion")
    tags: Optional['List[Optional[Tag]]'] = Field(alias="tags")
    application_id: Optional['str'] = Field(alias="applicationId")
    global_app: Optional['bool'] = Field(alias="globalApp")
    public_link: Optional['bool'] = Field(alias="publicLink")
    last_published_date: Optional['datetime'] = Field(alias="lastPublishedDate")
    last_published_user: Optional['str'] = Field(alias="lastPublishedUser")
    parent_object_id: Optional['str'] = Field(alias="parentObjectId")
    published_draft_id: Optional['str'] = Field(alias="publishedDraftId")
    folder_id: Optional['str'] = Field(alias="folderId")
    object_id: Optional['str'] = Field(alias="objectId")
    application: Optional['bool'] = Field(alias="application")


class DraftTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    title: Optional['str'] = Field(alias="title")
    document: Optional['Any'] = Field(alias="document")
    last_change_date: Optional['datetime'] = Field(alias="lastChangeDate")
    last_change_user_id: Optional['str'] = Field(alias="lastChangeUserId")
    last_change_user_name: Optional['str'] = Field(alias="lastChangeUserName")
    locked_until_date: Optional['datetime'] = Field(alias="lockedUntilDate")
    source_id: Optional['str'] = Field(alias="sourceId")


class KpiTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    name: Optional['str'] = Field(alias="name")
    description: Optional['str'] = Field(alias="description")
    template: Optional['str'] = Field(alias="template")
    parameters: Optional['Any'] = Field(alias="parameters")
    parameter_count: Optional['int'] = Field(alias="parameterCount")
    source: Optional['KpiSource'] = Field(alias="source")
    unit: Optional['str'] = Field(alias="unit")
    value_format: Optional['str'] = Field(alias="valueFormat")


class Tag(PyCelonisBaseModel):
    name: Optional['str'] = Field(alias="name")


class DataCommand(PyCelonisBaseModel):
    cube_id: Optional['str'] = Field(alias="cubeId")
    commands: Optional['List[Optional[DataQuery]]'] = Field(alias="commands")


class DataCommandBatchRequest(PyCelonisBaseModel):
    variables: Optional['List[Optional[Variable]]'] = Field(alias="variables")
    requests: Optional['List[Optional[DataCommandBatchTransport]]'] = Field(alias="requests")


class DataCommandBatchTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    request: Optional['DataCommand'] = Field(alias="request")


class DataQuery(PyCelonisBaseModel):
    computation_id: Optional['int'] = Field(alias="computationId")
    queries: Optional['List[Optional[str]]'] = Field(alias="queries")
    is_transient: Optional['bool'] = Field(alias="isTransient")


class Variable(PyCelonisBaseModel):
    name: Optional['str'] = Field(alias="name")
    type_: Optional['str'] = Field(alias="type")
    value: Optional['str'] = Field(alias="value")


class DataPermissionRule(PyCelonisBaseModel):
    values: Optional['List[Optional[str]]'] = Field(alias="values")
    column_id: Optional['str'] = Field(alias="columnId")
    table_id: Optional['str'] = Field(alias="tableId")


class Kpi(PyCelonisBaseModel):
    name: Optional['str'] = Field(alias="name")
    template: Optional['str'] = Field(alias="template")
    parameter_count: Optional['int'] = Field(alias="parameterCount")
    error: Optional['str'] = Field(alias="error")
    formula: Optional['str'] = Field(alias="formula")


class KpiInformation(PyCelonisBaseModel):
    kpis: Optional['Dict[str, Optional[Kpi]]'] = Field(alias="kpis")


class PostBatchQueryTransport(PyCelonisBaseModel):
    analysis_commands: Optional['List[Optional[DataCommandBatchTransport]]'] = Field(alias="analysisCommands")
    query_environment: Optional['QueryEnvironment'] = Field(alias="queryEnvironment")


class QueryEnvironment(PyCelonisBaseModel):
    accelerator_session_id: Optional['str'] = Field(alias="acceleratorSessionId")
    process_id: Optional['str'] = Field(alias="processId")
    user_id: Optional['str'] = Field(alias="userId")
    user_name: Optional['str'] = Field(alias="userName")
    load_script: Optional['str'] = Field(alias="loadScript")
    kpi_infos: Optional['KpiInformation'] = Field(alias="kpiInfos")
    data_permission_rules: Optional['List[Optional[DataPermissionRule]]'] = Field(alias="dataPermissionRules")
    data_permission_strategy: Optional['DataPermissionStrategy'] = Field(alias="dataPermissionStrategy")


FrontendHandledBackendError.update_forward_refs()
AnalysisPackageConfig.update_forward_refs()
AnalysisPackageTransport.update_forward_refs()
AnalysisTransport.update_forward_refs()
DraftTransport.update_forward_refs()
KpiTransport.update_forward_refs()
Tag.update_forward_refs()
DataCommand.update_forward_refs()
DataCommandBatchRequest.update_forward_refs()
DataCommandBatchTransport.update_forward_refs()
DataQuery.update_forward_refs()
Variable.update_forward_refs()
DataPermissionRule.update_forward_refs()
Kpi.update_forward_refs()
KpiInformation.update_forward_refs()
PostBatchQueryTransport.update_forward_refs()
QueryEnvironment.update_forward_refs()


class ProcessAnalyticsService:
    @staticmethod
    def post_analysis_v2_api_analysis(client: Client, request_body: AnalysisPackageConfig) -> AnalysisPackageTransport:
        logger.debug(
            f"Request: 'POST' -> '/process-analytics/analysis/v2/api/analysis'",
            extra={
                "request_type": "POST",
                "path": "/process-analytics/analysis/v2/api/analysis",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/process-analytics/analysis/v2/api/analysis",
            request_body=request_body,
            parse_json=True,
            type_=AnalysisPackageTransport,
        )

    @staticmethod
    def post_analysis_v2_api_analysis_analysis_id_kpi(
        client: Client, analysis_id: str, request_body: KpiTransport
    ) -> KpiTransport:
        logger.debug(
            f"Request: 'POST' -> '/process-analytics/analysis/v2/api/analysis/{analysis_id}/kpi'",
            extra={
                "request_type": "POST",
                "path": "/process-analytics/analysis/v2/api/analysis/{analysis_id}/kpi",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/process-analytics/analysis/v2/api/analysis/{analysis_id}/kpi",
            request_body=request_body,
            parse_json=True,
            type_=KpiTransport,
        )

    @staticmethod
    def post_analysis_v2_api_analysis_analysis_id_data_command(
        client: Client, analysis_id: str, request_body: DataCommandBatchRequest
    ) -> PostBatchQueryTransport:
        logger.debug(
            f"Request: 'POST' -> '/process-analytics/analysis/v2/api/analysis/{analysis_id}/data_command'",
            extra={
                "request_type": "POST",
                "path": "/process-analytics/analysis/v2/api/analysis/{analysis_id}/data_command",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/process-analytics/analysis/v2/api/analysis/{analysis_id}/data_command",
            request_body=request_body,
            parse_json=True,
            type_=PostBatchQueryTransport,
        )

