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


JsonNode = Any


class ContentNodeType(PyCelonisBaseEnum):
    ASSET = "ASSET"
    PACKAGE = "PACKAGE"
    FOLDER = "FOLDER"
    IMAGE = "IMAGE"


class RelationType(PyCelonisBaseEnum):
    USES = "USES"
    DEPENDS_ON = "DEPENDS_ON"


class ExceptionReference(PyCelonisBaseModel):
    reference: Optional['str'] = Field(alias="reference")
    message: Optional['str'] = Field(alias="message")
    short_message: Optional['str'] = Field(alias="shortMessage")


class ValidationError(PyCelonisBaseModel):
    attribute: Optional['str'] = Field(alias="attribute")
    error: Optional['str'] = Field(alias="error")
    error_code: Optional['str'] = Field(alias="errorCode")
    additional_info: Optional['str'] = Field(alias="additionalInfo")


class ValidationExceptionDescriptor(PyCelonisBaseModel):
    errors: Optional['List[Optional[ValidationError]]'] = Field(alias="errors")


class SpaceSaveTransport(PyCelonisBaseModel):
    permissions: Optional['List[Optional[str]]'] = Field(alias="permissions")
    id: Optional['str'] = Field(alias="id")
    name: Optional['str'] = Field(alias="name")
    icon_reference: Optional['str'] = Field(alias="iconReference")
    object_id: Optional['str'] = Field(alias="objectId")


class SpaceTransport(PyCelonisBaseModel):
    permissions: Optional['List[Optional[str]]'] = Field(alias="permissions")
    id: Optional['str'] = Field(alias="id")
    name: Optional['str'] = Field(alias="name")
    icon_reference: Optional['str'] = Field(alias="iconReference")
    creation_date: Optional['datetime'] = Field(alias="creationDate")
    change_date: Optional['datetime'] = Field(alias="changeDate")
    object_id: Optional['str'] = Field(alias="objectId")


class AssetMetadataTransport(PyCelonisBaseModel):
    used_variables: Optional['List[Optional[VariableDefinition]]'] = Field(alias="usedVariables")
    related_assets: Optional['List[Optional[RelatedAsset]]'] = Field(alias="relatedAssets")
    asset_usages: Optional['List[Optional[AssetUsage]]'] = Field(alias="assetUsages")
    metadata: Optional['JsonNode'] = Field(alias="metadata")
    hidden: Optional['bool'] = Field(alias="hidden")


class AssetUsage(PyCelonisBaseModel):
    object_id: Optional['str'] = Field(alias="objectId")
    target_objects: Optional['List[Optional[TargetUsageMetadata]]'] = Field(alias="targetObjects")


class ContentNodeBaseTransport(PyCelonisBaseModel):
    reference: Optional['str'] = Field(alias="reference")
    version: Optional['str'] = Field(alias="version")
    external: Optional['bool'] = Field(alias="external")


class RelatedAsset(PyCelonisBaseModel):
    object_id: Optional['str'] = Field(alias="objectId")
    type_: Optional['str'] = Field(alias="type")
    relation_type: Optional['RelationType'] = Field(alias="relationType")


