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


class CloudTeamPrivacyType(PyCelonisBaseEnum):
    PUBLIC = "PUBLIC"
    PUBLIC_TO_DOMAIN = "PUBLIC_TO_DOMAIN"
    PRIVATE = "PRIVATE"


class DataConsumptionStage(PyCelonisBaseEnum):
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    ORANGE = "ORANGE"
    RED = "RED"


class PermissionsManagementMode(PyCelonisBaseEnum):
    STANDARD = "STANDARD"
    RESTRICTED_TO_ADMINS = "RESTRICTED_TO_ADMINS"


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


class UserTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    email: Optional['str'] = Field(alias="email")
    name: Optional['str'] = Field(alias="name")
    team_name: Optional['str'] = Field(alias="teamName")
    team_id: Optional['str'] = Field(alias="teamId")
    team_domain: Optional['str'] = Field(alias="teamDomain")
    api_token: Optional['str'] = Field(alias="apiToken")
    active: Optional['bool'] = Field(alias="active")
    token: Optional['str'] = Field(alias="token")
    account_created: Optional['bool'] = Field(alias="accountCreated")
    current: Optional['bool'] = Field(alias="current")
    language: Optional['str'] = Field(alias="language")
    avatar_url: Optional['str'] = Field(alias="avatarUrl")
    enable_notifications: Optional['bool'] = Field(alias="enableNotifications")
    notifications_time: Optional['str'] = Field(alias="notificationsTime")
    time_zone: Optional['str'] = Field(alias="timeZone")
    role: Optional['int'] = Field(alias="role")
    effective_role: Optional['int'] = Field(alias="effectiveRole")
    contentstore_admin: Optional['bool'] = Field(alias="contentstoreAdmin")
    backend_access: Optional['bool'] = Field(alias="backendAccess")
    last_log_in_date: Optional['datetime'] = Field(alias="lastLogInDate")
    is_first_log_in: Optional['bool'] = Field(alias="isFirstLogIn")
    is_celonis_user: Optional['bool'] = Field(alias="isCelonisUser")
    full_template_access: Optional['bool'] = Field(alias="fullTemplateAccess")
    group_ids: Optional['List[Optional[str]]'] = Field(alias="groupIds")
    cloud_admin: Optional['bool'] = Field(alias="cloudAdmin")
    migrated_to_idp: Optional['bool'] = Field(alias="migratedToIdp")
    name_or_email: Optional['str'] = Field(alias="nameOrEmail")
    analyst: Optional['bool'] = Field(alias="analyst")
    admin: Optional['bool'] = Field(alias="admin")
    member: Optional['bool'] = Field(alias="member")
    name_and_email: Optional['str'] = Field(alias="nameAndEmail")


class UserServicePermissionsTransport(PyCelonisBaseModel):
    service_name: Optional['str'] = Field(alias="serviceName")
    permissions: Optional['List[Optional[str]]'] = Field(alias="permissions")


class TeamTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    name: Optional['str'] = Field(alias="name")
    domain: Optional['str'] = Field(alias="domain")
    privacy_type: Optional['CloudTeamPrivacyType'] = Field(alias="privacyType")
    allowed_domain: Optional['str'] = Field(alias="allowedDomain")
    open_signup_enabled: Optional['bool'] = Field(alias="openSignupEnabled")
    open_signup_code: Optional['str'] = Field(alias="openSignupCode")
    open_signup_default_group_id: Optional['str'] = Field(alias="openSignupDefaultGroupId")
    active: Optional['bool'] = Field(alias="active")
    active_until: Optional['datetime'] = Field(alias="activeUntil")
    accessible_from_ip: Optional['bool'] = Field(alias="accessibleFromIp")
    visible: Optional['bool'] = Field(alias="visible")
    member_limit: Optional['int'] = Field(alias="memberLimit")
    analyst_limit: Optional['int'] = Field(alias="analystLimit")
    action_engine_user_limit: Optional['int'] = Field(alias="actionEngineUserLimit")
    ml_workbenches_limit: Optional['int'] = Field(alias="mlWorkbenchesLimit")
    table_rows_limit: Optional['int'] = Field(alias="tableRowsLimit")
    data_consumption_limit_in_gigabytes: Optional['int'] = Field(alias="dataConsumptionLimitInGigabytes")
    data_pool_versions_limit: Optional['int'] = Field(alias="dataPoolVersionsLimit")
    current_data_consumption_in_bytes: Optional['int'] = Field(alias="currentDataConsumptionInBytes")
    data_push_job_submission_limit_per_sec: Optional['int'] = Field(alias="dataPushJobSubmissionLimitPerSec")
    data_push_job_submission_limit_per_hour: Optional['int'] = Field(alias="dataPushJobSubmissionLimitPerHour")
    data_consumptions_last_updated_at: Optional['datetime'] = Field(alias="dataConsumptionsLastUpdatedAt")
    data_consumption_stage: Optional['DataConsumptionStage'] = Field(alias="dataConsumptionStage")
    data_transfer_hybrid_to_cloud_enabled: Optional['bool'] = Field(alias="dataTransferHybridToCloudEnabled")
    tracking_enabled: Optional['bool'] = Field(alias="trackingEnabled")
    terms_of_use_url: Optional['str'] = Field(alias="termsOfUseUrl")
    terms_and_conditions_enabled: Optional['bool'] = Field(alias="termsAndConditionsEnabled")
    enforce_two_factor_authentication_enabled: Optional['bool'] = Field(alias="enforceTwoFactorAuthenticationEnabled")
    lms_url: Optional['str'] = Field(alias="lmsUrl")
    permissions_management_mode: Optional['PermissionsManagementMode'] = Field(alias="permissionsManagementMode")
    request_date: Optional['datetime'] = Field(alias="requestDate")
    unlimited_action_engine_users: Optional['bool'] = Field(alias="unlimitedActionEngineUsers")
    unlimited_data_pool_versions_limit: Optional['bool'] = Field(alias="unlimitedDataPoolVersionsLimit")
    unlimited_data_push_job_submissions: Optional['bool'] = Field(alias="unlimitedDataPushJobSubmissions")
    unlimited_members: Optional['bool'] = Field(alias="unlimitedMembers")
    unlimited_analysts: Optional['bool'] = Field(alias="unlimitedAnalysts")
    unlimited_ml_workbenches: Optional['bool'] = Field(alias="unlimitedMlWorkbenches")
    unlimited_table_rows: Optional['bool'] = Field(alias="unlimitedTableRows")
    unlimited_data_consumption: Optional['bool'] = Field(alias="unlimitedDataConsumption")


ExceptionReference.update_forward_refs()
ValidationError.update_forward_refs()
ValidationExceptionDescriptor.update_forward_refs()
UserTransport.update_forward_refs()
UserServicePermissionsTransport.update_forward_refs()
TeamTransport.update_forward_refs()


class TeamService:
    @staticmethod
    def get_api_cloud(client: Client) -> UserTransport:
        logger.debug(
            f"Request: 'GET' -> '/api/cloud'",
            extra={
                "request_type": "GET",
                "path": "/api/cloud",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/api/cloud",
            parse_json=True,
            type_=UserTransport,
        )

    @staticmethod
    def get_api_cloud_permissions(client: Client) -> List[Optional[UserServicePermissionsTransport]]:
        logger.debug(
            f"Request: 'GET' -> '/api/cloud/permissions'",
            extra={
                "request_type": "GET",
                "path": "/api/cloud/permissions",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/api/cloud/permissions",
            parse_json=True,
            type_=List[Optional[UserServicePermissionsTransport]],
        )

    @staticmethod
    def get_api_team(client: Client) -> TeamTransport:
        logger.debug(
            f"Request: 'GET' -> '/api/team'",
            extra={
                "request_type": "GET",
                "path": "/api/team",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/api/team",
            parse_json=True,
            type_=TeamTransport,
        )

