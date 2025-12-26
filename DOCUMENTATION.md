# PyCelonis Documentation

## Overview

PyCelonis is the official Python SDK for Celonis, a leading process mining and execution management platform. This package provides comprehensive programmatic access to Celonis Enterprise Mining Suite (EMS) services, enabling developers to automate process mining workflows, data integration tasks, and analytics operations.

**Version**: 2.20.1  
**Python Support**: 3.8+ (with compatibility notes for 3.13+)  
**License**: Proprietary (Celonis)

## Key Features

### 🔗 Core Connectivity
- **Secure Authentication**: Support for APP_KEY and USER_KEY authentication methods
- **Flexible Configuration**: Environment variables, direct parameters, or OAuth flows
- **Connection Management**: Automatic retry logic, SSL verification, proxy support
- **Version Checking**: Automatic detection of outdated package versions

### 📊 Data Integration
- **Data Pools**: Create, manage, and monitor data storage containers
- **Data Models**: Build and maintain process models with relationships
- **Jobs & Tasks**: Schedule and execute data extraction, transformation, and loading operations
- **Table Management**: Handle data tables, columns, and foreign key relationships
- **Data Export/Import**: Support for various data formats and sources

### 🎨 Studio & Apps
- **Space Management**: Organize analytical content in workspaces
- **Content Nodes**: Manage analysis views, dashboards, and reports
- **Application Development**: Build and deploy custom process mining applications

### 🔍 Process Query Language (PQL)
- **DataFrame API**: Pandas-like interface for process data manipulation
- **Series Operations**: Column-based data operations and transformations
- **Query Building**: Construct complex process queries programmatically
- **Debugging Tools**: Built-in query validation and performance analysis

### 👥 Team & Permissions
- **User Management**: Handle team members and access controls
- **Permission System**: Granular permission assignment and validation
- **Audit Trails**: Track changes and access patterns

### 🔧 Backend Services
- **Integration Services**: API endpoints for external system connectivity
- **Package Manager**: Handle custom extensions and plugins
- **Process Analytics**: Advanced process discovery and conformance checking
- **Semantic Layer**: Business terminology and metadata management

## Installation

### Prerequisites
- Python 3.8 or higher (Python 3.11 recommended for best compatibility)
- Access to Celonis EMS instance
- Valid API credentials (APP_KEY or USER_KEY)

### Setup Steps

1. **Create Virtual Environment**:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Unix/Mac:
   source .venv/bin/activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install --extra-index-url=https://pypi.celonis.cloud/ -r requirements.txt
   ```

3. **Alternative Direct Installation**:
   ```bash
   pip install --extra-index-url=https://pypi.celonis.cloud/ pycelonis pycelonis_core
   ```

### Required Dependencies
- `pycelonis_core==2.10.3`: Core Celonis functionality
- `httpx>=0.28.0`: HTTP client for API communication
- `pydantic>=2.0.0`: Data validation and serialization
- `pandas`: Data manipulation and analysis
- `pyarrow`: High-performance data processing
- `numpy`: Numerical computing
- `saolapy`: Celonis query engine integration

## Quick Start

### Basic Connection

```python
from pycelonis import get_celonis

# Using environment variables (recommended for production)
# Set CELONIS_URL and CELONIS_API_TOKEN environment variables
celonis = get_celonis()

# Or specify credentials directly
celonis = get_celonis(
    base_url="https://your-tenant.celonis.cloud/",
    api_token="your-api-token-here",
    key_type="APP_KEY"  # or "USER_KEY"
)
```

### Data Integration Example

```python
# List all data pools
data_pools = celonis.data_integration.get_data_pools()
print(f"Found {len(data_pools)} data pools")

# Create a new data pool
new_pool = celonis.data_integration.create_data_pool(
    name="My Analysis Pool",
    description="Data pool for process mining analysis"
)

# Get data models in a pool
data_models = new_pool.get_data_models()
```

### PQL Query Example

```python
from pycelonis.pql import PQL

