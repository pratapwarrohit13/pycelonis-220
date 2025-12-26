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


class ExecutionType(PyCelonisBaseEnum):
    SCHEDULE = "SCHEDULE"
    JOB = "JOB"
    TASK = "TASK"
    STEP = "STEP"


class LogLevel(PyCelonisBaseEnum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class TaskType(PyCelonisBaseEnum):
    EXTRACTION = "EXTRACTION"
    TRANSFORMATION = "TRANSFORMATION"
    DATA_MODEL_LOAD = "DATA_MODEL_LOAD"


class TemplateProtectionStatus(PyCelonisBaseEnum):
    OPEN = "OPEN"
    VIEWABLE = "VIEWABLE"
    PROTECTED = "PROTECTED"
    LOCKED = "LOCKED"


class ChangeDateOffsetType(PyCelonisBaseEnum):
    DAYS = "DAYS"
    HOURS = "HOURS"
    MINUTES = "MINUTES"


class DataPushDeleteStrategy(PyCelonisBaseEnum):
    DELETE = "DELETE"
    STORE_IN_STAGING_TABLE = "STORE_IN_STAGING_TABLE"
    IGNORE = "IGNORE"
    DELETE_AND_STORE_IN_STAGING_TABLE = "DELETE_AND_STORE_IN_STAGING_TABLE"


class JoinType(PyCelonisBaseEnum):
    NONE = "NONE"
    JOIN = "JOIN"
    COLUMN_VALUE = "COLUMN_VALUE"


class TableConfigurationParameterKey(PyCelonisBaseEnum):
    BATCH_SIZE = "BATCH_SIZE"
    ROLLING_PAGE_SIZE = "ROLLING_PAGE_SIZE"
    SPLIT_JOB_BY_DAYS = "SPLIT_JOB_BY_DAYS"
    MAX_STRING_LENGTH = "MAX_STRING_LENGTH"
    DELTA_LOAD_AS_REPLACE_MERGE = "DELTA_LOAD_AS_REPLACE_MERGE"
    EXTRACT_DISPLAY_VALUES = "EXTRACT_DISPLAY_VALUES"
    METADATA_SOURCE = "METADATA_SOURCE"
    MAX_EXTRACTED_RECORDS = "MAX_EXTRACTED_RECORDS"
    PARTITION_COLUMNS = "PARTITION_COLUMNS"
    ORDER_COLUMNS = "ORDER_COLUMNS"
    REMOVE_DUPLICATES_WITH_ORDER = "REMOVE_DUPLICATES_WITH_ORDER"
    CHANGELOG_EXTRACTION_STRATEGY_OPTIONS = "CHANGELOG_EXTRACTION_STRATEGY_OPTIONS"
    CHANGELOG_TABLE_NAME = "CHANGELOG_TABLE_NAME"
    CHANGELOG_TABLE_NAME_COLUMN = "CHANGELOG_TABLE_NAME_COLUMN"
    CHANGELOG_ID_COLUMN = "CHANGELOG_ID_COLUMN"
    SOURCE_SYSTEM_JOIN_COLUMN = "SOURCE_SYSTEM_JOIN_COLUMN"
    CHANGELOG_JOIN_COLUMN = "CHANGELOG_JOIN_COLUMN"
    CHANGELOG_CHANGE_TYPE_COLUMN = "CHANGELOG_CHANGE_TYPE_COLUMN"
    CHANGELOG_DELETE_CHANGE_TYPE_IDENTIFIER = "CHANGELOG_DELETE_CHANGE_TYPE_IDENTIFIER"
    CHANGELOG_CLEANUP_METHOD = "CHANGELOG_CLEANUP_METHOD"
    CHANGELOG_CLEANUP_STATUS_COLUMN = "CHANGELOG_CLEANUP_STATUS_COLUMN"
    CHANGELOG_CLEANUP_STATUS_VALUE = "CHANGELOG_CLEANUP_STATUS_VALUE"
    CHANGELOG_CHANGE_TIMESTAMP_COLUMN = "CHANGELOG_CHANGE_TIMESTAMP_COLUMN"
    IGNORE_ERRORS_ON_RESPONSE = "IGNORE_ERRORS_ON_RESPONSE"
    STRING_COLUMN_LENGTH = "STRING_COLUMN_LENGTH"
    CURRENCY = "CURRENCY"
    FILE_EXTENSION_OPTIONS = "FILE_EXTENSION_OPTIONS"
    FILE_HAS_HEADER_ROW = "FILE_HAS_HEADER_ROW"
    FILE_ENCODING = "FILE_ENCODING"
    FIELD_SEPARATOR = "FIELD_SEPARATOR"
    QUOTE_CHARACTER = "QUOTE_CHARACTER"
    ESCAPE_SEQUENCE = "ESCAPE_SEQUENCE"
    DECIMAL_SEPARATOR = "DECIMAL_SEPARATOR"
    THOUSAND_SEPARATOR = "THOUSAND_SEPARATOR"
    LINE_ENDING = "LINE_ENDING"
    DATA_FORMAT = "DATA_FORMAT"
    CURRENCY_FROM = "CURRENCY_FROM"
    CURRENCY_TO = "CURRENCY_TO"
    CONVERSION_TYPE = "CONVERSION_TYPE"
    PAGINATION_WINDOW_IN_DAYS = "PAGINATION_WINDOW_IN_DAYS"


class TableExtractionType(PyCelonisBaseEnum):
    PARENT_TABLE = "PARENT_TABLE"
    DEPENDENT_TABLE = "DEPENDENT_TABLE"
    NESTED_TABLE = "NESTED_TABLE"


class ExecutionStatus(PyCelonisBaseEnum):
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    CANCEL = "CANCEL"
    FAIL = "FAIL"
    SKIPPED = "SKIPPED"


class AutoMergeExecutionMode(PyCelonisBaseEnum):
    DISTINCT = "DISTINCT"
    NON_DISTINCT = "NON_DISTINCT"


class CalendarDay(PyCelonisBaseEnum):
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class ColumnType(PyCelonisBaseEnum):
    INTEGER = "INTEGER"
    DATE = "DATE"
    TIME = "TIME"
    DATETIME = "DATETIME"
    FLOAT = "FLOAT"
    BOOLEAN = "BOOLEAN"
    STRING = "STRING"


class DataModelCalendarType(PyCelonisBaseEnum):
    NONE = "NONE"
    CUSTOM = "CUSTOM"
    FACTORY = "FACTORY"


class PoolConfigurationStatus(PyCelonisBaseEnum):
    NEW_CUSTOM_POOL_WITHOUT_TARGET_CONFIGURATION = "NEW_CUSTOM_POOL_WITHOUT_TARGET_CONFIGURATION"
    NEW = "NEW"
    DATA_SOURCES_CONFIGURED = "DATA_SOURCES_CONFIGURED"
    OPTIONS_CONFIGURED = "OPTIONS_CONFIGURED"
    CONFIGURED = "CONFIGURED"


class DataPushUpsertStrategy(PyCelonisBaseEnum):
    UPSERT_WITH_UNCHANGED_METADATA = "UPSERT_WITH_UNCHANGED_METADATA"
    UPSERT_WITH_NULLIFICATION = "UPSERT_WITH_NULLIFICATION"


class JobStatus(PyCelonisBaseEnum):
    NEW = "NEW"
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    DONE = "DONE"
    ERROR = "ERROR"
    CANCELED = "CANCELED"


class JobType(PyCelonisBaseEnum):
    REPLACE = "REPLACE"
    DELTA = "DELTA"


class UploadFileType(PyCelonisBaseEnum):
    PARQUET = "PARQUET"
    CSV = "CSV"


class DataPermissionStrategy(PyCelonisBaseEnum):
    AND = "AND"
    OR = "OR"


class ExportType(PyCelonisBaseEnum):
    PARQUET = "PARQUET"
    EXCEL = "EXCEL"
    CSV = "CSV"


class ExportStatus(PyCelonisBaseEnum):
    RUNNING = "RUNNING"
    DONE = "DONE"
    FAILED = "FAILED"
    EXPIRED = "EXPIRED"


class ExtractionMode(PyCelonisBaseEnum):
    FULL = "FULL"
    DELTA = "DELTA"


class ChunkType(PyCelonisBaseEnum):
    UPSERT = "UPSERT"
    DELETE = "DELETE"


class AnonymizationAlgorithm(PyCelonisBaseEnum):
    SHA_1 = "SHA_1"
    SHA_256 = "SHA_256"
    SHA_256_NO_SALT = "SHA_256_NO_SALT"
    SHA_512 = "SHA_512"
    SHA_512_NO_SALT = "SHA_512_NO_SALT"


class ExecutionMessageCode(PyCelonisBaseEnum):
    CONNECTOR_BUILDER_INFER_DUPLICATE_COLUMN = "CONNECTOR_BUILDER_INFER_DUPLICATE_COLUMN"
    CONNECTOR_BUILDER_INFER_TYPE_MISMATCH = "CONNECTOR_BUILDER_INFER_TYPE_MISMATCH"
    CONNECTOR_BUILDER_INFER_UNKNOWN_TYPE = "CONNECTOR_BUILDER_INFER_UNKNOWN_TYPE"
    CONNECTOR_BUILDER_INFER_INVALID_JSON = "CONNECTOR_BUILDER_INFER_INVALID_JSON"
    CONNECTOR_BUILDER_RESPONSE_ROOT_NOT_OBJECT = "CONNECTOR_BUILDER_RESPONSE_ROOT_NOT_OBJECT"
    CONNECTOR_BUILDER_INVALID_RESPONSE_ROOT = "CONNECTOR_BUILDER_INVALID_RESPONSE_ROOT"
    CONNECTOR_BUILDER_GET_SAMPLES_FAILED = "CONNECTOR_BUILDER_GET_SAMPLES_FAILED"
    CANCELING_EXTRACTION = "CANCELING_EXTRACTION"
    AT_LEAST_ONE_TABLE_EXTRACTION_FAILED = "AT_LEAST_ONE_TABLE_EXTRACTION_FAILED"
    STARTING_LOADING_TABLE_TO_TARGET = "STARTING_LOADING_TABLE_TO_TARGET"
    STARTING_RUNNING_JOB = "STARTING_RUNNING_JOB"
    EXTRACTION_SUCCESSFUL = "EXTRACTION_SUCCESSFUL"
    WAITING_FOR_SUCCESS_STATE = "WAITING_FOR_SUCCESS_STATE"
    REACHED_DATA_PUSH_JOB_LIMIT = "REACHED_DATA_PUSH_JOB_LIMIT"
    LOADING_TABLE = "LOADING_TABLE"
    EXTRACTION_FAILED = "EXTRACTION_FAILED"
    EXTRACTION_FAILED_WITH_EXCEPTION = "EXTRACTION_FAILED_WITH_EXCEPTION"
    EXTRACTION_FAILED_AFTER_RETRY_EXHAUSTED = "EXTRACTION_FAILED_AFTER_RETRY_EXHAUSTED"
    STOPPED_RETRYING_DATAPUSHJOB_CREATION = "STOPPED_RETRYING_DATAPUSHJOB_CREATION"
    USING_TARGET_TABLE_NAME = "USING_TARGET_TABLE_NAME"
    PUSHING_FILE_FOR_TABLE = "PUSHING_FILE_FOR_TABLE"
    CALLED_UPLOAD_FILE = "CALLED_UPLOAD_FILE"
    STARTING_EXTRACTION_FOR_RESOURCE = "STARTING_EXTRACTION_FOR_RESOURCE"
    NUMBER_OF_RECORDS_THAT_WILL_BE_EXTRACTED = "NUMBER_OF_RECORDS_THAT_WILL_BE_EXTRACTED"
    FINAL_COUNT_FOR_TABLE = "FINAL_COUNT_FOR_TABLE"
    EMPTY_RESPONSE_FROM_EXTRACTOR = "EMPTY_RESPONSE_FROM_EXTRACTOR"
    EXTRACTOR_NOT_REACHABLE = "EXTRACTOR_NOT_REACHABLE"
    INTEGRATION_NOT_USED_BY_TYPE = "INTEGRATION_NOT_USED_BY_TYPE"
    INTERNAL_ERROR_FROM_EXTRACTOR = "INTERNAL_ERROR_FROM_EXTRACTOR"
    ERROR_WHILE_MAKING_CAPABILITIES_REQUEST = "ERROR_WHILE_MAKING_CAPABILITIES_REQUEST"
    UPLINK_NOT_REACHABLE = "UPLINK_NOT_REACHABLE"
    CONNECTION_CONFIGURATION_VALID = "CONNECTION_CONFIGURATION_VALID"
    CONNECTION_CONFIGURATION_INVALID = "CONNECTION_CONFIGURATION_INVALID"
    CONNECTION_CHECK_MISSING_JDBC_DRIVER = "CONNECTION_CHECK_MISSING_JDBC_DRIVER"
    CPP_2013_PACKAGES_NOT_INSTALLED = "CPP_2013_PACKAGES_NOT_INSTALLED"
    EXTRACTOR_VERSION_DOES_NOT_SUPPORT_COMPRESSION = "EXTRACTOR_VERSION_DOES_NOT_SUPPORT_COMPRESSION"
    EXTRACTOR_VERSION_DOES_NOT_SUPPORT_ADVANCED_SETTINGS = "EXTRACTOR_VERSION_DOES_NOT_SUPPORT_ADVANCED_SETTINGS"
    NECESSARY_FUNCTION_NOT_IMPLEMENTED_IN_SAP = "NECESSARY_FUNCTION_NOT_IMPLEMENTED_IN_SAP"
    UPDATE_RFC_TO_USE_ZIP = "UPDATE_RFC_TO_USE_ZIP"
    ERROR_DURING_CONNECTION_VALIDATION = "ERROR_DURING_CONNECTION_VALIDATION"
    SAP_ERR_NETWORK = "SAP_ERR_NETWORK"
    SAP_ERR_NO_RFC_PING_AUTH = "SAP_ERR_NO_RFC_PING_AUTH"
    SAP_ERR_NO_AUTH = "SAP_ERR_NO_AUTH"
    RFC_ERR_FILE_PERMISSIONS = "RFC_ERR_FILE_PERMISSIONS"
    RFC_ERR_WRITE_FILE = "RFC_ERR_WRITE_FILE"
    RFC_ERR_COMPRESS_FILE = "RFC_ERR_COMPRESS_FILE"
    RFC_ERR_COMPRESS_FILE_NOT_FOUND = "RFC_ERR_COMPRESS_FILE_NOT_FOUND"
    RFC_ERR_DELETE_FILE = "RFC_ERR_DELETE_FILE"
    RFC_ERR_LIST_FILES = "RFC_ERR_LIST_FILES"
    RFC_ERR_GENERIC = "RFC_ERR_GENERIC"
    RFC_WARN_DEFAULT_TARGET_PATH = "RFC_WARN_DEFAULT_TARGET_PATH"
    JCO_NOT_FOUND = "JCO_NOT_FOUND"
    JCO_NATIVE_LIB_NOT_FOUND = "JCO_NATIVE_LIB_NOT_FOUND"
    JCO_NATIVE_LIB_UNSUPPORTED_OS = "JCO_NATIVE_LIB_UNSUPPORTED_OS"
    JCO_NATIVE_LIB_COPY_ERROR = "JCO_NATIVE_LIB_COPY_ERROR"
    SAP_CHECK_JCO_JAR_INSTALLED = "SAP_CHECK_JCO_JAR_INSTALLED"
    SAP_CHECK_JCO_NATIVE_LIB_INSTALLED = "SAP_CHECK_JCO_NATIVE_LIB_INSTALLED"
    SAP_CHECK_MSVC_2013_INSTALLED = "SAP_CHECK_MSVC_2013_INSTALLED"
    SAP_CHECK_NETWORK = "SAP_CHECK_NETWORK"
    SAP_CHECK_NECESSARY_FUNCTIONS_IMPLEMENTED_IN_SAP = "SAP_CHECK_NECESSARY_FUNCTIONS_IMPLEMENTED_IN_SAP"
    SAP_CHECK_EXTRACTOR_VERSION_SUPPORT_COMPRESSION = "SAP_CHECK_EXTRACTOR_VERSION_SUPPORT_COMPRESSION"
    SAP_CHECK_PARQUET_WRITING = "SAP_CHECK_PARQUET_WRITING"
    SAP_CHECK_RFC_TEST_FILE_CREATION = "SAP_CHECK_RFC_TEST_FILE_CREATION"
    SAP_CHECK_RFC_TEST_FILE_COMPRESSION = "SAP_CHECK_RFC_TEST_FILE_COMPRESSION"
    SAP_CHECK_RFC_TEST_FILE_DELETION = "SAP_CHECK_RFC_TEST_FILE_DELETION"
    SAP_CHECK_RFC_LIST_FILES = "SAP_CHECK_RFC_LIST_FILES"
    INTERNAL_ERROR_PERFORMING_TEST = "INTERNAL_ERROR_PERFORMING_TEST"
    SAP_CONFIGURATION_VALIDATION_FAILED = "SAP_CONFIGURATION_VALIDATION_FAILED"
    NO_FILE_RECEIVED_FROM_SAP = "NO_FILE_RECEIVED_FROM_SAP"
    CHANGE_LOG_ENABLED_NECESSARY_FUNCTION_NOT_IMPLEMENTED_IN_SAP = (
        "CHANGE_LOG_ENABLED_NECESSARY_FUNCTION_NOT_IMPLEMENTED_IN_SAP"
    )
    ERROR_RUNNING_VALIDATION_FUNCTION = "ERROR_RUNNING_VALIDATION_FUNCTION"
    NO_RUNNABLE_EXTRACTIONS_OR_TRANSFORMATIONS = "NO_RUNNABLE_EXTRACTIONS_OR_TRANSFORMATIONS"
    DATA_CONSUMPTION_LIMIT_EXCEEDED = "DATA_CONSUMPTION_LIMIT_EXCEEDED"
    STARTING_EXECUTION_OF_EXTRACTION = "STARTING_EXECUTION_OF_EXTRACTION"
    JOB_HAS_NO_DATA_SOURCE = "JOB_HAS_NO_DATA_SOURCE"
    DATASOURCE_NOT_REACHABLE = "DATASOURCE_NOT_REACHABLE"
    DATASOURCE_CONFIGURATION_IS_INVALID = "DATASOURCE_CONFIGURATION_IS_INVALID"
    REQUIRED_FEATURE_NOT_ENABLED = "REQUIRED_FEATURE_NOT_ENABLED"
    CANNOT_READ_DATA_SOURCE = "CANNOT_READ_DATA_SOURCE"
    CANNOT_RETRIEVE_EXTRACTOR_METADATA = "CANNOT_RETRIEVE_EXTRACTOR_METADATA"
    AMBIGUOUS_TABLE_NAME_IN_EXTRACTION = "AMBIGUOUS_TABLE_NAME_IN_EXTRACTION"
    METADATA_HAS_CHANGED = "METADATA_HAS_CHANGED"
    NO_TABLE_IN_EXTRACTION = "NO_TABLE_IN_EXTRACTION"
    EXTRACTION_IS_SKIPPED = "EXTRACTION_IS_SKIPPED"
    VARIABLE_RESOLVING_ERROR = "VARIABLE_RESOLVING_ERROR"
    DELETE_ONLY_POSSIBLE_FOR_DELTA = "DELETE_ONLY_POSSIBLE_FOR_DELTA"
    TABLE_MAPPING_ERROR = "TABLE_MAPPING_ERROR"
    JOB_EXECUTION_CANCELLED = "JOB_EXECUTION_CANCELLED"
    ERROR_STARTING_EXTRACTION = "ERROR_STARTING_EXTRACTION"
    VERSION_INFORMATION = "VERSION_INFORMATION"
    DATA_CONNECTION_CONFIGURATION = "DATA_CONNECTION_CONFIGURATION"
    TABLE_CONFIGURATION = "TABLE_CONFIGURATION"
    TABLE_SUCCESSFULLY_EXTRACTED = "TABLE_SUCCESSFULLY_EXTRACTED"
    ERROR_COMPLETING_TABLE_LOAD = "ERROR_COMPLETING_TABLE_LOAD"
    INVALID_EXTRACTION_IS_RUNNING = "INVALID_EXTRACTION_IS_RUNNING"
    GOT_CHUNK_FOR_TERMINAL_EXTRACTION = "GOT_CHUNK_FOR_TERMINAL_EXTRACTION"
    CANCELING_EXTRACTION_WITH_NAME = "CANCELING_EXTRACTION_WITH_NAME"
    GOT_CHUNK_FOR_TABLE = "GOT_CHUNK_FOR_TABLE"
    FILE_UPLOAD_FAILED = "FILE_UPLOAD_FAILED"
    JOB_ALREADY_RUNNING = "JOB_ALREADY_RUNNING"
    STARTING_RUNNING_JOB_WITH_NAME = "STARTING_RUNNING_JOB_WITH_NAME"
    EARLIER_JOB_IN_SCHEDULE_FAILED_OR_CANCELLED = "EARLIER_JOB_IN_SCHEDULE_FAILED_OR_CANCELLED"
    JOB_COULD_NOT_STARTED = "JOB_COULD_NOT_STARTED"
    EXECUTING_JOB_IN_SCHEDULE = "EXECUTING_JOB_IN_SCHEDULE"
    JOB_ALREADY_RUNNING_CANNOT_EXECUTE_SCHEDULE = "JOB_ALREADY_RUNNING_CANNOT_EXECUTE_SCHEDULE"
    CANNOT_EXECUTE_SCHEDULED_JOBS = "CANNOT_EXECUTE_SCHEDULED_JOBS"
    EXECUTION_CANCELED_ON_REQUEST = "EXECUTION_CANCELED_ON_REQUEST"
    EXECUTION_AUTOMATICALLY_CANCELLED_AFTER_X_MINUTES = "EXECUTION_AUTOMATICALLY_CANCELLED_AFTER_X_MINUTES"
    REMOVING_TMP_FOLDER = "REMOVING_TMP_FOLDER"
    CANNOT_REMOVE_TMP_FOLDER = "CANNOT_REMOVE_TMP_FOLDER"
    CHECKING_SOURCE_SYSTEM_METADATA_CHANGE = "CHECKING_SOURCE_SYSTEM_METADATA_CHANGE"
    UNABLE_GET_COLUMNS_FOR_TABLE = "UNABLE_GET_COLUMNS_FOR_TABLE"
    NO_METADATA_FOUND_FOR_COMPARISON = "NO_METADATA_FOUND_FOR_COMPARISON"
    COLUMNS_HAVE_CHANGED = "COLUMNS_HAVE_CHANGED"
    CANNOT_MAP_TABLE_NAME_IN_EXTRACTION = "CANNOT_MAP_TABLE_NAME_IN_EXTRACTION"
    COLUMN_SMALL_FOR_ANONYMIZATION = "COLUMN_SMALL_FOR_ANONYMIZATION"
    COLUMN_INVALID_FOR_ANONYMIZATION = "COLUMN_INVALID_FOR_ANONYMIZATION"
    METADATA_CHANGED_FOR_TABLE = "METADATA_CHANGED_FOR_TABLE"
    FAILED_TO_START_EXECUTION_ITEM = "FAILED_TO_START_EXECUTION_ITEM"
    FAILED_TO_CHANGE_EXECUTION_ITEM_STATUS = "FAILED_TO_CHANGE_EXECUTION_ITEM_STATUS"
    DELTA_LOAD_HAS_NO_FILTER = "DELTA_LOAD_HAS_NO_FILTER"
    WSDL_FILE_NOT_FOUND = "WSDL_FILE_NOT_FOUND"
    WSDL_MULTIPLE_FILES_FOUND = "WSDL_MULTIPLE_FILES_FOUND"
    WSDL_DIRECTORY_NOT_READABLE = "WSDL_DIRECTORY_NOT_READABLE"
    WSDL_DIRECTORY_IS_EMPTY = "WSDL_DIRECTORY_IS_EMPTY"
    WSDL_PORT_NOT_FOUND = "WSDL_PORT_NOT_FOUND"
    EXTRACTING_FROM_ROW = "EXTRACTING_FROM_ROW"
    NO_VALUE_FOUND_IN_FIRST_COLUMN = "NO_VALUE_FOUND_IN_FIRST_COLUMN"
    ERROR_WHILE_EXTRACTING_TABLE = "ERROR_WHILE_EXTRACTING_TABLE"
    ERROR_RETRIEVING_SPREADSHEET = "ERROR_RETRIEVING_SPREADSHEET"
    GOOGLE_SHEETS_API_LIMIT_REACHED = "GOOGLE_SHEETS_API_LIMIT_REACHED"
    MISSING_FULL_LOAD_COLUMN = "MISSING_FULL_LOAD_COLUMN"
    MISSING_DELTA_LOAD_COLUMN = "MISSING_DELTA_LOAD_COLUMN"
    CONTAINS_FAULTY_COLUMN = "CONTAINS_FAULTY_COLUMN"
    MISSING_MANDATORY_DATE_FILTER_COLUMN = "MISSING_MANDATORY_DATE_FILTER_COLUMN"
    EMPTY_DIRECTORY_AS_TABLE = "EMPTY_DIRECTORY_AS_TABLE"
    DIRECTORY_CONTAINS_MULTIPLE_TYPES = "DIRECTORY_CONTAINS_MULTIPLE_TYPES"
    DOWNLOAD_FINISHED_FOR_FILE = "DOWNLOAD_FINISHED_FOR_FILE"
    DOWNLOAD_PROGRESS_OF_FILE = "DOWNLOAD_PROGRESS_OF_FILE"
    ERROR_EXECUTING_BATCH = "ERROR_EXECUTING_BATCH"
    NO_RECORDS_FOUND_FOR_TABLE = "NO_RECORDS_FOUND_FOR_TABLE"
    UNKNOWN_COLUMN_IN_FILTER = "UNKNOWN_COLUMN_IN_FILTER"
    INCOMPATIBLE_COMPARISON_IN_FILTER = "INCOMPATIBLE_COMPARISON_IN_FILTER"
    REMOVE_DUPLICATE_WITHOUT_PK = "REMOVE_DUPLICATE_WITHOUT_PK"
    SPECIAL_CHAR_IN_TABLE_NAME = "SPECIAL_CHAR_IN_TABLE_NAME"
    DUPLICATE_COLUMN_DETECTED = "DUPLICATE_COLUMN_DETECTED"


class DataLoadType(PyCelonisBaseEnum):
    FROM_CACHE = "FROM_CACHE"
    COMPLETE = "COMPLETE"
    PARTIAL = "PARTIAL"


class DataModelLoadStatus(PyCelonisBaseEnum):
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"
    WARNING = "WARNING"
    LOST_CONNECTION = "LOST_CONNECTION"
    CANCELED = "CANCELED"
    CANCELLING = "CANCELLING"


class LoadStatus(PyCelonisBaseEnum):
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CANCELED = "CANCELED"


class PoolColumnType(PyCelonisBaseEnum):
    STRING = "STRING"
    DATE = "DATE"
    FLOAT = "FLOAT"
    INTEGER = "INTEGER"


class PropertyType(PyCelonisBaseEnum):
    TABLE = "TABLE"
    VIEW = "VIEW"


class LogMessageTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    execution_item_id: Optional['str'] = Field(alias="executionItemId")
    level: Optional['LogLevel'] = Field(alias="level")
    date: Optional['datetime'] = Field(alias="date")
    log_message: Optional['str'] = Field(alias="logMessage")
    log_translation_code: Optional['str'] = Field(alias="logTranslationCode")
    log_translation_parameters: Optional['List[Optional[LogTranslationParameter]]'] = Field(
        alias="logTranslationParameters"
    )


class LogMessageWithPageTransport(PyCelonisBaseModel):
    log_messages: Optional['List[Optional[LogMessageTransport]]'] = Field(alias="logMessages")
    num_of_pages: Optional['int'] = Field(alias="numOfPages")


class FrontendHandledBackendError(PyCelonisBaseModel):
    frontend_error_key: Optional['str'] = Field(alias="frontendErrorKey")
    error_information: Optional['Any'] = Field(alias="errorInformation")


class ExecutionItemWithPageTransport(PyCelonisBaseModel):
    execution_items: Optional['List[Optional[ExecutionItemTransport]]'] = Field(alias="executionItems")
    num_of_pages: Optional['int'] = Field(alias="numOfPages")


class ExecutionItemTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    pool_id: Optional['str'] = Field(alias="poolId")
    pool_name: Optional['str'] = Field(alias="poolName")
    execution_id: Optional['str'] = Field(alias="executionId")
    scheduling_id: Optional['str'] = Field(alias="schedulingId")
    job_id: Optional['str'] = Field(alias="jobId")
    task_id: Optional['str'] = Field(alias="taskId")
    step_id: Optional['str'] = Field(alias="stepId")
    name: Optional['str'] = Field(alias="name")
    status: Optional['ExecutionStatus'] = Field(alias="status")
    data_pool_version: Optional['str'] = Field(alias="dataPoolVersion")
    start_date: Optional['datetime'] = Field(alias="startDate")
    end_date: Optional['datetime'] = Field(alias="endDate")
    type_: Optional['ExecutionType'] = Field(alias="type")
    mode: Optional['ExtractionMode'] = Field(alias="mode")
    scheduling_name: Optional['str'] = Field(alias="schedulingName")
    execution_order: Optional['int'] = Field(alias="executionOrder")
    monitored: Optional['bool'] = Field(alias="monitored")


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


class TransformationTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    pool_id: Optional['str'] = Field(alias="poolId")
    task_id: Optional['str'] = Field(alias="taskId")
    task_type: Optional['TaskType'] = Field(alias="taskType")
    template: Optional['bool'] = Field(alias="template")
    protection_status: Optional['TemplateProtectionStatus'] = Field(alias="protectionStatus")
    name: Optional['str'] = Field(alias="name")
    description: Optional['str'] = Field(alias="description")
    job_id: Optional['str'] = Field(alias="jobId")
    created_at: Optional['datetime'] = Field(alias="createdAt")
    task_created_at: Optional['datetime'] = Field(alias="taskCreatedAt")
    execution_order: Optional['int'] = Field(alias="executionOrder")
    published: Optional['bool'] = Field(alias="published")
    disabled: Optional['bool'] = Field(alias="disabled")
    legal_agreement_accepted: Optional['bool'] = Field(alias="legalAgreementAccepted")
    statement: Optional['str'] = Field(alias="statement")


class TaskUpdate(PyCelonisBaseModel):
    name: Optional['str'] = Field(alias="name")
    description: Optional['str'] = Field(alias="description")


class TaskInstanceTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    pool_id: Optional['str'] = Field(alias="poolId")
    task_id: Optional['str'] = Field(alias="taskId")
    task_type: Optional['TaskType'] = Field(alias="taskType")
    template: Optional['bool'] = Field(alias="template")
    protection_status: Optional['TemplateProtectionStatus'] = Field(alias="protectionStatus")
    name: Optional['str'] = Field(alias="name")
    description: Optional['str'] = Field(alias="description")
    job_id: Optional['str'] = Field(alias="jobId")
    created_at: Optional['datetime'] = Field(alias="createdAt")
    task_created_at: Optional['datetime'] = Field(alias="taskCreatedAt")
    execution_order: Optional['int'] = Field(alias="executionOrder")
    published: Optional['bool'] = Field(alias="published")
    disabled: Optional['bool'] = Field(alias="disabled")
    legal_agreement_accepted: Optional['bool'] = Field(alias="legalAgreementAccepted")


class CalculatedColumnTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    name: Optional['str'] = Field(alias="name")
    expression: Optional['str'] = Field(alias="expression")


class TableConfigurationParameterValue(PyCelonisBaseModel):
    key: Optional['TableConfigurationParameterKey'] = Field(alias="key")
    value: Optional['Any'] = Field(alias="value")


class TableExtractionColumnTransport(PyCelonisBaseModel):
    column_name: Optional['str'] = Field(alias="columnName")
    from_join: Optional['bool'] = Field(alias="fromJoin")
    anonymized: Optional['bool'] = Field(alias="anonymized")
    primary_key: Optional['bool'] = Field(alias="primaryKey")
    preferred_type: Optional['str'] = Field(alias="preferredType")
    date_format: Optional['str'] = Field(alias="dateFormat")


class TableExtractionJoinTransport(PyCelonisBaseModel):
    parent_schema: Optional['str'] = Field(alias="parentSchema")
    parent_table: Optional['str'] = Field(alias="parentTable")
    child_table: Optional['str'] = Field(alias="childTable")
    use_primary_keys: Optional['bool'] = Field(alias="usePrimaryKeys")
    custom_join_path: Optional['str'] = Field(alias="customJoinPath")
    join_filter: Optional['str'] = Field(alias="joinFilter")
    order: Optional['int'] = Field(alias="order")


class TableExtractionTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    task_id: Optional['str'] = Field(alias="taskId")
    job_id: Optional['str'] = Field(alias="jobId")
    table_execution_item_id: Optional['str'] = Field(alias="tableExecutionItemId")
    table_name: Optional['str'] = Field(alias="tableName")
    rename_target_table: Optional['bool'] = Field(alias="renameTargetTable")
    target_table_name: Optional['str'] = Field(alias="targetTableName")
    columns: Optional['List[Optional[TableExtractionColumnTransport]]'] = Field(alias="columns")
    joins: Optional['List[Optional[TableExtractionJoinTransport]]'] = Field(alias="joins")
    dependent_tables: Optional['List[Optional[TableExtractionTransport]]'] = Field(alias="dependentTables")
    use_manual_p_ks: Optional['bool'] = Field(alias="useManualPKs")
    filter_definition: Optional['str'] = Field(alias="filterDefinition")
    delta_filter_definition: Optional['str'] = Field(alias="deltaFilterDefinition")
    schema_name: Optional['str'] = Field(alias="schemaName")
    creation_date_column: Optional['str'] = Field(alias="creationDateColumn")
    creation_date_value_start: Optional['str'] = Field(alias="creationDateValueStart")
    creation_date_value_end: Optional['str'] = Field(alias="creationDateValueEnd")
    creation_date_parameter_start: Optional['str'] = Field(alias="creationDateParameterStart")
    creation_date_parameter_end: Optional['str'] = Field(alias="creationDateParameterEnd")
    creation_date_value_today: Optional['bool'] = Field(alias="creationDateValueToday")
    change_date_column: Optional['str'] = Field(alias="changeDateColumn")
    change_date_offset: Optional['int'] = Field(alias="changeDateOffset")
    change_date_offset_type: Optional['ChangeDateOffsetType'] = Field(alias="changeDateOffsetType")
    table_extraction_type: Optional['TableExtractionType'] = Field(alias="tableExtractionType")
    parent_table: Optional['str'] = Field(alias="parentTable")
    depends_on: Optional['str'] = Field(alias="dependsOn")
    column_value_table: Optional['str'] = Field(alias="columnValueTable")
    column_value_column: Optional['str'] = Field(alias="columnValueColumn")
    column_value_target_column: Optional['str'] = Field(alias="columnValueTargetColumn")
    column_values_at_a_time: Optional['int'] = Field(alias="columnValuesAtATime")
    join_type: Optional['JoinType'] = Field(alias="joinType")
    disabled: Optional['bool'] = Field(alias="disabled")
    connector_specific_configuration: Optional['List[Optional[TableConfigurationParameterValue]]'] = Field(
        alias="connectorSpecificConfiguration"
    )
    calculated_columns: Optional['List[Optional[CalculatedColumnTransport]]'] = Field(alias="calculatedColumns")
    end_date_disabled: Optional['bool'] = Field(alias="endDateDisabled")
    disable_change_log: Optional['bool'] = Field(alias="disableChangeLog")
    data_push_delete_strategy: Optional['DataPushDeleteStrategy'] = Field(alias="dataPushDeleteStrategy")
    customize_column_selection: Optional['bool'] = Field(alias="customizeColumnSelection")
    mirror_table_names: Optional['List[Optional[str]]'] = Field(alias="mirrorTableNames")
    parent: Optional['bool'] = Field(alias="parent")
    selected_columns: Optional['List[Optional[str]]'] = Field(alias="selectedColumns")


class JobTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    name: Optional['str'] = Field(alias="name")
    data_pool_id: Optional['str'] = Field(alias="dataPoolId")
    data_source_id: Optional['str'] = Field(alias="dataSourceId")
    time_stamp: Optional['datetime'] = Field(alias="timeStamp")
    status: Optional['ExecutionStatus'] = Field(alias="status")
    current_execution_id: Optional['str'] = Field(alias="currentExecutionId")
    dag_based_execution_enabled: Optional['bool'] = Field(alias="dagBasedExecutionEnabled")
    latest_execution_item_id: Optional['str'] = Field(alias="latestExecutionItemId")


class DataModelColumnTransport(PyCelonisBaseModel):
    name: Optional['str'] = Field(alias="name")
    type_: Optional['ColumnType'] = Field(alias="type")
    primary_key: Optional['bool'] = Field(alias="primaryKey")


class DataModelConfigurationTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    data_model_id: Optional['str'] = Field(alias="dataModelId")
    activity_table_id: Optional['str'] = Field(alias="activityTableId")
    case_table_id: Optional['str'] = Field(alias="caseTableId")
    default_configuration: Optional['bool'] = Field(alias="defaultConfiguration")
    case_id_column: Optional['str'] = Field(alias="caseIdColumn")
    activity_column: Optional['str'] = Field(alias="activityColumn")
    timestamp_column: Optional['str'] = Field(alias="timestampColumn")
    sorting_column: Optional['str'] = Field(alias="sortingColumn")
    end_timestamp_column: Optional['str'] = Field(alias="endTimestampColumn")
    cost_column: Optional['str'] = Field(alias="costColumn")
    user_column: Optional['str'] = Field(alias="userColumn")
    use_parallel_process: Optional['bool'] = Field(alias="useParallelProcess")
    parallel_process_parent_column: Optional['str'] = Field(alias="parallelProcessParentColumn")
    parallel_process_child_column: Optional['str'] = Field(alias="parallelProcessChildColumn")


class DataModelCustomCalendarEntryTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    day: Optional['CalendarDay'] = Field(alias="day")
    working_day: Optional['bool'] = Field(alias="workingDay")
    start_time: Optional['int'] = Field(alias="startTime")
    end_time: Optional['int'] = Field(alias="endTime")


class DataModelCustomCalendarTransport(PyCelonisBaseModel):
    data_model_id: Optional['str'] = Field(alias="dataModelId")
    entries: Optional['List[Optional[DataModelCustomCalendarEntryTransport]]'] = Field(alias="entries")


class DataModelFactoryCalendarTransport(PyCelonisBaseModel):
    table_name: Optional['str'] = Field(alias="tableName")
    data_source_id: Optional['str'] = Field(alias="dataSourceId")
    data_model_id: Optional['str'] = Field(alias="dataModelId")


class DataModelForeignKeyColumnTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    source_column_name: Optional['str'] = Field(alias="sourceColumnName")
    target_column_name: Optional['str'] = Field(alias="targetColumnName")


class DataModelForeignKeyTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    data_model_id: Optional['str'] = Field(alias="dataModelId")
    source_table_id: Optional['str'] = Field(alias="sourceTableId")
    target_table_id: Optional['str'] = Field(alias="targetTableId")
    columns: Optional['List[Optional[DataModelForeignKeyColumnTransport]]'] = Field(alias="columns")


class DataModelTableTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    data_model_id: Optional['str'] = Field(alias="dataModelId")
    data_source_id: Optional['str'] = Field(alias="dataSourceId")
    name: Optional['str'] = Field(alias="name")
    alias: Optional['str'] = Field(alias="alias")
    columns: Optional['List[Optional[DataModelColumnTransport]]'] = Field(alias="columns")
    use_direct_storage: Optional['bool'] = Field(alias="useDirectStorage")
    primary_keys: Optional['List[Optional[str]]'] = Field(alias="primaryKeys")
    alias_or_name: Optional['str'] = Field(alias="aliasOrName")


class DataModelTransport(PyCelonisBaseModel):
    permissions: Optional['List[Optional[str]]'] = Field(alias="permissions")
    id: Optional['str'] = Field(alias="id")
    name: Optional['str'] = Field(alias="name")
    description: Optional['str'] = Field(alias="description")
    create_date: Optional['datetime'] = Field(alias="createDate")
    changed_date: Optional['datetime'] = Field(alias="changedDate")
    configuration_skipped: Optional['bool'] = Field(alias="configurationSkipped")
    pool_id: Optional['str'] = Field(alias="poolId")
    unavailable: Optional['bool'] = Field(alias="unavailable")
    editable: Optional['bool'] = Field(alias="editable")
    creator_user_id: Optional['str'] = Field(alias="creatorUserId")
    tables: Optional['List[Optional[DataModelTableTransport]]'] = Field(alias="tables")
    foreign_keys: Optional['List[Optional[DataModelForeignKeyTransport]]'] = Field(alias="foreignKeys")
    process_configurations: Optional['List[Optional[DataModelConfigurationTransport]]'] = Field(
        alias="processConfigurations"
    )
    data_model_calendar_type: Optional['DataModelCalendarType'] = Field(alias="dataModelCalendarType")
    factory_calendar: Optional['DataModelFactoryCalendarTransport'] = Field(alias="factoryCalendar")
    custom_calendar: Optional['DataModelCustomCalendarTransport'] = Field(alias="customCalendar")
    original_id: Optional['str'] = Field(alias="originalId")
    eventlog_automerge_enabled: Optional['bool'] = Field(alias="eventlogAutomergeEnabled")
    auto_merge_execution_mode: Optional['AutoMergeExecutionMode'] = Field(alias="autoMergeExecutionMode")
    event_log_count: Optional['int'] = Field(alias="eventLogCount")
    object_id: Optional['str'] = Field(alias="objectId")


class DataModelConfiguration(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    tenant_id: Optional['str'] = Field(alias="tenantId")
    data_model_id: Optional['str'] = Field(alias="dataModelId")
    activity_table_id: Optional['str'] = Field(alias="activityTableId")
    case_table_id: Optional['str'] = Field(alias="caseTableId")
    default_configuration: Optional['bool'] = Field(alias="defaultConfiguration")
    case_id_column: Optional['str'] = Field(alias="caseIdColumn")
    activity_column: Optional['str'] = Field(alias="activityColumn")
    timestamp_column: Optional['str'] = Field(alias="timestampColumn")
    sorting_column: Optional['str'] = Field(alias="sortingColumn")
    end_timestamp_column: Optional['str'] = Field(alias="endTimestampColumn")
    cost_column: Optional['str'] = Field(alias="costColumn")
    user_column: Optional['str'] = Field(alias="userColumn")
    use_parallel_process: Optional['bool'] = Field(alias="useParallelProcess")
    parallel_process_parent_column: Optional['str'] = Field(alias="parallelProcessParentColumn")
    parallel_process_child_column: Optional['str'] = Field(alias="parallelProcessChildColumn")
    optional_tenant_id: Optional['str'] = Field(alias="optionalTenantId")


class DataPoolTransport(PyCelonisBaseModel):
    permissions: Optional['List[Optional[str]]'] = Field(alias="permissions")
    id: Optional['str'] = Field(alias="id")
    name: Optional['str'] = Field(alias="name")
    description: Optional['str'] = Field(alias="description")
    time_stamp: Optional['datetime'] = Field(alias="timeStamp")
    configuration_status: Optional['PoolConfigurationStatus'] = Field(alias="configurationStatus")
    locked: Optional['bool'] = Field(alias="locked")
    content_id: Optional['str'] = Field(alias="contentId")
    content_version: Optional['int'] = Field(alias="contentVersion")
    tags: Optional['List[Optional[Tag]]'] = Field(alias="tags")
    original_id: Optional['str'] = Field(alias="originalId")
    monitoring_target: Optional['bool'] = Field(alias="monitoringTarget")
    custom_monitoring_target: Optional['bool'] = Field(alias="customMonitoringTarget")
    custom_monitoring_target_active: Optional['bool'] = Field(alias="customMonitoringTargetActive")
    exported: Optional['bool'] = Field(alias="exported")
    monitoring_message_columns_migrated: Optional['bool'] = Field(alias="monitoringMessageColumnsMigrated")
    creator_user_id: Optional['str'] = Field(alias="creatorUserId")
    object_id: Optional['str'] = Field(alias="objectId")


class Tag(PyCelonisBaseModel):
    name: Optional['str'] = Field(alias="name")


class CsvColumnParsingOptions(PyCelonisBaseModel):
    column_name: Optional['str'] = Field(alias="columnName")
    date_format: Optional['str'] = Field(alias="dateFormat")
    thousands_separator: Optional['str'] = Field(alias="thousandsSeparator")
    decimal_separator: Optional['str'] = Field(alias="decimalSeparator")


class CsvParsingOptions(PyCelonisBaseModel):
    escape_sequence: Optional['str'] = Field(alias="escapeSequence")
    quote_sequence: Optional['str'] = Field(alias="quoteSequence")
    separator_sequence: Optional['str'] = Field(alias="separatorSequence")
    line_ending: Optional['str'] = Field(alias="lineEnding")
    char_set: Optional['str'] = Field(alias="charSet")
    decimal_separator: Optional['str'] = Field(alias="decimalSeparator")
    thousand_separator: Optional['str'] = Field(alias="thousandSeparator")
    date_format: Optional['str'] = Field(alias="dateFormat")
    additional_column_options: Optional['List[Optional[CsvColumnParsingOptions]]'] = Field(
        alias="additionalColumnOptions"
    )


class ColumnTransport(PyCelonisBaseModel):
    column_name: Optional['str'] = Field(alias="columnName")
    column_type: Optional['ColumnType'] = Field(alias="columnType")
    field_length: Optional['int'] = Field(alias="fieldLength")
    decimals: Optional['int'] = Field(alias="decimals")
    pk_field: Optional['bool'] = Field(alias="pkField")


class DataPushJob(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    tenant_id: Optional['str'] = Field(alias="tenantId")
    target_name: Optional['str'] = Field(alias="targetName")
    last_modified: Optional['datetime'] = Field(alias="lastModified")
    last_ping: Optional['datetime'] = Field(alias="lastPing")
    status: Optional['JobStatus'] = Field(alias="status")
    type_: Optional['JobType'] = Field(alias="type")
    file_type: Optional['UploadFileType'] = Field(alias="fileType")
    target_schema: Optional['str'] = Field(alias="targetSchema")
    upsert_strategy: Optional['DataPushUpsertStrategy'] = Field(alias="upsertStrategy")
    fallback_varchar_length: Optional['int'] = Field(alias="fallbackVarcharLength")
    data_pool_id: Optional['str'] = Field(alias="dataPoolId")
    connection_id: Optional['str'] = Field(alias="connectionId")
    post_execution_query: Optional['str'] = Field(alias="postExecutionQuery")
    sanitized_post_execution_query: Optional['str'] = Field(alias="sanitizedPostExecutionQuery")
    allow_duplicate: Optional['bool'] = Field(alias="allowDuplicate")
    foreign_keys: Optional['str'] = Field(alias="foreignKeys")
    keys: Optional['List[Optional[str]]'] = Field(alias="keys")
    logs: Optional['List[Optional[str]]'] = Field(alias="logs")
    table_schema: Optional['TableTransport'] = Field(alias="tableSchema")
    csv_parsing_options: Optional['CsvParsingOptions'] = Field(alias="csvParsingOptions")
    mirror_target_names: Optional['List[Optional[str]]'] = Field(alias="mirrorTargetNames")
    change_date: Optional['datetime'] = Field(alias="changeDate")
    optional_tenant_id: Optional['str'] = Field(alias="optionalTenantId")


class TableTransport(PyCelonisBaseModel):
    table_name: Optional['str'] = Field(alias="tableName")
    columns: Optional['List[Optional[ColumnTransport]]'] = Field(alias="columns")


class DataCommand(PyCelonisBaseModel):
    cube_id: Optional['str'] = Field(alias="cubeId")
    commands: Optional['List[Optional[DataQuery]]'] = Field(alias="commands")


class DataExportRequest(PyCelonisBaseModel):
    query_environment: Optional['QueryEnvironment'] = Field(alias="queryEnvironment")
    data_command: Optional['DataCommand'] = Field(alias="dataCommand")
    export_type: Optional['ExportType'] = Field(alias="exportType")


class DataPermissionRule(PyCelonisBaseModel):
    values: Optional['List[Optional[str]]'] = Field(alias="values")
    column_id: Optional['str'] = Field(alias="columnId")
    table_id: Optional['str'] = Field(alias="tableId")


class DataQuery(PyCelonisBaseModel):
    computation_id: Optional['int'] = Field(alias="computationId")
    queries: Optional['List[Optional[str]]'] = Field(alias="queries")
    is_transient: Optional['bool'] = Field(alias="isTransient")


class Kpi(PyCelonisBaseModel):
    name: Optional['str'] = Field(alias="name")
    template: Optional['str'] = Field(alias="template")
    parameter_count: Optional['int'] = Field(alias="parameterCount")
    error: Optional['str'] = Field(alias="error")
    formula: Optional['str'] = Field(alias="formula")


class KpiInformation(PyCelonisBaseModel):
    kpis: Optional['Dict[str, Optional[Kpi]]'] = Field(alias="kpis")


class QueryEnvironment(PyCelonisBaseModel):
    accelerator_session_id: Optional['str'] = Field(alias="acceleratorSessionId")
    process_id: Optional['str'] = Field(alias="processId")
    user_id: Optional['str'] = Field(alias="userId")
    user_name: Optional['str'] = Field(alias="userName")
    load_script: Optional['str'] = Field(alias="loadScript")
    kpi_infos: Optional['KpiInformation'] = Field(alias="kpiInfos")
    data_permission_rules: Optional['List[Optional[DataPermissionRule]]'] = Field(alias="dataPermissionRules")
    data_permission_strategy: Optional['DataPermissionStrategy'] = Field(alias="dataPermissionStrategy")


class DataExportStatusResponse(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    export_status: Optional['ExportStatus'] = Field(alias="exportStatus")
    created: Optional['datetime'] = Field(alias="created")
    message: Optional['str'] = Field(alias="message")
    export_type: Optional['ExportType'] = Field(alias="exportType")
    export_chunks: Optional['int'] = Field(alias="exportChunks")


class NewTaskInstanceTransport(PyCelonisBaseModel):
    task_type: Optional['TaskType'] = Field(alias="taskType")
    name: Optional['str'] = Field(alias="name")
    description: Optional['str'] = Field(alias="description")
    task_id: Optional['str'] = Field(alias="taskId")
    job_id: Optional['str'] = Field(alias="jobId")
    execution_order: Optional['int'] = Field(alias="executionOrder")


class DataModelExecutionTableItem(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    alias_or_name: Optional['str'] = Field(alias="aliasOrName")
    selected: Optional['bool'] = Field(alias="selected")


class DataModelExecutionTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    data_model_id: Optional['str'] = Field(alias="dataModelId")
    job_id: Optional['str'] = Field(alias="jobId")
    disabled: Optional['bool'] = Field(alias="disabled")
    data_model_name: Optional['str'] = Field(alias="dataModelName")
    tables: Optional['List[Optional[DataModelExecutionTableItem]]'] = Field(alias="tables")
    partial_load: Optional['bool'] = Field(alias="partialLoad")


class DataModelExecutionConfiguration(PyCelonisBaseModel):
    data_model_execution_id: Optional['str'] = Field(alias="dataModelExecutionId")
    tables: Optional['List[Optional[str]]'] = Field(alias="tables")


class ExtractionConfiguration(PyCelonisBaseModel):
    extraction_id: Optional['str'] = Field(alias="extractionId")
    load_only_subset_of_tables: Optional['bool'] = Field(alias="loadOnlySubsetOfTables")
    tables: Optional['List[Optional[str]]'] = Field(alias="tables")


class JobExecutionConfiguration(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    execution_id: Optional['str'] = Field(alias="executionId")
    pool_id: Optional['str'] = Field(alias="poolId")
    job_id: Optional['str'] = Field(alias="jobId")
    mode: Optional['ExtractionMode'] = Field(alias="mode")
    execute_only_subset_of_transformations: Optional['bool'] = Field(alias="executeOnlySubsetOfTransformations")
    transformations: Optional['List[Optional[str]]'] = Field(alias="transformations")
    execute_only_subset_of_extractions: Optional['bool'] = Field(alias="executeOnlySubsetOfExtractions")
    extractions: Optional['List[Optional[ExtractionConfiguration]]'] = Field(alias="extractions")
    data_source_id: Optional['str'] = Field(alias="dataSourceId")
    load_only_subset_of_data_models: Optional['bool'] = Field(alias="loadOnlySubsetOfDataModels")
    data_models: Optional['List[Optional[DataModelExecutionConfiguration]]'] = Field(alias="dataModels")


class NameMappingAggregated(PyCelonisBaseModel):
    count: Optional['int'] = Field(alias="count")
    type_: Optional['str'] = Field(alias="type")
    language: Optional['str'] = Field(alias="language")


class NameMappingLoadReport(PyCelonisBaseModel):
    nb_of_tables_in_data_model: Optional['int'] = Field(alias="nbOfTablesInDataModel")
    nb_of_table_mappings: Optional['int'] = Field(alias="nbOfTableMappings")
    nb_of_column_mappings: Optional['int'] = Field(alias="nbOfColumnMappings")
    name_mappings_aggregated: Optional['List[Optional[NameMappingAggregated]]'] = Field(alias="nameMappingsAggregated")


class DataPushChunk(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    tenant_id: Optional['str'] = Field(alias="tenantId")
    creation_date: Optional['datetime'] = Field(alias="creationDate")
    type_: Optional['ChunkType'] = Field(alias="type")
    push_job_id: Optional['str'] = Field(alias="pushJobId")
    checksum: Optional['str'] = Field(alias="checksum")
    optional_tenant_id: Optional['str'] = Field(alias="optionalTenantId")


class EntityStatus(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    status: Optional['ExecutionStatus'] = Field(alias="status")
    last_execution_start_date: Optional['datetime'] = Field(alias="lastExecutionStartDate")


class StatementTransport(PyCelonisBaseModel):
    statement: Optional['str'] = Field(alias="statement")
    legal_note: Optional['str'] = Field(alias="legalNote")


class ExtractionConfigurationValueTransport(PyCelonisBaseModel):
    data_push_upsert_strategy: Optional['DataPushUpsertStrategy'] = Field(alias="dataPushUpsertStrategy")
    debug_mode: Optional['bool'] = Field(alias="debugMode")
    delete_job: Optional['bool'] = Field(alias="deleteJob")
    connector_specific_configuration: Optional['List[Optional[TableConfigurationParameterValue]]'] = Field(
        alias="connectorSpecificConfiguration"
    )
    ignore_metadata_changes: Optional['bool'] = Field(alias="ignoreMetadataChanges")


class ExtractionWithTablesTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    pool_id: Optional['str'] = Field(alias="poolId")
    task_id: Optional['str'] = Field(alias="taskId")
    task_type: Optional['TaskType'] = Field(alias="taskType")
    template: Optional['bool'] = Field(alias="template")
    protection_status: Optional['TemplateProtectionStatus'] = Field(alias="protectionStatus")
    name: Optional['str'] = Field(alias="name")
    description: Optional['str'] = Field(alias="description")
    job_id: Optional['str'] = Field(alias="jobId")
    created_at: Optional['datetime'] = Field(alias="createdAt")
    task_created_at: Optional['datetime'] = Field(alias="taskCreatedAt")
    execution_order: Optional['int'] = Field(alias="executionOrder")
    published: Optional['bool'] = Field(alias="published")
    disabled: Optional['bool'] = Field(alias="disabled")
    legal_agreement_accepted: Optional['bool'] = Field(alias="legalAgreementAccepted")
    extraction_configuration_value_transport: Optional['ExtractionConfigurationValueTransport'] = Field(
        alias="extractionConfigurationValueTransport"
    )
    tables: Optional['List[Optional[TableExtractionTransport]]'] = Field(alias="tables")
    metadata_tables: Optional['List[Optional[TableTransport]]'] = Field(alias="metadataTables")
    extraction_configuration: Optional['ExtractionConfigurationValueTransport'] = Field(alias="extractionConfiguration")


class DataSourceTransport(PyCelonisBaseModel):
    id: Optional['str'] = Field(alias="id")
    name: Optional['str'] = Field(alias="name")
    pool_id: Optional['str'] = Field(alias="poolId")
    type_: Optional['str'] = Field(alias="type")
    metadata: Optional['str'] = Field(alias="metadata")
    uplink_id: Optional['str'] = Field(alias="uplinkId")
    connected: Optional['bool'] = Field(alias="connected")
    locked: Optional['bool'] = Field(alias="locked")
    uplink_name: Optional['str'] = Field(alias="uplinkName")
    signature: Optional['str'] = Field(alias="signature")
    use_uplink: Optional['bool'] = Field(alias="useUplink")
    internal_system_id: Optional['str'] = Field(alias="internalSystemId")
    internal_system_selected: Optional['bool'] = Field(alias="internalSystemSelected")
    configuration: Optional['List[Optional[Any]]'] = Field(alias="configuration")
    target_schema_name: Optional['str'] = Field(alias="targetSchemaName")
    exported: Optional['bool'] = Field(alias="exported")
    export_available: Optional['bool'] = Field(alias="exportAvailable")
    extractor_port: Optional['int'] = Field(alias="extractorPort")
    anonymization_algorithm: Optional['AnonymizationAlgorithm'] = Field(alias="anonymizationAlgorithm")
    salt_id: Optional['str'] = Field(alias="saltId")
    custom_extractor_id: Optional['str'] = Field(alias="customExtractorId")
    custom_extractor_name: Optional['str'] = Field(alias="customExtractorName")
    creator_user_id: Optional['str'] = Field(alias="creatorUserId")
    creator_username: Optional['str'] = Field(alias="creatorUsername")
    reachable_and_valid: Optional['bool'] = Field(alias="reachableAndValid")
    normalized_name: Optional['str'] = Field(alias="normalizedName")
    imported: Optional['bool'] = Field(alias="imported")
    parameter_name: Optional['str'] = Field(alias="parameterName")
    configured: Optional['bool'] = Field(alias="configured")


class DataSourceAvailableTables(PyCelonisBaseModel):
    available_tables: Optional['List[Optional[DataSourceTable]]'] = Field(alias="availableTables")
    lookup_successful: Optional['bool'] = Field(alias="lookupSuccessful")
    message: Optional['str'] = Field(alias="message")
    translated_connector_message: Optional['TranslatedConnectorMessage'] = Field(alias="translatedConnectorMessage")


class DataSourceTable(PyCelonisBaseModel):
    data_source_id: Optional['str'] = Field(alias="dataSourceId")
    name: Optional['str'] = Field(alias="name")
    alias: Optional['str'] = Field(alias="alias")
    schema_: Optional['str'] = Field(alias="schema")


class LogTranslationParameter(PyCelonisBaseModel):
    key: Optional['str'] = Field(alias="key")
    value: Optional['str'] = Field(alias="value")


class TranslatedConnectorMessage(PyCelonisBaseModel):
    message_translation_code: Optional['ExecutionMessageCode'] = Field(alias="messageTranslationCode")
    log_translation_parameters: Optional['List[Optional[LogTranslationParameter]]'] = Field(
        alias="logTranslationParameters"
    )


class NameMappingTransport(PyCelonisBaseModel):
    identifier: Optional['str'] = Field(alias="identifier")
    translation: Optional['str'] = Field(alias="translation")
    language: Optional['str'] = Field(alias="language")
    description: Optional['str'] = Field(alias="description")
    mapping_type: Optional['str'] = Field(alias="mappingType")


class DataLoadHistoryTransport(PyCelonisBaseModel):
    data_model_id: Optional['str'] = Field(alias="dataModelId")
    data_load_id: Optional['str'] = Field(alias="dataLoadId")
    message: Optional['str'] = Field(alias="message")
    load_status: Optional['LoadStatus'] = Field(alias="loadStatus")
    start_date: Optional['datetime'] = Field(alias="startDate")
    end_date: Optional['datetime'] = Field(alias="endDate")
    warmup_duration: Optional['int'] = Field(alias="warmupDuration")
    done: Optional['bool'] = Field(alias="done")


class DataModelAverageTimeMapTransport(PyCelonisBaseModel):
    type_: Optional['DataLoadType'] = Field(alias="type")
    average_loading_time: Optional['int'] = Field(alias="averageLoadingTime")


class DataModelDataLoadHistoryTransport(PyCelonisBaseModel):
    data_load_id: Optional['str'] = Field(alias="dataLoadId")
    data_model_id: Optional['str'] = Field(alias="dataModelId")
    start_date: Optional['datetime'] = Field(alias="startDate")
    end_date: Optional['datetime'] = Field(alias="endDate")
    load_status: Optional['DataModelLoadStatus'] = Field(alias="loadStatus")
    message: Optional['str'] = Field(alias="message")
    load_type: Optional['DataLoadType'] = Field(alias="loadType")
    data_pool_version: Optional['str'] = Field(alias="dataPoolVersion")


class DataModelLoadHistoryTransport(PyCelonisBaseModel):
    last_successful_data_model: Optional['DataLoadHistoryTransport'] = Field(alias="lastSuccessfulDataModel")
    data_load_history: Optional['List[Optional[DataModelDataLoadHistoryTransport]]'] = Field(alias="dataLoadHistory")
    average_load_time: Optional['List[Optional[DataModelAverageTimeMapTransport]]'] = Field(alias="averageLoadTime")


class DataModelLoadInfoTransport(PyCelonisBaseModel):
    live_data_model: Optional['DataModelLoadTransport'] = Field(alias="liveDataModel")
    current_compute_load: Optional['DataModelDataLoadHistoryTransport'] = Field(alias="currentComputeLoad")


class DataModelLoadSyncTransport(PyCelonisBaseModel):
    load_info: Optional['DataModelLoadInfoTransport'] = Field(alias="loadInfo")
    load_history: Optional['DataModelLoadHistoryTransport'] = Field(alias="loadHistory")


class DataModelLoadTableTransport(PyCelonisBaseModel):
    table_id: Optional['str'] = Field(alias="tableId")
    table_name: Optional['str'] = Field(alias="tableName")
    table_row_count: Optional['int'] = Field(alias="tableRowCount")
    done: Optional['bool'] = Field(alias="done")
    invisible: Optional['bool'] = Field(alias="invisible")
    cancel: Optional['bool'] = Field(alias="cancel")


class DataModelLoadTransport(PyCelonisBaseModel):
    data_model_id: Optional['str'] = Field(alias="dataModelId")
    data_model_name: Optional['str'] = Field(alias="dataModelName")
    done: Optional['bool'] = Field(alias="done")
    error: Optional['bool'] = Field(alias="error")
    tables_loaded: Optional['bool'] = Field(alias="tablesLoaded")
    error_message: Optional['str'] = Field(alias="errorMessage")
    last_load: Optional['datetime'] = Field(alias="lastLoad")
    project_name: Optional['str'] = Field(alias="projectName")
    next_load: Optional['datetime'] = Field(alias="nextLoad")
    data_model_uuid: Optional['str'] = Field(alias="dataModelUUID")
    num_tables: Optional['int'] = Field(alias="numTables")
    scheduled_loading: Optional['bool'] = Field(alias="scheduledLoading")
    cancel: Optional['bool'] = Field(alias="cancel")
    table_loads: Optional['List[Optional[DataModelLoadTableTransport]]'] = Field(alias="tableLoads")
    start_time: Optional['datetime'] = Field(alias="startTime")
    end_time: Optional['datetime'] = Field(alias="endTime")
    response: Optional['str'] = Field(alias="response")
    data_load_id: Optional['str'] = Field(alias="dataLoadId")


class PoolColumn(PyCelonisBaseModel):
    name: Optional['str'] = Field(alias="name")
    length: Optional['int'] = Field(alias="length")
    type_: Optional['PoolColumnType'] = Field(alias="type")


class PoolTable(PyCelonisBaseModel):
    name: Optional['str'] = Field(alias="name")
    loader_source: Optional['str'] = Field(alias="loaderSource")
    available: Optional['bool'] = Field(alias="available")
    data_source_id: Optional['str'] = Field(alias="dataSourceId")
    data_source_name: Optional['str'] = Field(alias="dataSourceName")
    columns: Optional['List[Optional[PoolColumn]]'] = Field(alias="columns")
    type_: Optional['PropertyType'] = Field(alias="type")
    schema_name: Optional['str'] = Field(alias="schemaName")


LogMessageTransport.update_forward_refs()
LogMessageWithPageTransport.update_forward_refs()
FrontendHandledBackendError.update_forward_refs()
ExecutionItemWithPageTransport.update_forward_refs()
ExecutionItemTransport.update_forward_refs()
ExceptionReference.update_forward_refs()
ValidationError.update_forward_refs()
ValidationExceptionDescriptor.update_forward_refs()
TransformationTransport.update_forward_refs()
TaskUpdate.update_forward_refs()
TaskInstanceTransport.update_forward_refs()
CalculatedColumnTransport.update_forward_refs()
TableConfigurationParameterValue.update_forward_refs()
TableExtractionColumnTransport.update_forward_refs()
TableExtractionJoinTransport.update_forward_refs()
TableExtractionTransport.update_forward_refs()
JobTransport.update_forward_refs()
DataModelColumnTransport.update_forward_refs()
DataModelConfigurationTransport.update_forward_refs()
DataModelCustomCalendarEntryTransport.update_forward_refs()
DataModelCustomCalendarTransport.update_forward_refs()
DataModelFactoryCalendarTransport.update_forward_refs()
DataModelForeignKeyColumnTransport.update_forward_refs()
DataModelForeignKeyTransport.update_forward_refs()
DataModelTableTransport.update_forward_refs()
DataModelTransport.update_forward_refs()
DataModelConfiguration.update_forward_refs()
DataPoolTransport.update_forward_refs()
Tag.update_forward_refs()
CsvColumnParsingOptions.update_forward_refs()
CsvParsingOptions.update_forward_refs()
ColumnTransport.update_forward_refs()
DataPushJob.update_forward_refs()
TableTransport.update_forward_refs()
DataCommand.update_forward_refs()
DataExportRequest.update_forward_refs()
DataPermissionRule.update_forward_refs()
DataQuery.update_forward_refs()
Kpi.update_forward_refs()
KpiInformation.update_forward_refs()
QueryEnvironment.update_forward_refs()
DataExportStatusResponse.update_forward_refs()
NewTaskInstanceTransport.update_forward_refs()
DataModelExecutionTableItem.update_forward_refs()
DataModelExecutionTransport.update_forward_refs()
DataModelExecutionConfiguration.update_forward_refs()
ExtractionConfiguration.update_forward_refs()
JobExecutionConfiguration.update_forward_refs()
NameMappingAggregated.update_forward_refs()
NameMappingLoadReport.update_forward_refs()
DataPushChunk.update_forward_refs()
EntityStatus.update_forward_refs()
StatementTransport.update_forward_refs()
ExtractionConfigurationValueTransport.update_forward_refs()
ExtractionWithTablesTransport.update_forward_refs()
DataSourceTransport.update_forward_refs()
DataSourceAvailableTables.update_forward_refs()
DataSourceTable.update_forward_refs()
LogTranslationParameter.update_forward_refs()
TranslatedConnectorMessage.update_forward_refs()
NameMappingTransport.update_forward_refs()
DataLoadHistoryTransport.update_forward_refs()
DataModelAverageTimeMapTransport.update_forward_refs()
DataModelDataLoadHistoryTransport.update_forward_refs()
DataModelLoadHistoryTransport.update_forward_refs()
DataModelLoadInfoTransport.update_forward_refs()
DataModelLoadSyncTransport.update_forward_refs()
DataModelLoadTableTransport.update_forward_refs()
DataModelLoadTransport.update_forward_refs()
PoolColumn.update_forward_refs()
PoolTable.update_forward_refs()


class IntegrationService:
    @staticmethod
    def get_api_pools_pool_id_logs_executions(
        client: Client,
        pool_id: str,
        execution_id: Optional['str'] = None,
        type_: Optional['ExecutionType'] = None,
        id: Optional['str'] = None,
    ) -> List[Optional[ExecutionItemTransport]]:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/logs/executions'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/logs/executions",
                "tracking_type": "API_REQUEST",
            },
        )

        params: Dict[str, Any] = {}
        if execution_id:
            params["executionId"] = execution_id
        if type_:
            params["type"] = type_
        if id:
            params["id"] = id
        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/logs/executions",
            params=params,
            parse_json=True,
            type_=List[Optional[ExecutionItemTransport]],
        )

    @staticmethod
    def get_api_pools_pool_id_logs_job_id_executions(
        client: Client, pool_id: str, job_id: str, limit: Optional['int'] = None, page: Optional['int'] = None
    ) -> ExecutionItemWithPageTransport:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/logs/{job_id}/executions'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/logs/{job_id}/executions",
                "tracking_type": "API_REQUEST",
            },
        )

        params: Dict[str, Any] = {}
        if limit:
            params["limit"] = limit
        if page:
            params["page"] = page
        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/logs/{job_id}/executions",
            params=params,
            parse_json=True,
            type_=ExecutionItemWithPageTransport,
        )

    @staticmethod
    def get_api_pools_pool_id_logs_executions_detail(
        client: Client,
        pool_id: str,
        execution_id: Optional['str'] = None,
        id: Optional['str'] = None,
        type_: Optional['ExecutionType'] = None,
        limit: Optional['int'] = None,
        page: Optional['int'] = None,
        log_levels: Optional['List[Optional[LogLevel]]'] = None,
    ) -> LogMessageWithPageTransport:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/logs/executions/detail'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/logs/executions/detail",
                "tracking_type": "API_REQUEST",
            },
        )

        params: Dict[str, Any] = {}
        if execution_id:
            params["executionId"] = execution_id
        if id:
            params["id"] = id
        if type_:
            params["type"] = type_
        if limit:
            params["limit"] = limit
        if page:
            params["page"] = page
        if log_levels:
            params["logLevels"] = log_levels
        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/logs/executions/detail",
            params=params,
            parse_json=True,
            type_=LogMessageWithPageTransport,
        )

    @staticmethod
    def get_api_pools_pool_id_jobs_job_id_transformations_transformation_id_statement(
        client: Client, pool_id: str, job_id: str, transformation_id: str
    ) -> StatementTransport:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/jobs/{job_id}/transformations/{transformation_id}/statement'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/jobs/{job_id}/transformations/{transformation_id}/statement",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/jobs/{job_id}/transformations/{transformation_id}/statement",
            parse_json=True,
            type_=StatementTransport,
        )

    @staticmethod
    def put_api_pools_pool_id_jobs_job_id_transformations_transformation_id_statement(
        client: Client, pool_id: str, job_id: str, transformation_id: str, request_body: str
    ) -> TransformationTransport:
        logger.debug(
            f"Request: 'PUT' -> '/integration/api/pools/{pool_id}/jobs/{job_id}/transformations/{transformation_id}/statement'",
            extra={
                "request_type": "PUT",
                "path": "/integration/api/pools/{pool_id}/jobs/{job_id}/transformations/{transformation_id}/statement",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="PUT",
            url=f"/integration/api/pools/{pool_id}/jobs/{job_id}/transformations/{transformation_id}/statement",
            request_body=request_body,
            parse_json=True,
            type_=TransformationTransport,
        )

    @staticmethod
    def put_api_pools_pool_id_jobs_job_id_tasks_task_instance_id(
        client: Client, pool_id: str, job_id: str, task_instance_id: str, request_body: TaskUpdate
    ) -> TaskInstanceTransport:
        logger.debug(
            f"Request: 'PUT' -> '/integration/api/pools/{pool_id}/jobs/{job_id}/tasks/{task_instance_id}'",
            extra={
                "request_type": "PUT",
                "path": "/integration/api/pools/{pool_id}/jobs/{job_id}/tasks/{task_instance_id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="PUT",
            url=f"/integration/api/pools/{pool_id}/jobs/{job_id}/tasks/{task_instance_id}",
            request_body=request_body,
            parse_json=True,
            type_=TaskInstanceTransport,
        )

    @staticmethod
    def delete_api_pools_pool_id_jobs_job_id_tasks_task_instance_id(
        client: Client, pool_id: str, job_id: str, task_instance_id: str
    ) -> None:
        logger.debug(
            f"Request: 'DELETE' -> '/integration/api/pools/{pool_id}/jobs/{job_id}/tasks/{task_instance_id}'",
            extra={
                "request_type": "DELETE",
                "path": "/integration/api/pools/{pool_id}/jobs/{job_id}/tasks/{task_instance_id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="DELETE",
            url=f"/integration/api/pools/{pool_id}/jobs/{job_id}/tasks/{task_instance_id}",
        )

    @staticmethod
    def put_api_pools_pool_id_jobs_job_id_extractions_extraction_id_tables(
        client: Client,
        pool_id: str,
        job_id: str,
        extraction_id: str,
        request_body: List[Optional[TableExtractionTransport]],
    ) -> List[Optional[TableExtractionTransport]]:
        logger.debug(
            f"Request: 'PUT' -> '/integration/api/pools/{pool_id}/jobs/{job_id}/extractions/{extraction_id}/tables/'",
            extra={
                "request_type": "PUT",
                "path": "/integration/api/pools/{pool_id}/jobs/{job_id}/extractions/{extraction_id}/tables/",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="PUT",
            url=f"/integration/api/pools/{pool_id}/jobs/{job_id}/extractions/{extraction_id}/tables/",
            request_body=request_body,
            parse_json=True,
            type_=List[Optional[TableExtractionTransport]],
        )

    @staticmethod
    def post_api_pools_pool_id_jobs_job_id_extractions_extraction_id_tables(
        client: Client,
        pool_id: str,
        job_id: str,
        extraction_id: str,
        request_body: List[Optional[TableExtractionTransport]],
    ) -> List[Optional[TableExtractionTransport]]:
        logger.debug(
            f"Request: 'POST' -> '/integration/api/pools/{pool_id}/jobs/{job_id}/extractions/{extraction_id}/tables/'",
            extra={
                "request_type": "POST",
                "path": "/integration/api/pools/{pool_id}/jobs/{job_id}/extractions/{extraction_id}/tables/",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/integration/api/pools/{pool_id}/jobs/{job_id}/extractions/{extraction_id}/tables/",
            request_body=request_body,
            parse_json=True,
            type_=List[Optional[TableExtractionTransport]],
        )

    @staticmethod
    def get_api_pools_pool_id_jobs_id(client: Client, pool_id: str, id: str) -> JobTransport:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/jobs/{id}'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/jobs/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/jobs/{id}",
            parse_json=True,
            type_=JobTransport,
        )

    @staticmethod
    def put_api_pools_pool_id_jobs_id(
        client: Client, pool_id: str, id: str, request_body: JobTransport
    ) -> JobTransport:
        logger.debug(
            f"Request: 'PUT' -> '/integration/api/pools/{pool_id}/jobs/{id}'",
            extra={
                "request_type": "PUT",
                "path": "/integration/api/pools/{pool_id}/jobs/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="PUT",
            url=f"/integration/api/pools/{pool_id}/jobs/{id}",
            request_body=request_body,
            parse_json=True,
            type_=JobTransport,
        )

    @staticmethod
    def get_api_pools_pool_id_data_models_data_model_id(
        client: Client, pool_id: str, data_model_id: str
    ) -> DataModelTransport:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/data-models/{data_model_id}'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/data-models/{data_model_id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/data-models/{data_model_id}",
            parse_json=True,
            type_=DataModelTransport,
        )

    @staticmethod
    def put_api_pools_pool_id_data_models_data_model_id(
        client: Client, pool_id: str, data_model_id: str, request_body: DataModelTransport
    ) -> DataModelTransport:
        logger.debug(
            f"Request: 'PUT' -> '/integration/api/pools/{pool_id}/data-models/{data_model_id}'",
            extra={
                "request_type": "PUT",
                "path": "/integration/api/pools/{pool_id}/data-models/{data_model_id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="PUT",
            url=f"/integration/api/pools/{pool_id}/data-models/{data_model_id}",
            request_body=request_body,
            parse_json=True,
            type_=DataModelTransport,
        )

    @staticmethod
    def delete_api_pools_pool_id_data_models_data_model_id(client: Client, pool_id: str, data_model_id: str) -> None:
        logger.debug(
            f"Request: 'DELETE' -> '/integration/api/pools/{pool_id}/data-models/{data_model_id}'",
            extra={
                "request_type": "DELETE",
                "path": "/integration/api/pools/{pool_id}/data-models/{data_model_id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="DELETE",
            url=f"/integration/api/pools/{pool_id}/data-models/{data_model_id}",
        )

    @staticmethod
    def get_api_pools_pool_id_data_models_data_model_id_process_configurations(
        client: Client, pool_id: str, data_model_id: str
    ) -> List[Optional[DataModelConfiguration]]:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/data-models/{data_model_id}/process-configurations'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/data-models/{data_model_id}/process-configurations",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/data-models/{data_model_id}/process-configurations",
            parse_json=True,
            type_=List[Optional[DataModelConfiguration]],
        )

    @staticmethod
    def put_api_pools_pool_id_data_models_data_model_id_process_configurations(
        client: Client, pool_id: str, data_model_id: str, request_body: DataModelConfiguration
    ) -> DataModelConfiguration:
        logger.debug(
            f"Request: 'PUT' -> '/integration/api/pools/{pool_id}/data-models/{data_model_id}/process-configurations'",
            extra={
                "request_type": "PUT",
                "path": "/integration/api/pools/{pool_id}/data-models/{data_model_id}/process-configurations",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="PUT",
            url=f"/integration/api/pools/{pool_id}/data-models/{data_model_id}/process-configurations",
            request_body=request_body,
            parse_json=True,
            type_=DataModelConfiguration,
        )

    @staticmethod
    def get_api_pools_pool_id_data_models_data_model_id_foreign_keys_id(
        client: Client, pool_id: str, data_model_id: str, id: str
    ) -> DataModelForeignKeyTransport:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/data-models/{data_model_id}/foreign-keys/{id}'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/data-models/{data_model_id}/foreign-keys/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/data-models/{data_model_id}/foreign-keys/{id}",
            parse_json=True,
            type_=DataModelForeignKeyTransport,
        )

    @staticmethod
    def put_api_pools_pool_id_data_models_data_model_id_foreign_keys_id(
        client: Client, pool_id: str, data_model_id: str, id: str, request_body: DataModelForeignKeyTransport
    ) -> DataModelForeignKeyTransport:
        logger.debug(
            f"Request: 'PUT' -> '/integration/api/pools/{pool_id}/data-models/{data_model_id}/foreign-keys/{id}'",
            extra={
                "request_type": "PUT",
                "path": "/integration/api/pools/{pool_id}/data-models/{data_model_id}/foreign-keys/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="PUT",
            url=f"/integration/api/pools/{pool_id}/data-models/{data_model_id}/foreign-keys/{id}",
            request_body=request_body,
            parse_json=True,
            type_=DataModelForeignKeyTransport,
        )

    @staticmethod
    def delete_api_pools_pool_id_data_models_data_model_id_foreign_keys_id(
        client: Client, pool_id: str, data_model_id: str, id: str
    ) -> None:
        logger.debug(
            f"Request: 'DELETE' -> '/integration/api/pools/{pool_id}/data-models/{data_model_id}/foreign-keys/{id}'",
            extra={
                "request_type": "DELETE",
                "path": "/integration/api/pools/{pool_id}/data-models/{data_model_id}/foreign-keys/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="DELETE",
            url=f"/integration/api/pools/{pool_id}/data-models/{data_model_id}/foreign-keys/{id}",
        )

    @staticmethod
    def get_api_pools_pool_id_data_model_data_model_id_tables_id(
        client: Client, pool_id: str, data_model_id: str, id: str
    ) -> DataModelTableTransport:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/data-model/{data_model_id}/tables/{id}'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/data-model/{data_model_id}/tables/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/data-model/{data_model_id}/tables/{id}",
            parse_json=True,
            type_=DataModelTableTransport,
        )

    @staticmethod
    def put_api_pools_pool_id_data_model_data_model_id_tables_id(
        client: Client, pool_id: str, data_model_id: str, id: str, request_body: DataModelTableTransport
    ) -> DataModelTableTransport:
        logger.debug(
            f"Request: 'PUT' -> '/integration/api/pools/{pool_id}/data-model/{data_model_id}/tables/{id}'",
            extra={
                "request_type": "PUT",
                "path": "/integration/api/pools/{pool_id}/data-model/{data_model_id}/tables/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="PUT",
            url=f"/integration/api/pools/{pool_id}/data-model/{data_model_id}/tables/{id}",
            request_body=request_body,
            parse_json=True,
            type_=DataModelTableTransport,
        )

    @staticmethod
    def get_api_pools_id(client: Client, id: str) -> DataPoolTransport:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{id}'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{id}",
            parse_json=True,
            type_=DataPoolTransport,
        )

    @staticmethod
    def put_api_pools_id(client: Client, id: str, request_body: DataPoolTransport) -> DataPoolTransport:
        logger.debug(
            f"Request: 'PUT' -> '/integration/api/pools/{id}'",
            extra={
                "request_type": "PUT",
                "path": "/integration/api/pools/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="PUT",
            url=f"/integration/api/pools/{id}",
            request_body=request_body,
            parse_json=True,
            type_=DataPoolTransport,
        )

    @staticmethod
    def delete_api_pools_id(client: Client, id: str) -> None:
        logger.debug(
            f"Request: 'DELETE' -> '/integration/api/pools/{id}'",
            extra={
                "request_type": "DELETE",
                "path": "/integration/api/pools/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="DELETE",
            url=f"/integration/api/pools/{id}",
        )

    @staticmethod
    def get_api_v1_data_push_pool_id_jobs_id(client: Client, pool_id: str, id: str) -> DataPushJob:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/v1/data-push/{pool_id}/jobs/{id}'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/v1/data-push/{pool_id}/jobs/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/v1/data-push/{pool_id}/jobs/{id}",
            parse_json=True,
            type_=DataPushJob,
        )

    @staticmethod
    def post_api_v1_data_push_pool_id_jobs_id(
        client: Client, pool_id: str, id: str, duplicate_removal_column: Optional['str'] = None
    ) -> None:
        logger.debug(
            f"Request: 'POST' -> '/integration/api/v1/data-push/{pool_id}/jobs/{id}'",
            extra={
                "request_type": "POST",
                "path": "/integration/api/v1/data-push/{pool_id}/jobs/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        params: Dict[str, Any] = {}
        if duplicate_removal_column:
            params["duplicateRemovalColumn"] = duplicate_removal_column
        return client.request(
            method="POST",
            url=f"/integration/api/v1/data-push/{pool_id}/jobs/{id}",
            params=params,
        )

    @staticmethod
    def delete_api_v1_data_push_pool_id_jobs_id(client: Client, pool_id: str, id: str) -> None:
        logger.debug(
            f"Request: 'DELETE' -> '/integration/api/v1/data-push/{pool_id}/jobs/{id}'",
            extra={
                "request_type": "DELETE",
                "path": "/integration/api/v1/data-push/{pool_id}/jobs/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="DELETE",
            url=f"/integration/api/v1/data-push/{pool_id}/jobs/{id}",
        )

    @staticmethod
    def post_api_v1_data_push_pool_id_jobs_id_chunks_upserted(
        client: Client, pool_id: str, id: str, request_body: Dict[str, Any]
    ) -> None:
        logger.debug(
            f"Request: 'POST' -> '/integration/api/v1/data-push/{pool_id}/jobs/{id}/chunks/upserted'",
            extra={
                "request_type": "POST",
                "path": "/integration/api/v1/data-push/{pool_id}/jobs/{id}/chunks/upserted",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/integration/api/v1/data-push/{pool_id}/jobs/{id}/chunks/upserted",
            request_body=request_body,
        )

    @staticmethod
    def get_api_v1_data_push_pool_id_jobs(client: Client, pool_id: str) -> List[Optional[DataPushJob]]:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/v1/data-push/{pool_id}/jobs/'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/v1/data-push/{pool_id}/jobs/",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/v1/data-push/{pool_id}/jobs/",
            parse_json=True,
            type_=List[Optional[DataPushJob]],
        )

    @staticmethod
    def post_api_v1_data_push_pool_id_jobs(client: Client, pool_id: str, request_body: DataPushJob) -> DataPushJob:
        logger.debug(
            f"Request: 'POST' -> '/integration/api/v1/data-push/{pool_id}/jobs/'",
            extra={
                "request_type": "POST",
                "path": "/integration/api/v1/data-push/{pool_id}/jobs/",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/integration/api/v1/data-push/{pool_id}/jobs/",
            request_body=request_body,
            parse_json=True,
            type_=DataPushJob,
        )

    @staticmethod
    def post_api_v1_data_pools_pool_id_data_models_data_model_id_load_partial_sync(
        client: Client,
        pool_id: str,
        data_model_id: str,
        request_body: List[Optional[str]],
        full_reload: Optional['bool'] = None,
    ) -> None:
        logger.debug(
            f"Request: 'POST' -> '/integration/api/v1/data-pools/{pool_id}/data-models/{data_model_id}/load/partial-sync'",
            extra={
                "request_type": "POST",
                "path": "/integration/api/v1/data-pools/{pool_id}/data-models/{data_model_id}/load/partial-sync",
                "tracking_type": "API_REQUEST",
            },
        )

        params: Dict[str, Any] = {}
        if full_reload:
            params["fullReload"] = full_reload
        return client.request(
            method="POST",
            url=f"/integration/api/v1/data-pools/{pool_id}/data-models/{data_model_id}/load/partial-sync",
            params=params,
            request_body=request_body,
        )

    @staticmethod
    def post_api_v1_compute_data_model_id_export_query(
        client: Client, data_model_id: str, request_body: DataExportRequest
    ) -> DataExportStatusResponse:
        logger.debug(
            f"Request: 'POST' -> '/integration/api/v1/compute/{data_model_id}/export/query'",
            extra={
                "request_type": "POST",
                "path": "/integration/api/v1/compute/{data_model_id}/export/query",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/integration/api/v1/compute/{data_model_id}/export/query",
            request_body=request_body,
            parse_json=True,
            type_=DataExportStatusResponse,
        )

    @staticmethod
    def get_api_pools(
        client: Client, team_domain: Optional['str'] = None, pool_ids: Optional['List[Optional[str]]'] = None
    ) -> List[Optional[DataPoolTransport]]:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools",
                "tracking_type": "API_REQUEST",
            },
        )

        params: Dict[str, Any] = {}
        if team_domain:
            params["teamDomain"] = team_domain
        if pool_ids:
            params["poolIds"] = pool_ids
        return client.request(
            method="GET",
            url=f"/integration/api/pools",
            params=params,
            parse_json=True,
            type_=List[Optional[DataPoolTransport]],
        )

    @staticmethod
    def post_api_pools(client: Client, request_body: DataPoolTransport) -> DataPoolTransport:
        logger.debug(
            f"Request: 'POST' -> '/integration/api/pools'",
            extra={
                "request_type": "POST",
                "path": "/integration/api/pools",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/integration/api/pools",
            request_body=request_body,
            parse_json=True,
            type_=DataPoolTransport,
        )

    @staticmethod
    def get_api_pools_pool_id_jobs(client: Client, pool_id: str) -> List[Optional[JobTransport]]:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/jobs'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/jobs",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/jobs",
            parse_json=True,
            type_=List[Optional[JobTransport]],
        )

    @staticmethod
    def post_api_pools_pool_id_jobs(client: Client, pool_id: str, request_body: JobTransport) -> JobTransport:
        logger.debug(
            f"Request: 'POST' -> '/integration/api/pools/{pool_id}/jobs'",
            extra={
                "request_type": "POST",
                "path": "/integration/api/pools/{pool_id}/jobs",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/integration/api/pools/{pool_id}/jobs",
            request_body=request_body,
            parse_json=True,
            type_=JobTransport,
        )

    @staticmethod
    def get_api_pools_pool_id_jobs_job_id_tasks(
        client: Client, pool_id: str, job_id: str
    ) -> List[Optional[TaskInstanceTransport]]:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/jobs/{job_id}/tasks/'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/jobs/{job_id}/tasks/",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/jobs/{job_id}/tasks/",
            parse_json=True,
            type_=List[Optional[TaskInstanceTransport]],
        )

    @staticmethod
    def post_api_pools_pool_id_jobs_job_id_tasks(
        client: Client, pool_id: str, job_id: str, request_body: NewTaskInstanceTransport
    ) -> TaskInstanceTransport:
        logger.debug(
            f"Request: 'POST' -> '/integration/api/pools/{pool_id}/jobs/{job_id}/tasks/'",
            extra={
                "request_type": "POST",
                "path": "/integration/api/pools/{pool_id}/jobs/{job_id}/tasks/",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/integration/api/pools/{pool_id}/jobs/{job_id}/tasks/",
            request_body=request_body,
            parse_json=True,
            type_=TaskInstanceTransport,
        )

    @staticmethod
    def get_api_pools_pool_id_jobs_job_id_loads(
        client: Client, pool_id: str, job_id: str
    ) -> List[Optional[DataModelExecutionTransport]]:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/jobs/{job_id}/loads'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/jobs/{job_id}/loads",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/jobs/{job_id}/loads",
            parse_json=True,
            type_=List[Optional[DataModelExecutionTransport]],
        )

    @staticmethod
    def post_api_pools_pool_id_jobs_job_id_loads(
        client: Client, pool_id: str, job_id: str, request_body: DataModelExecutionTransport
    ) -> DataModelExecutionTransport:
        logger.debug(
            f"Request: 'POST' -> '/integration/api/pools/{pool_id}/jobs/{job_id}/loads'",
            extra={
                "request_type": "POST",
                "path": "/integration/api/pools/{pool_id}/jobs/{job_id}/loads",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/integration/api/pools/{pool_id}/jobs/{job_id}/loads",
            request_body=request_body,
            parse_json=True,
            type_=DataModelExecutionTransport,
        )

    @staticmethod
    def post_api_pools_pool_id_jobs_job_id_execute(
        client: Client, pool_id: str, job_id: str, request_body: JobExecutionConfiguration
    ) -> None:
        logger.debug(
            f"Request: 'POST' -> '/integration/api/pools/{pool_id}/jobs/{job_id}/execute'",
            extra={
                "request_type": "POST",
                "path": "/integration/api/pools/{pool_id}/jobs/{job_id}/execute",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/integration/api/pools/{pool_id}/jobs/{job_id}/execute",
            request_body=request_body,
        )

    @staticmethod
    def get_api_pools_pool_id_data_models(
        client: Client, pool_id: str, limit: Optional['int'] = None
    ) -> List[Optional[DataModelTransport]]:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/data-models'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/data-models",
                "tracking_type": "API_REQUEST",
            },
        )

        params: Dict[str, Any] = {}
        if limit:
            params["limit"] = limit
        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/data-models",
            params=params,
            parse_json=True,
            type_=List[Optional[DataModelTransport]],
        )

    @staticmethod
    def post_api_pools_pool_id_data_models(
        client: Client, pool_id: str, request_body: DataModelTransport
    ) -> DataModelTransport:
        logger.debug(
            f"Request: 'POST' -> '/integration/api/pools/{pool_id}/data-models'",
            extra={
                "request_type": "POST",
                "path": "/integration/api/pools/{pool_id}/data-models",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/integration/api/pools/{pool_id}/data-models",
            request_body=request_body,
            parse_json=True,
            type_=DataModelTransport,
        )

    @staticmethod
    def post_api_pools_pool_id_data_models_data_model_id_reload(
        client: Client, pool_id: str, data_model_id: str, force_complete: Optional['bool'] = None
    ) -> None:
        logger.debug(
            f"Request: 'POST' -> '/integration/api/pools/{pool_id}/data-models/{data_model_id}/reload'",
            extra={
                "request_type": "POST",
                "path": "/integration/api/pools/{pool_id}/data-models/{data_model_id}/reload",
                "tracking_type": "API_REQUEST",
            },
        )

        params: Dict[str, Any] = {}
        if force_complete:
            params["forceComplete"] = force_complete
        return client.request(
            method="POST",
            url=f"/integration/api/pools/{pool_id}/data-models/{data_model_id}/reload",
            params=params,
        )

    @staticmethod
    def post_api_pools_pool_id_data_models_data_model_id_name_mapping_file(
        client: Client, pool_id: str, data_model_id: str, request_body: Dict[str, Any]
    ) -> NameMappingLoadReport:
        logger.debug(
            f"Request: 'POST' -> '/integration/api/pools/{pool_id}/data-models/{data_model_id}/name-mapping/file'",
            extra={
                "request_type": "POST",
                "path": "/integration/api/pools/{pool_id}/data-models/{data_model_id}/name-mapping/file",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/integration/api/pools/{pool_id}/data-models/{data_model_id}/name-mapping/file",
            request_body=request_body,
            parse_json=True,
            type_=NameMappingLoadReport,
        )

    @staticmethod
    def get_api_pools_pool_id_data_models_data_model_id_foreign_keys(
        client: Client, pool_id: str, data_model_id: str
    ) -> List[Optional[DataModelForeignKeyTransport]]:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/data-models/{data_model_id}/foreign-keys'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/data-models/{data_model_id}/foreign-keys",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/data-models/{data_model_id}/foreign-keys",
            parse_json=True,
            type_=List[Optional[DataModelForeignKeyTransport]],
        )

    @staticmethod
    def post_api_pools_pool_id_data_models_data_model_id_foreign_keys(
        client: Client, pool_id: str, data_model_id: str, request_body: DataModelForeignKeyTransport
    ) -> DataModelForeignKeyTransport:
        logger.debug(
            f"Request: 'POST' -> '/integration/api/pools/{pool_id}/data-models/{data_model_id}/foreign-keys'",
            extra={
                "request_type": "POST",
                "path": "/integration/api/pools/{pool_id}/data-models/{data_model_id}/foreign-keys",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/integration/api/pools/{pool_id}/data-models/{data_model_id}/foreign-keys",
            request_body=request_body,
            parse_json=True,
            type_=DataModelForeignKeyTransport,
        )

    @staticmethod
    def get_api_pools_pool_id_data_model_data_model_id_tables(
        client: Client, pool_id: str, data_model_id: str
    ) -> List[Optional[DataModelTableTransport]]:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/data-model/{data_model_id}/tables'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/data-model/{data_model_id}/tables",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/data-model/{data_model_id}/tables",
            parse_json=True,
            type_=List[Optional[DataModelTableTransport]],
        )

    @staticmethod
    def post_api_pools_pool_id_data_model_data_model_id_tables(
        client: Client, pool_id: str, data_model_id: str, request_body: List[Optional[DataModelTableTransport]]
    ) -> List[Optional[DataModelTableTransport]]:
        logger.debug(
            f"Request: 'POST' -> '/integration/api/pools/{pool_id}/data-model/{data_model_id}/tables'",
            extra={
                "request_type": "POST",
                "path": "/integration/api/pools/{pool_id}/data-model/{data_model_id}/tables",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/integration/api/pools/{pool_id}/data-model/{data_model_id}/tables",
            request_body=request_body,
            parse_json=True,
            type_=List[Optional[DataModelTableTransport]],
        )

    @staticmethod
    def get_api_v1_data_push_pool_id_jobs_id_chunks(
        client: Client, pool_id: str, id: str
    ) -> List[Optional[DataPushChunk]]:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/v1/data-push/{pool_id}/jobs/{id}/chunks'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/v1/data-push/{pool_id}/jobs/{id}/chunks",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/v1/data-push/{pool_id}/jobs/{id}/chunks",
            parse_json=True,
            type_=List[Optional[DataPushChunk]],
        )

    @staticmethod
    def get_api_v1_compute_data_model_id_export_export_id(
        client: Client, data_model_id: str, export_id: str
    ) -> DataExportStatusResponse:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/v1/compute/{data_model_id}/export/{export_id}'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/v1/compute/{data_model_id}/export/{export_id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/v1/compute/{data_model_id}/export/{export_id}",
            parse_json=True,
            type_=DataExportStatusResponse,
        )

    @staticmethod
    def get_api_v1_compute_data_model_id_export_export_id_chunk_id_result(
        client: Client, data_model_id: str, export_id: str, chunk_id: str
    ) -> BytesIO:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/v1/compute/{data_model_id}/export/{export_id}/{chunk_id}/result'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/v1/compute/{data_model_id}/export/{export_id}/{chunk_id}/result",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/v1/compute/{data_model_id}/export/{export_id}/{chunk_id}/result",
            parse_json=True,
            type_=BytesIO,
        )

    @staticmethod
    def get_api_v1_compute_data_model_id_export_export_id_result(
        client: Client, data_model_id: str, export_id: str
    ) -> BytesIO:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/v1/compute/{data_model_id}/export/{export_id}/result'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/v1/compute/{data_model_id}/export/{export_id}/result",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/v1/compute/{data_model_id}/export/{export_id}/result",
            parse_json=True,
            type_=BytesIO,
        )

    @staticmethod
    def get_api_pools_pool_id_logs_status(client: Client, pool_id: str) -> List[Optional[EntityStatus]]:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/logs/status'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/logs/status",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/logs/status",
            parse_json=True,
            type_=List[Optional[EntityStatus]],
        )

    @staticmethod
    def get_api_pools_pool_id_jobs_job_id_extractions_extraction_id_tables_table_id(
        client: Client, pool_id: str, job_id: str, extraction_id: str, table_id: str
    ) -> TableExtractionTransport:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/jobs/{job_id}/extractions/{extraction_id}/tables/{table_id}'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/jobs/{job_id}/extractions/{extraction_id}/tables/{table_id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/jobs/{job_id}/extractions/{extraction_id}/tables/{table_id}",
            parse_json=True,
            type_=TableExtractionTransport,
        )

    @staticmethod
    def delete_api_pools_pool_id_jobs_job_id_extractions_extraction_id_tables_table_id(
        client: Client, pool_id: str, job_id: str, extraction_id: str, table_id: str
    ) -> None:
        logger.debug(
            f"Request: 'DELETE' -> '/integration/api/pools/{pool_id}/jobs/{job_id}/extractions/{extraction_id}/tables/{table_id}'",
            extra={
                "request_type": "DELETE",
                "path": "/integration/api/pools/{pool_id}/jobs/{job_id}/extractions/{extraction_id}/tables/{table_id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="DELETE",
            url=f"/integration/api/pools/{pool_id}/jobs/{job_id}/extractions/{extraction_id}/tables/{table_id}",
        )

    @staticmethod
    def get_api_pools_pool_id_jobs_job_id_extractions_extraction_id_expanded(
        client: Client, pool_id: str, job_id: str, extraction_id: str
    ) -> ExtractionWithTablesTransport:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/jobs/{job_id}/extractions/{extraction_id}/expanded'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/jobs/{job_id}/extractions/{extraction_id}/expanded",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/jobs/{job_id}/extractions/{extraction_id}/expanded",
            parse_json=True,
            type_=ExtractionWithTablesTransport,
        )

    @staticmethod
    def get_api_pools_pool_id_data_sources_data_source_id(
        client: Client, pool_id: str, data_source_id: str
    ) -> DataSourceTransport:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/data-sources/{data_source_id}'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/data-sources/{data_source_id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/data-sources/{data_source_id}",
            parse_json=True,
            type_=DataSourceTransport,
        )

    @staticmethod
    def delete_api_pools_pool_id_data_sources_data_source_id(client: Client, pool_id: str, data_source_id: str) -> None:
        logger.debug(
            f"Request: 'DELETE' -> '/integration/api/pools/{pool_id}/data-sources/{data_source_id}'",
            extra={
                "request_type": "DELETE",
                "path": "/integration/api/pools/{pool_id}/data-sources/{data_source_id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="DELETE",
            url=f"/integration/api/pools/{pool_id}/data-sources/{data_source_id}",
        )

    @staticmethod
    def get_api_pools_pool_id_data_sources_data_source_id_search_tables(
        client: Client,
        pool_id: str,
        data_source_id: str,
        extraction_id: Optional['str'] = None,
        search_string: Optional['str'] = None,
    ) -> DataSourceAvailableTables:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/data-sources/{data_source_id}/search-tables'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/data-sources/{data_source_id}/search-tables",
                "tracking_type": "API_REQUEST",
            },
        )

        params: Dict[str, Any] = {}
        if extraction_id:
            params["extractionId"] = extraction_id
        if search_string:
            params["searchString"] = search_string
        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/data-sources/{data_source_id}/search-tables",
            params=params,
            parse_json=True,
            type_=DataSourceAvailableTables,
        )

    @staticmethod
    def get_api_pools_pool_id_data_sources(
        client: Client,
        pool_id: str,
        exclude_unconfigured: Optional['bool'] = None,
        distinct: Optional['bool'] = None,
        type_: Optional['str'] = None,
        limit: Optional['int'] = None,
        exclude_only_realtime_connectors: Optional['bool'] = None,
    ) -> List[Optional[DataSourceTransport]]:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/data-sources/'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/data-sources/",
                "tracking_type": "API_REQUEST",
            },
        )

        params: Dict[str, Any] = {}
        if exclude_unconfigured:
            params["excludeUnconfigured"] = exclude_unconfigured
        if distinct:
            params["distinct"] = distinct
        if type_:
            params["type"] = type_
        if limit:
            params["limit"] = limit
        if exclude_only_realtime_connectors:
            params["excludeOnlyRealtimeConnectors"] = exclude_only_realtime_connectors
        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/data-sources/",
            params=params,
            parse_json=True,
            type_=List[Optional[DataSourceTransport]],
        )

    @staticmethod
    def get_api_pools_pool_id_data_models_data_model_id_process_configurations_activity_table_activity_table_id(
        client: Client, pool_id: str, data_model_id: str, activity_table_id: str
    ) -> DataModelConfiguration:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/data-models/{data_model_id}/process-configurations/activityTable/{activity_table_id}'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/data-models/{data_model_id}/process-configurations/activityTable/{activity_table_id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/data-models/{data_model_id}/process-configurations/activityTable/{activity_table_id}",
            parse_json=True,
            type_=DataModelConfiguration,
        )

    @staticmethod
    def get_api_pools_pool_id_data_models_data_model_id_name_mapping(
        client: Client, pool_id: str, data_model_id: str
    ) -> List[Optional[NameMappingTransport]]:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/data-models/{data_model_id}/name-mapping'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/data-models/{data_model_id}/name-mapping",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/data-models/{data_model_id}/name-mapping",
            parse_json=True,
            type_=List[Optional[NameMappingTransport]],
        )

    @staticmethod
    def delete_api_pools_pool_id_data_models_data_model_id_name_mapping(
        client: Client, pool_id: str, data_model_id: str
    ) -> None:
        logger.debug(
            f"Request: 'DELETE' -> '/integration/api/pools/{pool_id}/data-models/{data_model_id}/name-mapping'",
            extra={
                "request_type": "DELETE",
                "path": "/integration/api/pools/{pool_id}/data-models/{data_model_id}/name-mapping",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="DELETE",
            url=f"/integration/api/pools/{pool_id}/data-models/{data_model_id}/name-mapping",
        )

    @staticmethod
    def get_api_pools_pool_id_data_models_data_model_id_load_history_load_info_sync(
        client: Client, pool_id: str, data_model_id: str
    ) -> DataModelLoadSyncTransport:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/data-models/{data_model_id}/load-history/load-info-sync'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/data-models/{data_model_id}/load-history/load-info-sync",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/data-models/{data_model_id}/load-history/load-info-sync",
            parse_json=True,
            type_=DataModelLoadSyncTransport,
        )

    @staticmethod
    def get_api_pools_pool_id_data_model_data_model_id_tables_table_id_columns(
        client: Client, pool_id: str, data_model_id: str, table_id: str
    ) -> List[Optional[PoolColumn]]:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{pool_id}/data-model/{data_model_id}/tables/{table_id}/columns'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{pool_id}/data-model/{data_model_id}/tables/{table_id}/columns",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{pool_id}/data-model/{data_model_id}/tables/{table_id}/columns",
            parse_json=True,
            type_=List[Optional[PoolColumn]],
        )

    @staticmethod
    def get_api_pools_id_tables(client: Client, id: str) -> List[Optional[PoolTable]]:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{id}/tables'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{id}/tables",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="GET",
            url=f"/integration/api/pools/{id}/tables",
            parse_json=True,
            type_=List[Optional[PoolTable]],
        )

    @staticmethod
    def get_api_pools_id_columns(
        client: Client, id: str, table_name: Optional['str'] = None, schema_name: Optional['str'] = None
    ) -> List[Optional[PoolColumn]]:
        logger.debug(
            f"Request: 'GET' -> '/integration/api/pools/{id}/columns'",
            extra={
                "request_type": "GET",
                "path": "/integration/api/pools/{id}/columns",
                "tracking_type": "API_REQUEST",
            },
        )

        params: Dict[str, Any] = {}
        if table_name:
            params["tableName"] = table_name
        if schema_name:
            params["schemaName"] = schema_name
        return client.request(
            method="GET",
            url=f"/integration/api/pools/{id}/columns",
            params=params,
            parse_json=True,
            type_=List[Optional[PoolColumn]],
        )

    @staticmethod
    def delete_api_pools_pool_id_jobs_job_id(client: Client, pool_id: str, job_id: str) -> None:
        logger.debug(
            f"Request: 'DELETE' -> '/integration/api/pools/{pool_id}/jobs/{job_id}'",
            extra={
                "request_type": "DELETE",
                "path": "/integration/api/pools/{pool_id}/jobs/{job_id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="DELETE",
            url=f"/integration/api/pools/{pool_id}/jobs/{job_id}",
        )

    @staticmethod
    def delete_api_pools_pool_id_jobs_job_id_loads_id(client: Client, pool_id: str, job_id: str, id: str) -> None:
        logger.debug(
            f"Request: 'DELETE' -> '/integration/api/pools/{pool_id}/jobs/{job_id}/loads/{id}'",
            extra={
                "request_type": "DELETE",
                "path": "/integration/api/pools/{pool_id}/jobs/{job_id}/loads/{id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="DELETE",
            url=f"/integration/api/pools/{pool_id}/jobs/{job_id}/loads/{id}",
        )

    @staticmethod
    def delete_api_pools_pool_id_data_models_data_model_id_process_configurations_process_configuration_id(
        client: Client, pool_id: str, data_model_id: str, process_configuration_id: str
    ) -> None:
        logger.debug(
            f"Request: 'DELETE' -> '/integration/api/pools/{pool_id}/data-models/{data_model_id}/process-configurations/{process_configuration_id}'",
            extra={
                "request_type": "DELETE",
                "path": "/integration/api/pools/{pool_id}/data-models/{data_model_id}/process-configurations/{process_configuration_id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="DELETE",
            url=f"/integration/api/pools/{pool_id}/data-models/{data_model_id}/process-configurations/{process_configuration_id}",
        )

    @staticmethod
    def delete_api_pools_pool_id_data_model_data_model_id_tables_table_id(
        client: Client, pool_id: str, data_model_id: str, table_id: str
    ) -> None:
        logger.debug(
            f"Request: 'DELETE' -> '/integration/api/pools/{pool_id}/data-model/{data_model_id}/tables/{table_id}'",
            extra={
                "request_type": "DELETE",
                "path": "/integration/api/pools/{pool_id}/data-model/{data_model_id}/tables/{table_id}",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="DELETE",
            url=f"/integration/api/pools/{pool_id}/data-model/{data_model_id}/tables/{table_id}",
        )

    @staticmethod
    def post_api_pools_pool_id_jobs_job_id_tasks_task_instance_id_enabled(
        client: Client, pool_id: str, job_id: str, task_instance_id: str
    ) -> TaskInstanceTransport:
        logger.debug(
            f"Request: 'POST' -> '/integration/api/pools/{pool_id}/jobs/{job_id}/tasks/{task_instance_id}/enabled'",
            extra={
                "request_type": "POST",
                "path": "/integration/api/pools/{pool_id}/jobs/{job_id}/tasks/{task_instance_id}/enabled",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="POST",
            url=f"/integration/api/pools/{pool_id}/jobs/{job_id}/tasks/{task_instance_id}/enabled",
            parse_json=True,
            type_=TaskInstanceTransport,
        )

    @staticmethod
    def delete_api_pools_pool_id_jobs_job_id_tasks_task_instance_id_enabled(
        client: Client, pool_id: str, job_id: str, task_instance_id: str
    ) -> TaskInstanceTransport:
        logger.debug(
            f"Request: 'DELETE' -> '/integration/api/pools/{pool_id}/jobs/{job_id}/tasks/{task_instance_id}/enabled'",
            extra={
                "request_type": "DELETE",
                "path": "/integration/api/pools/{pool_id}/jobs/{job_id}/tasks/{task_instance_id}/enabled",
                "tracking_type": "API_REQUEST",
            },
        )

        return client.request(
            method="DELETE",
            url=f"/integration/api/pools/{pool_id}/jobs/{job_id}/tasks/{task_instance_id}/enabled",
            parse_json=True,
            type_=TaskInstanceTransport,
        )