class SaveContentNodeTransport(PyCelonisBaseModel):
    permissions: Optional['List[Optional[str]]'] = Field(alias="permissions")
    tenant_id: Optional['str'] = Field(alias="tenantId")
    id: Optional['str'] = Field(alias="id")
    key: Optional['str'] = Field(alias="key")
    name: Optional['str'] = Field(alias="name")
    root_node_key: Optional['str'] = Field(alias="rootNodeKey")
    base: Optional['ContentNodeBaseTransport'] = Field(alias="base")
    asset_type: Optional['str'] = Field(alias="assetType")
    node_type: Optional['ContentNodeType'] = Field(alias="nodeType")
    parent_node_key: Optional['str'] = Field(alias="parentNodeKey")
    parent_node_id: Optional['str'] = Field(alias="parentNodeId")
    invalid_content: Optional['bool'] = Field(alias="invalidContent")
    serialized_content: Optional['str'] = Field(alias="serializedContent")
    serialization_type: Optional['str'] = Field(alias="serializationType")
    draft_id: Optional['str'] = Field(alias="draftId")
    working_draft_id: Optional['str'] = Field(alias="workingDraftId")
    activated_draft_id: Optional['str'] = Field(alias="activatedDraftId")
    show_in_viewer_mode: Optional['bool'] = Field(alias="showInViewerMode")
    public_available: Optional['bool'] = Field(alias="publicAvailable")
    embeddable: Optional['bool'] = Field(alias="embeddable")
    root_node_id: Optional['str'] = Field(alias="rootNodeId")
    order: Optional['int'] = Field(alias="order")
    source: Optional['str'] = Field(alias="source")
    asset_metadata_transport: Optional['AssetMetadataTransport'] = Field(alias="assetMetadataTransport")
    space_id: Optional['str'] = Field(alias="spaceId")
    change_date: Optional['datetime'] = Field(alias="changeDate")
    created_by_id: Optional['str'] = Field(alias="createdById")
    creation_date: Optional['datetime'] = Field(alias="creationDate")
    created_by_name: Optional['str'] = Field(alias="createdByName")
    updated_by: Optional['str'] = Field(alias="updatedBy")
    publish: Optional['bool'] = Field(alias="publish")
    activate: Optional['bool'] = Field(alias="activate")
    version: Optional['str'] = Field(alias="version")
    root: Optional['bool'] = Field(alias="root")
    asset: Optional['bool'] = Field(alias="asset")
    object_id: Optional['str'] = Field(alias="objectId")
    root_with_key: Optional['str'] = Field(alias="rootWithKey")
    identifier: Optional['str'] = Field(alias="identifier")