# Connect to a data model
data_model = celonis.data_integration.get_data_model("your-data-model-id")

# Create PQL query
pql = PQL(data_model=data_model)

# Build query with filters and aggregations
query = pql.query("""
    CASE_TABLE."Case ID",
    COUNT(CASE_TABLE."Activity") AS "Activity Count",
    AVG(CASE_TABLE."Duration") AS "Avg Duration"
""").filter(
    CASE_TABLE."Status" == "Completed"
).groupby(
    CASE_TABLE."Case ID"
)

# Execute query
result = query.execute()
print(result.head())
```

## Architecture

### Core Classes

#### `Celonis`
Main entry point providing access to all EMS services.

**Attributes**:
- `data_integration`: DataIntegration service instance
- `studio`: Studio service instance  
- `apps`: Apps service instance
- `team`: Team service instance

#### `DataIntegration`
Handles all data-related operations.

**Key Methods**:
- `get_data_pools()`: List all data pools
- `create_data_pool(name, description)`: Create new data pool
- `get_data_model(id)`: Retrieve specific data model

#### `Studio`
Manages analytical content and workspaces.

**Key Methods**:
- `get_spaces()`: List all spaces
- `create_space(name, description)`: Create new workspace

#### `PQL`
Process Query Language interface for data analysis.

**Key Classes**:
- `DataFrame`: Tabular data representation
- `Series`: Column-based data operations
- `PQLColumn`: Query column definitions

### Service Layer

The package includes several service modules:

- **Integration Service**: External system connectivity
- **Package Manager Service**: Extension management
- **PQL Language Service**: Query parsing and validation
- **Process Analytics Service**: Advanced mining algorithms
- **Semantic Layer Service**: Business metadata management
- **Team Service**: User and permission management

## Authentication & Security

### Authentication Methods

1. **Application Key (APP_KEY)**:
   - Recommended for service accounts
   - Scoped permissions
   - No user context

2. **User Key (USER_KEY)**:
   - Personal authentication
   - Full user permissions
   - Audit trail with user identity

### Environment Variables

```bash
export CELONIS_URL="https://your-tenant.celonis.cloud/"
export CELONIS_API_TOKEN="your-token-here"
export CELONIS_KEY_TYPE="APP_KEY"
```

### OAuth Support

For advanced authentication scenarios, the SDK supports OAuth 2.0 flows through the `AuthToken` class.

## Data Operations

### Data Pool Management

```python
# Create data pool
pool = celonis.data_integration.create_data_pool(
    name="Production Data",
    description="Main production data pool"
)

# Configure pool settings
pool.update_settings(
    schema_name="production_schema",
    connection_type="SNOWFLAKE"
)

# List tables in pool
tables = pool.get_tables()
```

### Data Model Operations

```python
# Get data model
model = celonis.data_integration.get_data_model("model-id")

# Reload data model
model.reload()

# Get model statistics
stats = model.get_statistics()
print(f"Tables: {stats.table_count}, Rows: {stats.row_count}")
```

### Job Execution

```python
# Create extraction job
job = pool.create_job(
    name="Daily Extract",
    description="Extract sales data daily",
    schedule_type="SCHEDULED"
)

# Execute job immediately
execution = job.execute()

# Monitor execution
while not execution.is_finished():
    status = execution.get_status()
    print(f"Progress: {status.progress}%")
    time.sleep(10)
```

## Process Mining with PQL

### Basic Queries

```python
from pycelonis.pql import PQL

pql = PQL(data_model=data_model)

# Simple case count
result = pql.query("COUNT(CASE_TABLE.\"Case ID\")").execute()

# Activity frequency analysis
activity_freq = pql.query("""
    ACTIVITY_TABLE."Activity",
    COUNT(ACTIVITY_TABLE."Activity") AS "Frequency"
""").groupby(
    ACTIVITY_TABLE."Activity"
).orderby(
    "Frequency", ascending=False
).execute()
```

### Advanced Analytics

```python
# Process flow analysis
flow_analysis = pql.query("""
    SOURCE_ACTIVITY."Activity" AS "From",
    TARGET_ACTIVITY."Activity" AS "To", 
    COUNT(*) AS "Flow Count"
""").filter(
    SOURCE_ACTIVITY."Case ID" == TARGET_ACTIVITY."Case ID"
).groupby(
    "From", "To"
).execute()

# Performance metrics
performance = pql.query("""
    CASE_TABLE."Case ID",
    MIN(ACTIVITY_TABLE."Timestamp") AS "Start Time",
    MAX(ACTIVITY_TABLE."Timestamp") AS "End Time",
    DATEDIFF(day, "Start Time", "End Time") AS "Duration"
""").execute()
```

## Studio & Content Management

### Space Operations

```python
# List all spaces
spaces = celonis.studio.get_spaces()

# Create analysis space
analysis_space = celonis.studio.create_space(
    name="Process Analysis",
    description="Space for process mining analyses"
)

# Get space content
content = analysis_space.get_content_nodes()
```

### Content Management

```python
# Upload analysis
analysis = analysis_space.upload_analysis(
    file_path="process_analysis.json",
    name="Order Fulfillment Analysis"
)

# Share content
analysis.share_with_team(team_id="team-uuid")

# Export content
exported = analysis.export(format="PDF")
```

## Application Development

### Custom Apps

```python
# List available apps
apps = celonis.apps.get_apps()

# Deploy custom app
app = celonis.apps.deploy_app(
    package_path="my-app.zip",
    name="Custom Process Monitor"
)

# Configure app settings
app.update_configuration({
    "alert_threshold": 100,
    "notification_email": "admin@company.com"
})
```

## Team & Permission Management

### User Management

```python
# Get team information
team = celonis.team.get_team()

# List team members
members = team.get_members()

# Add new member
new_member = team.add_member(
    email="analyst@company.com",
    role="ANALYST"
)
```

### Permission Control

```python
# Check current permissions
permissions = celonis.team.get_permissions()

# Request additional permissions
celonis.team.request_permission(
    service="DATA_INTEGRATION",
    permission="WRITE"
)
```

## Error Handling & Best Practices

### Exception Types

- `PyCelonisError`: Base exception for all PyCelonis errors
- `PyCelonisPermissionError`: Authentication/authorization failures
- `PyCelonisValueError`: Invalid parameter values

### Error Handling Pattern

```python
from pycelonis_core.utils.errors import PyCelonisError

try:
    result = celonis.data_integration.get_data_pool("invalid-id")
except PyCelonisPermissionError:
    print("Insufficient permissions")
except PyCelonisValueError as e:
    print(f"Invalid parameter: {e}")
except PyCelonisError as e:
    print(f"Celonis API error: {e}")
```

### Best Practices

1. **Connection Management**: Reuse Celonis instances when possible
2. **Error Handling**: Always wrap API calls in try-catch blocks
3. **Resource Cleanup**: Properly close connections when done
4. **Rate Limiting**: Implement delays between bulk operations
5. **Logging**: Enable debug logging for troubleshooting

## Advanced Configuration

### Proxy Support

```python
# HTTP proxy configuration
celonis = get_celonis(
    proxy="http://proxy.company.com:8080"
)

# SOCKS proxy
celonis = get_celonis(
    proxy="socks5://proxy.company.com:1080"
)
```

### SSL Configuration

```python
import ssl

# Custom SSL context
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False