class SourceUsageMetadata(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")


class TargetUsageMetadata(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    type_: Optional['str'] = Field(alias="type")
    source_objects: Optional['List[Optional[SourceUsageMetadata]]'] = Field(alias="sourceObjects")


class VariableDefinition(PyCelonisBaseModel):
    key: Optional['str'] = Field(alias="key")
    type_: Optional['str'] = Field(alias="type")
    description: Optional['str'] = Field(alias="description")
    source: Optional['str'] = Field(alias="source")
    runtime: Optional['bool'] = Field(alias="runtime")
    metadata: Optional['JsonNode'] = Field(alias="metadata")


class ContentNodeTransport(PyCelonisBaseModel):
    permissions: Optional['List[Optional[str]]'] = Field(alias="permissions")
    tenant_id: Optional['str'] = Field(alias="tenantId")
    id: Optional['str'] = Field(alias="id")
    key: Optional['str'] = Field(alias="key")
    name: Optional['str'] = Field(alias="name")
    root_node_key: Optional['str'] = Field(alias="rootNodeKey")
    base: Optional['ContentNodeBaseTransport'] = Field(alias="base")
    asset_type: Optional['str'] = Field(alias="assetType")
    node_type: Optional['ContentNodeType'] = Field(alias="nodeType")
    parent_node_key: Optional['str'] = Field(alias="parentNodeKey")
    parent_node_id: Optional['str'] = Field(alias="parentNodeId")
    invalid_content: Optional['bool'] = Field(alias="invalidContent")
    serialized_content: Optional['str'] = Field(alias="serializedContent")
    serialization_type: Optional['str'] = Field(alias="serializationType")
    draft_id: Optional['str'] = Field(alias="draftId")
    working_draft_id: Optional['str'] = Field(alias="workingDraftId")
    activated_draft_id: Optional['str'] = Field(alias="activatedDraftId")
    show_in_viewer_mode: Optional['bool'] = Field(alias="showInViewerMode")
    public_available: Optional['bool'] = Field(alias="publicAvailable")
    embeddable: Optional['bool'] = Field(alias="embeddable")
    root_node_id: Optional['str'] = Field(alias="rootNodeId")
    order: Optional['int'] = Field(alias="order")
    source: Optional['str'] = Field(alias="source")
    asset_metadata_transport: Optional['AssetMetadataTransport'] = Field(alias="assetMetadataTransport")
    space_id: Optional['str'] = Field(alias="spaceId")
    change_date: Optional['datetime'] = Field(alias="changeDate")
    created_by_id: Optional['str'] = Field(alias="createdById")
    creation_date: Optional['datetime'] = Field(alias="creationDate")
    created_by_name: Optional['str'] = Field(alias="createdByName")
    updated_by: Optional['str'] = Field(alias="updatedBy")
    root: Optional['bool'] = Field(alias="root")
    asset: Optional['bool'] = Field(alias="asset")
    object_id: Optional['str'] = Field(alias="objectId")
    root_with_key: Optional['str'] = Field(alias="rootWithKey")
    identifier: Optional['str'] = Field(alias="identifier")


class VariableDefinitionWithValue(PyCelonisBaseModel):
    key: Optional['str'] = Field(alias="key")
    type_: Optional['str'] = Field(alias="type")
    description: Optional['str'] = Field(alias="description")
    source: Optional['str'] = Field(alias="source")
    runtime: Optional['bool'] = Field(alias="runtime")
    metadata: Optional['JsonNode'] = Field(alias="metadata")
    value: Optional['Any'] = Field(alias="value")


class SpaceDeleteTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    name: Optional['str'] = Field(alias="name")


class ActivatePackageTransport(PyCelonisBaseModel):
    package_key: Optional['str'] = Field(alias="packageKey")
    version: Optional['str'] = Field(alias="version")
    node_ids_to_exclude: Optional['List[Optional[str]]'] = Field(alias="nodeIdsToExclude")


class PackageVersionTransport(PyCelonisBaseModel):
    package_key: Optional['str'] = Field(alias="packageKey")
    version: Optional['str'] = Field(alias="version")
    root_draft_id: Optional['str'] = Field(alias="rootDraftId")


class PackageDeleteTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    name: Optional['str'] = Field(alias="name")


class PackageHistoryTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    key: Optional['str'] = Field(alias="key")
    name: Optional['str'] = Field(alias="name")
    version: Optional['str'] = Field(alias="version")
    date: Optional['datetime'] = Field(alias="date")
    active: Optional['bool'] = Field(alias="active")
    author_id: Optional['str'] = Field(alias="authorId")
    author_name: Optional['str'] = Field(alias="authorName")
    draft_id: Optional['str'] = Field(alias="draftId")


ExceptionReference.update_forward_refs()
ValidationError.update_forward_refs()
ValidationExceptionDescriptor.update_forward_refs()
SpaceSaveTransport.update_forward_refs()
SpaceTransport.update_forward_refs()
AssetMetadataTransport.update_forward_refs()
AssetUsage.update_forward_refs()
ContentNodeBaseTransport.update_forward_refs()
RelatedAsset.update_forward_refs()
SaveContentNodeTransport.update_forward_refs()
SourceUsageMetadata.update_forward_refs()
TargetUsageMetadata.update_forward_refs()
VariableDefinition.update_forward_refs()
ContentNodeTransport.update_forward_refs()
VariableDefinitionWithValue.update_forward_refs()
SpaceDeleteTransport.update_forward_refs()
ActivatePackageTransport.update_forward_refs()
PackageVersionTransport.update_forward_refs()
PackageDeleteTransport.update_forward_refs()
PackageHistoryTransport.update_forward_refs()


class PackageManagerService:
    @staticmethod
    def get_api_spaces_id(client: Client, id: str) -> SpaceTransport:
        logger.debug(
            f"Request: 'GET' -> '/package-manager/api/spaces/{id}'",
            extra={
                "request_type": "GET",
                "path": "/package-manager/api/spaces/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/package-manager/api/spaces/{id}",
            parse_json=True,
            type_=SpaceTransport,
        )

    @staticmethod
    def put_api_spaces_id(client: Client, id: str, request_body: SpaceSaveTransport) -> SpaceTransport:
        logger.debug(
            f"Request: 'PUT' -> '/package-manager/api/spaces/{id}'",
            extra={
                "request_type": "PUT",
                "path": "/package-manager/api/spaces/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="PUT",
            url=f"/package-manager/api/spaces/{id}",
            request_body=request_body,
            parse_json=True,
            type_=SpaceTransport,
        )

    @staticmethod
    def get_api_nodes_id(client: Client, id: str, draft_id: Optional['str'] = None) -> ContentNodeTransport:
        logger.debug(
            f"Request: 'GET' -> '/package-manager/api/nodes/{id}'",
            extra={
                "request_type": "GET",
                "path": "/package-manager/api/nodes/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        params: Dict[str, Any] = {}
        if draft_id:
            params["draftId"] = draft_id
        return client.request(
            method="GET",
            url=f"/package-manager/api/nodes/{id}",
            params=params,
            parse_json=True,
            type_=ContentNodeTransport,
        )

    @staticmethod
    def put_api_nodes_id(client: Client, id: str, request_body: SaveContentNodeTransport) -> ContentNodeTransport:
        logger.debug(
            f"Request: 'PUT' -> '/package-manager/api/nodes/{id}'",
            extra={
                "request_type": "PUT",
                "path": "/package-manager/api/nodes/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="PUT",
            url=f"/package-manager/api/nodes/{id}",
            request_body=request_body,
            parse_json=True,
            type_=ContentNodeTransport,
        )

    @staticmethod
    def delete_api_nodes_id(client: Client, id: str) -> None:
        logger.debug(
            f"Request: 'DELETE' -> '/package-manager/api/nodes/{id}'",
            extra={
                "request_type": "DELETE",
                "path": "/package-manager/api/nodes/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="DELETE",
            url=f"/package-manager/api/nodes/{id}",
        )

    @staticmethod
    def put_api_nodes_by_package_key_package_key_variables_key(
        client: Client, package_key: str, key: str, request_body: VariableDefinitionWithValue
    ) -> VariableDefinitionWithValue:
        logger.debug(
            f"Request: 'PUT' -> '/package-manager/api/nodes/by-package-key/{package_key}/variables/{key}'",
            extra={
                "request_type": "PUT",
                "path": "/package-manager/api/nodes/by-package-key/{package_key}/variables/{key}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="PUT",
            url=f"/package-manager/api/nodes/by-package-key/{package_key}/variables/{key}",
            request_body=request_body,
            parse_json=True,
            type_=VariableDefinitionWithValue,
        )

    @staticmethod
    def delete_api_nodes_by_package_key_package_key_variables_key(client: Client, package_key: str, key: str) -> None:
        logger.debug(
            f"Request: 'DELETE' -> '/package-manager/api/nodes/by-package-key/{package_key}/variables/{key}'",
            extra={
                "request_type": "DELETE",
                "path": "/package-manager/api/nodes/by-package-key/{package_key}/variables/{key}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="DELETE",
            url=f"/package-manager/api/nodes/by-package-key/{package_key}/variables/{key}",
        )

    @staticmethod
    def get_api_spaces(client: Client) -> List[Optional[SpaceTransport]]:
        logger.debug(
            f"Request: 'GET' -> '/package-manager/api/spaces'",
            extra={
                "request_type": "GET",
                "path": "/package-manager/api/spaces",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/package-manager/api/spaces",
            parse_json=True,
            type_=List[Optional[SpaceTransport]],
        )

    @staticmethod
    def post_api_spaces(client: Client, request_body: SpaceSaveTransport) -> SpaceTransport:
        logger.debug(
            f"Request: 'POST' -> '/package-manager/api/spaces'",
            extra={
                "request_type": "POST",
                "path": "/package-manager/api/spaces",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/package-manager/api/spaces",
            request_body=request_body,
            parse_json=True,
            type_=SpaceTransport,
        )

    @staticmethod
    def post_api_spaces_delete_id(client: Client, id: str, request_body: SpaceDeleteTransport) -> None:
        logger.debug(
            f"Request: 'POST' -> '/package-manager/api/spaces/delete/{id}'",
            extra={
                "request_type": "POST",
                "path": "/package-manager/api/spaces/delete/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/package-manager/api/spaces/delete/{id}",
            request_body=request_body,
        )

    @staticmethod
    def post_api_packages_key_activate(client: Client, key: str, request_body: ActivatePackageTransport) -> None:
        logger.debug(
            f"Request: 'POST' -> '/package-manager/api/packages/{key}/activate'",
            extra={
                "request_type": "POST",
                "path": "/package-manager/api/packages/{key}/activate",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/package-manager/api/packages/{key}/activate",
            request_body=request_body,
        )

    @staticmethod
    def post_api_packages_id_load_version(client: Client, id: str, request_body: PackageVersionTransport) -> None:
        logger.debug(
            f"Request: 'POST' -> '/package-manager/api/packages/{id}/load-version'",
            extra={
                "request_type": "POST",
                "path": "/package-manager/api/packages/{id}/load-version",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/package-manager/api/packages/{id}/load-version",
            request_body=request_body,
        )

    @staticmethod
    def post_api_packages_delete_id(client: Client, id: str, request_body: PackageDeleteTransport) -> None:
        logger.debug(
            f"Request: 'POST' -> '/package-manager/api/packages/delete/{id}'",
            extra={
                "request_type": "POST",
                "path": "/package-manager/api/packages/delete/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/package-manager/api/packages/delete/{id}",
            request_body=request_body,
        )

    @staticmethod
    def post_api_nodes(client: Client, request_body: SaveContentNodeTransport) -> ContentNodeTransport:
        logger.debug(
            f"Request: 'POST' -> '/package-manager/api/nodes'",
            extra={
                "request_type": "POST",
                "path": "/package-manager/api/nodes",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/package-manager/api/nodes",
            request_body=request_body,
            parse_json=True,
            type_=ContentNodeTransport,
        )

    @staticmethod
    def post_api_nodes_by_package_key_package_key_variables(
        client: Client, package_key: str, request_body: VariableDefinitionWithValue
    ) -> VariableDefinitionWithValue:
        logger.debug(
            f"Request: 'POST' -> '/package-manager/api/nodes/by-package-key/{package_key}/variables'",
            extra={
                "request_type": "POST",
                "path": "/package-manager/api/nodes/by-package-key/{package_key}/variables",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/package-manager/api/nodes/by-package-key/{package_key}/variables",
            request_body=request_body,
            parse_json=True,
            type_=VariableDefinitionWithValue,
        )

    @staticmethod
    def get_api_packages_id_next_version(client: Client, id: str) -> PackageHistoryTransport:
        logger.debug(
            f"Request: 'GET' -> '/package-manager/api/packages/{id}/next-version'",
            extra={
                "request_type": "GET",
                "path": "/package-manager/api/packages/{id}/next-version",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/package-manager/api/packages/{id}/next-version",
            parse_json=True,
            type_=PackageHistoryTransport,
        )

    @staticmethod
    def get_api_packages_id_history(client: Client, id: str) -> List[Optional[PackageHistoryTransport]]:
        logger.debug(
            f"Request: 'GET' -> '/package-manager/api/packages/{id}/history'",
            extra={
                "request_type": "GET",
                "path": "/package-manager/api/packages/{id}/history",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/package-manager/api/packages/{id}/history",
            parse_json=True,
            type_=List[Optional[PackageHistoryTransport]],
        )

    @staticmethod
    def get_api_nodes_tree(client: Client, space_id: Optional['str'] = None) -> List[Optional[ContentNodeTransport]]:
        logger.debug(
            f"Request: 'GET' -> '/package-manager/api/nodes/tree'",
            extra={
                "request_type": "GET",
                "path": "/package-manager/api/nodes/tree",
                "tracking_type": "API_REQUEST",
            },
        )

        params: Dict[str, Any] = {}
        if space_id:
            params["spaceId"] = space_id
        return client.request(
            method="GET",
            url=f"/package-manager/api/nodes/tree",
            params=params,
            parse_json=True,
            type_=List[Optional[ContentNodeTransport]],
        )

    @staticmethod
    def get_api_nodes_by_root_key_root_key(
        client: Client, root_key: str, asset_type: Optional['str'] = None, node_type: Optional['ContentNodeType'] = None
    ) -> List[Optional[ContentNodeTransport]]:
        logger.debug(
            f"Request: 'GET' -> '/package-manager/api/nodes/by-root-key/{root_key}'",
            extra={
                "request_type": "GET",
                "path": "/package-manager/api/nodes/by-root-key/{root_key}",
                "tracking_type": "API_REQUEST",
            },
        )

        params: Dict[str, Any] = {}
        if asset_type:
            params["assetType"] = asset_type
        if node_type:
            params["nodeType"] = node_type
        return client.request(
            method="GET",
            url=f"/package-manager/api/nodes/by-root-key/{root_key}",
            params=params,
            parse_json=True,
            type_=List[Optional[ContentNodeTransport]],
        )

    @staticmethod
    def get_api_nodes_by_package_key_package_key_variables_definitions_with_values(
        client: Client, package_key: str, type_: Optional['str'] = None, app_mode: Optional['str'] = None
    ) -> List[Optional[VariableDefinitionWithValue]]:
        logger.debug(
            f"Request: 'GET' -> '/package-manager/api/nodes/by-package-key/{package_key}/variables/definitions-with-values'",
            extra={
                "request_type": "GET",
                "path": "/package-manager/api/nodes/by-package-key/{package_key}/variables/definitions-with-values",
                "tracking_type": "API_REQUEST",
            },
        )

        params: Dict[str, Any] = {}
        if type_:
            params["type"] = type_
        if app_mode:
            params["appMode"] = app_mode
        return client.request(
            method="GET",
            url=f"/package-manager/api/nodes/by-package-key/{package_key}/variables/definitions-with-values",
            params=params,
            parse_json=True,
            type_=List[Optional[VariableDefinitionWithValue]],
        )

    @staticmethod
    def get_api_final_nodes(client: Client, space_id: Optional['str'] = None) -> List[Optional[ContentNodeTransport]]:
        logger.debug(
            f"Request: 'GET' -> '/package-manager/api/final-nodes'",
            extra={
                "request_type": "GET",
                "path": "/package-manager/api/final-nodes",
                "tracking_type": "API_REQUEST",
            },
        )

        params: Dict[str, Any] = {}
        if space_id:
            params["spaceId"] = space_id
        return client.request(
            method="GET",
            url=f"/package-manager/api/final-nodes",
            params=params,
            parse_json=True,
            type_=List[Optional[ContentNodeTransport]],
        )

    @staticmethod
    def get_api_final_nodes_id(client: Client, id: str, is_draft: Optional['bool'] = None) -> ContentNodeTransport:
        logger.debug(
            f"Request: 'GET' -> '/package-manager/api/final-nodes/{id}'",
            extra={
                "request_type": "GET",
                "path": "/package-manager/api/final-nodes/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        params: Dict[str, Any] = {}
        if is_draft:
            params["isDraft"] = is_draft
        return client.request(
            method="GET",
            url=f"/package-manager/api/final-nodes/{id}",
            params=params,
            parse_json=True,
            type_=ContentNodeTransport,
        )