celonis = get_celonis(
    verify_ssl=ssl_context
)
```

### Retry Configuration

```python
# Configure retry behavior
celonis = get_celonis(
    retries=3,  # Number of retries
    delay=2     # Delay between retries in seconds
)
```

## LLM Integration Features

*Note: This section documents planned or custom modifications for enhanced LLM integration. The current base PyCelonis package does not include native LLM support.*

### Enhanced Query Generation

The modified package includes capabilities for:
- **Natural Language to PQL**: Convert plain English descriptions to PQL queries
- **Query Optimization**: LLM-powered query performance suggestions
- **Automated Analysis**: Generate complete analysis workflows from requirements

### Intelligent Data Discovery

- **Schema Understanding**: LLM analysis of data model structures
- **Relationship Inference**: Automatic discovery of process relationships
- **Anomaly Detection**: ML-powered identification of process deviations

### Automated Reporting

- **Insight Generation**: LLM-created summaries of process findings
- **Visualization Suggestions**: Recommended chart types and layouts
- **Narrative Reports**: Natural language explanations of process metrics

### Code Generation

- **Pipeline Creation**: Automated generation of data processing pipelines
- **Custom Function Development**: LLM-assisted creation of analysis functions
- **Integration Scripts**: Generated code for third-party system connections

## API Reference

### Main Classes

#### `get_celonis()`
Creates and returns a Celonis client instance.

**Parameters**:
- `base_url` (str, optional): Celonis tenant URL
- `api_token` (str, optional): API authentication token
- `key_type` (str, optional): "APP_KEY" or "USER_KEY"
- `user_agent` (str, optional): Custom user agent string
- `proxies` (dict, optional): Proxy configuration
- `connect` (bool): Test connection on initialization (default: True)
- `permissions` (bool): Display permission info (default: True)
- `check_if_outdated` (bool): Check for package updates (default: True)
- `retries` (int): Number of retry attempts (default: 0)
- `delay` (int): Delay between retries in seconds (default: 1)

**Returns**: `Celonis` instance

#### `Celonis`
Main client class providing access to all services.

**Attributes**:
- `data_integration`: DataIntegration service
- `studio`: Studio service
- `apps`: Apps service
- `team`: Team service

### Data Integration API

#### `DataIntegration.get_data_pools()`
Retrieves all data pools.

**Returns**: List of `DataPool` objects

#### `DataIntegration.create_data_pool(name, description)`
Creates a new data pool.

**Parameters**:
- `name` (str): Pool name
- `description` (str): Pool description

**Returns**: `DataPool` instance

#### `DataPool.create_job(name, description, schedule_type)`
Creates a data extraction job.

**Parameters**:
- `name` (str): Job name
- `description` (str): Job description
- `schedule_type` (str): "ON_DEMAND" or "SCHEDULED"

**Returns**: `Job` instance

### PQL API

#### `PQL(data_model)`
Creates a PQL query builder.

**Parameters**:
- `data_model` (DataModel): Target data model

#### `PQL.query(sql)`
Defines the SELECT portion of a PQL query.

**Parameters**:
- `sql` (str): PQL SELECT statement

**Returns**: Query builder for chaining

#### `QueryBuilder.filter(condition)`
Adds WHERE clause conditions.

#### `QueryBuilder.groupby(*columns)`
Adds GROUP BY clause.

#### `QueryBuilder.orderby(column, ascending=True)`
Adds ORDER BY clause.

#### `QueryBuilder.execute()`
Executes the query and returns results as DataFrame.

## Troubleshooting

### Common Issues

1. **Connection Failures**:
   - Verify API token validity
   - Check network connectivity and proxy settings
   - Ensure correct tenant URL format

2. **Permission Errors**:
   - Confirm appropriate key type (APP_KEY vs USER_KEY)
   - Verify token has required permissions
   - Check team membership and roles

3. **Query Errors**:
   - Validate PQL syntax
   - Ensure data model accessibility
   - Check column names and data types

4. **Performance Issues**:
   - Implement query optimization
   - Use appropriate indexing
   - Consider data model partitioning

### Debug Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("pycelonis")
```

### Support Resources

- **Documentation**: https://celonis.github.io/pycelonis/
- **API Reference**: https://celonis.github.io/pycelonis/api/
- **Community Forum**: Celonis Community
- **Support Portal**: Celonis Customer Support

## Contributing

For modifications and extensions:

1. Fork the repository
2. Create feature branch
3. Implement changes with comprehensive tests
4. Submit pull request with detailed description

## Changelog

### Version 2.20.1
- Enhanced PQL query performance
- Improved error handling and logging
- Added support for advanced authentication methods
- Updated dependencies for better compatibility

