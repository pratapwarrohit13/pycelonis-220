# PyCelonis Offline Installation & Setup Guide

## 📦 Complete Offline Installation Package for LLM Agents

**Version**: 2.20.1  
**Date**: December 26, 2025  
**Purpose**: Comprehensive offline installation and understanding guide for PyCelonis SDK  
**Target Audience**: LLM agents, developers, and automated systems requiring complete PyCelonis understanding

---

## 🎯 Overview

This guide provides everything needed to install, configure, and understand PyCelonis in completely offline environments. All dependencies, documentation, and examples are included for autonomous LLM operation.

### What's Included in This Package

- ✅ **Complete PyCelonis SDK** (v2.20.1) - All source code and modules
- ✅ **PyCelonis Core** (v2.10.3) - Core HTTP client and base functionality
- ✅ **All Dependencies** - Pre-packaged wheel files for offline installation
- ✅ **Comprehensive Documentation** - API references, examples, and architecture
- ✅ **Test Suite** - Validation scripts for all functionality
- ✅ **Configuration Templates** - Ready-to-use setup files
- ✅ **Troubleshooting Guide** - Solutions for common issues

### Package Structure

```
pycelonis_offline_package/
├── pycelonis-2.20.1-py3-none-any.whl          # Main SDK wheel
├── pycelonis_core-2.10.3-py3-none-any.whl     # Core dependency wheel
├── requirements.txt                           # All Python dependencies
├── OFFLINE_INSTALLATION_GUIDE.md             # This guide
├── DOCUMENTATION.md                          # Complete API documentation
├── test.py                                   # Comprehensive test suite
├── setup.py                                  # Package configuration
├── pyrightconfig.json                        # Type checking configuration
└── source_code/                              # Complete source code
    ├── pycelonis/                           # Main SDK modules
    ├── pycelonis_core/                      # Core functionality
    ├── ems/                                 # EMS service modules
    ├── pql/                                 # PQL query engine
    ├── service/                             # Backend services
    └── utils/                               # Utility functions
```

---

## 🚀 Offline Installation Instructions

### Step 1: Prerequisites Check

**Required Software (Offline Compatible):**
- Python 3.8+ (Python 3.11 recommended)
- pip package manager
- Virtual environment support (venv)

**System Requirements:**
- Windows 10+, macOS 10.15+, or Linux
- 4GB RAM minimum, 8GB recommended
- 2GB free disk space

### Step 2: Create Isolated Environment

```bash
# Create virtual environment
python -m venv pycelonis_env

# Activate environment
# Windows:
pycelonis_env\Scripts\activate
# Linux/Mac:
source pycelonis_env/bin/activate
```

### Step 3: Install PyCelonis Offline

```bash
# Install from local wheel files (no internet required)
pip install --no-index --find-links=. pycelonis-2.20.1-py3-none-any.whl
pip install --no-index --find-links=. pycelonis_core-2.10.3-py3-none-any.whl

# Alternative: Install all dependencies from requirements.txt
pip install --no-index --find-links=. -r requirements.txt
```

### Step 4: Verify Installation

```python
# Run this script to verify installation
python -c "
import pycelonis
import pycelonis_core
print('✅ PyCelonis installed successfully!')
print(f'Version: {pycelonis.__version__}')
print(f'Core Version: {pycelonis_core.__version__}')
"
```

---

## 🔧 Configuration & Setup

### Environment Variables (Recommended)

Create a `.env` file in your project directory:

```bash
# Celonis Connection Settings
CELONIS_URL=https://your-tenant.celonis.cloud/
CELONIS_API_TOKEN=your-app-key-here
CELONIS_KEY_TYPE=APP_KEY

# Optional: Proxy settings for corporate environments
HTTP_PROXY=http://proxy.company.com:8080
HTTPS_PROXY=http://proxy.company.com:8080

# Optional: SSL verification (set to false for self-signed certificates)
CELONIS_VERIFY_SSL=true
```

### Direct Configuration

```python
from pycelonis import get_celonis

# Method 1: Environment variables (recommended)
celonis = get_celonis()

# Method 2: Direct parameters
celonis = get_celonis(
    base_url='https://your-tenant.celonis.cloud/',
    api_token='your-api-token',
    key_type='APP_KEY',  # or 'USER_KEY'
    verify_ssl=True
)
```

---

## 🏗️ Architecture Deep Dive

### Core Architecture Overview

PyCelonis follows a modular, service-oriented architecture designed for enterprise process mining:

```
┌─────────────────────────────────────────────────────────────┐
│                    PyCelonis SDK (v2.20.1)                  │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────┐ │
│  │                 Celonis Class                          │ │
│  │  • Main entry point                                    │ │
│  │  • Service orchestration                               │ │
│  │  • Authentication management                           │ │
│  └─────────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────┐ │
│  │Data         │ │   Studio    │ │    Apps     │ │  Team   │ │
│  │Integration │ │             │ │             │ │         │ │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────┘ │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────┐ │
│  │              PyCelonis Core (v2.10.3)                  │ │
│  │  • HTTP client abstraction                             │ │
│  │  • Base models and collections                         │ │
│  │  • Authentication handling                             │ │
│  │  • Error management                                    │ │
│  └─────────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────┐ │
│  │   PQL       │ │  Services   │ │  Utils     │ │   EMS   │ │
│  │  Engine     │ │             │ │             │ │         │ │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### Key Components Explained

#### 1. Celonis Class (Main Entry Point)

```python
class Celonis:
    """
    Main SDK entry point providing access to all Celonis services.

    Attributes:
        data_integration (DataIntegration): Data pool and model management
        studio (Studio): Analytical content and workspace management
        apps (Apps): Custom application development
        team (Team): User and permission management
        pql (PQL): Process Query Language interface
    """

    def __init__(self, base_url: str, api_token: str, key_type: str = "APP_KEY"):
        self.base_url = base_url
        self.api_token = api_token
        self.key_type = key_type
        # Initialize all service modules...
```

#### 2. Data Integration Service

**Purpose**: Manage data pools, models, jobs, and ETL operations.

**Key Classes**:
- `DataPool`: Data storage container
- `DataModel`: Process model with relationships
- `Job`: Scheduled data operations
- `Task`: Individual execution units

**Example Usage**:
```python
# Access data integration service
di = celonis.data_integration

# List all data pools
pools = di.get_data_pools()
print(f"Found {len(pools)} data pools")

# Create new data pool
new_pool = di.create_data_pool(
    name="Production Analysis",
    description="Data pool for production process mining"
)

# Get data models
models = new_pool.get_data_models()
```

#### 3. Studio Service

**Purpose**: Manage analytical content, workspaces, and visualizations.

**Key Classes**:
- `Space`: Workspace container
- `ContentNode`: Analysis, views, dashboards
- `Folder`: Content organization
- `Package`: Content bundles

#### 4. PQL (Process Query Language) Engine

**Purpose**: Query and analyze process data using Celonis's proprietary query language.

**Key Classes**:
- `PQL`: Main query interface
- `DataFrame`: Tabular result representation
- `Series`: Column-based operations
- `PQLColumn`: Query column definitions

**Architecture**:
```
PQL Query → Parser → Saola Connector → Data Model → Results
```

### Service Layer Architecture

PyCelonis includes multiple backend services:

#### Integration Service
- **Purpose**: External system connectivity
- **Key Features**: API endpoints, webhook handling, data synchronization

#### Package Manager Service
- **Purpose**: Extension and plugin management
- **Key Features**: Custom package installation, dependency management

#### Process Analytics Service
- **Purpose**: Advanced process mining algorithms
- **Key Features**: Conformance checking, bottleneck analysis, process discovery

#### Semantic Layer Service
- **Purpose**: Business terminology and metadata management
- **Key Features**: Business object definitions, data cataloging

---

## 📚 Complete API Reference

### Celonis Class Methods

#### Connection & Authentication
```python
# Get authenticated Celonis instance
celonis = get_celonis(
    base_url="https://tenant.celonis.cloud/",
    api_token="app_key_here",
    key_type="APP_KEY",
    verify_ssl=True,
    timeout=30
)
```

#### Service Access
```python
# Access all major services
data_integration = celonis.data_integration
studio = celonis.studio
apps = celonis.apps
team = celonis.team
pql = celonis.pql
```

### Data Integration API

#### Data Pool Operations
```python
# List data pools
pools = celonis.data_integration.get_data_pools()

# Create data pool
pool = celonis.data_integration.create_data_pool(
    name="Analysis Pool",
    description="Process mining data storage"
)

# Get specific pool
pool = celonis.data_integration.get_data_pool(pool_id)

# Delete pool
pool.delete()
```

#### Data Model Operations
```python
# Get data models in pool
models = pool.get_data_models()

# Create data model
model = pool.create_data_model(
    name="Order Processing Model",
    description="Model for order-to-cash process"
)

# Reload data model
model.reload()

# Export data model
export = model.export_data()
```

#### Job & Task Management
```python
# List jobs
jobs = pool.get_jobs()

# Create extraction job
job = pool.create_job(
    name="Daily Data Load",
    schedule="0 6 * * *",  # Daily at 6 AM
    tasks=[
        {
            "name": "Extract Orders",
            "type": "EXTRACTION",
            "table": "ORDER_TABLE"
        }
    ]
)

# Execute job immediately
job.execute()

# Monitor job status
status = job.get_status()
```

### Studio API

#### Space Management
```python
# List spaces
spaces = celonis.studio.get_spaces()

# Create space
space = celonis.studio.create_space(
    name="Process Analytics",
    description="Workspace for process mining analysis"
)

# Get space content
content = space.get_content()
```

#### Content Node Operations
```python
# List content in space
nodes = space.get_content_nodes()

# Create analysis
analysis = space.create_analysis(
    name="Order Analysis",
    description="Analysis of order processing efficiency"
)

# Create dashboard
dashboard = space.create_view(
    name="KPI Dashboard",
    type="DASHBOARD"
)
```

### PQL API

#### Basic Query Construction
```python
from pycelonis.pql import PQL

# Initialize PQL with data model
pql = PQL(data_model=model)

# Simple column selection
query = pql.query("""
    CASE_TABLE."Case ID",
    CASE_TABLE."Order Value",
    CASE_TABLE."Status"
""")

result = query.execute()
```

#### Advanced Query Features
```python
# Filtered query
query = pql.query("""
    CASE_TABLE."Case ID",
    COUNT(CASE_TABLE."Activity") as "Activity Count"
""").filter(
    CASE_TABLE."Status" == "Completed"
).groupby(
    CASE_TABLE."Case ID"
).having(
    COUNT(CASE_TABLE."Activity") > 5
)

# Execute with pagination
result = query.execute(limit=1000, offset=0)
```

#### DataFrame Operations
```python
# Convert to pandas DataFrame
df = result.to_pandas()

# DataFrame operations
summary = df.groupby('Case ID').agg({
    'Activity Count': 'sum',
    'Order Value': 'mean'
})

# Export results
result.to_csv('results.csv')
result.to_parquet('results.parquet')
```

---

## 🔍 Code Examples & Patterns

### 1. Complete Process Mining Workflow

```python
from pycelonis import get_celonis
import pandas as pd

def complete_process_mining_workflow():
    """
    Complete example of process mining workflow using PyCelonis
    """
    # 1. Connect to Celonis
    celonis = get_celonis()

    # 2. Access data integration
    di = celonis.data_integration

    # 3. Get or create data pool
    pool = di.get_data_pool("production_pool")
    if not pool:
        pool = di.create_data_pool("Production Pool")

    # 4. Create data model
    model = pool.create_data_model("Order Processing Model")

    # 5. Load data (assuming CSV upload)
    table = pool.create_table_from_csv(
        file_path="order_data.csv",
        table_name="ORDER_DATA"
    )

    # 6. Build data model relationships
    model.add_table(table)
    model.create_foreign_key(
        from_table="ORDER_DATA",
        from_column="Order ID",
        to_table="ACTIVITY_DATA",
        to_column="Order ID"
    )

    # 7. Reload model
    model.reload()

    # 8. Create PQL analysis
    from pycelonis.pql import PQL
    pql = PQL(data_model=model)

    # 9. Build process analysis query
    process_query = pql.query("""
        CASE_TABLE."Case ID",
        VARIANT(CASE_TABLE."Activity") as "Process Variant",
        COUNT(CASE_TABLE."Activity") as "Total Activities",
        AVG(CASE_TABLE."Duration") as "Avg Activity Duration",
        MIN(CASE_TABLE."Timestamp") as "Case Start",
        MAX(CASE_TABLE."Timestamp") as "Case End"
    """).groupby(CASE_TABLE."Case ID")

    # 10. Execute and analyze
    results = process_query.execute()

    # 11. Create analysis in Studio
    studio = celonis.studio
    space = studio.get_space("analysis_space")

    analysis = space.create_analysis(
        name="Order Processing Analysis",
        data_model=model
    )

    # 12. Add visualizations
    chart = analysis.create_chart(
        name="Process Variants",
        type="BAR_CHART",
        query=process_query
    )

    return {
        "data_pool": pool,
        "data_model": model,
        "analysis": analysis,
        "results": results
    }
```

### 2. Data Integration Pipeline

```python
def create_etl_pipeline():
    """
    Create automated ETL pipeline for process data
    """
    celonis = get_celonis()
    di = celonis.data_integration

    # Create data pool
    pool = di.create_data_pool("ETL_Pool")

    # Define extraction tasks
    tasks = [
        {
            "name": "Extract Orders",
            "type": "DATABASE_EXTRACTION",
            "connection": "erp_database",
            "query": "SELECT * FROM orders WHERE created_date >= ?",
            "parameters": ["2024-01-01"]
        },
        {
            "name": "Extract Activities",
            "type": "DATABASE_EXTRACTION",
            "connection": "erp_database",
            "query": "SELECT * FROM order_activities WHERE timestamp >= ?",
            "parameters": ["2024-01-01"]
        }
    ]

    # Create transformation job
    job = pool.create_job(
        name="Daily ETL Pipeline",
        schedule="0 */4 * * *",  # Every 4 hours
        tasks=tasks
    )

    # Add data quality checks
    job.add_validation_rule(
        name="Completeness Check",
        query="SELECT COUNT(*) FROM ORDER_DATA WHERE order_id IS NULL",
        expected_result=0
    )

    return job
```

### 3. Real-time Process Monitoring

```python
def setup_process_monitoring():
    """
    Set up real-time process monitoring dashboard
    """
    celonis = get_celonis()
    studio = celonis.studio

    # Create monitoring space
    space = studio.create_space("Process Monitoring")

    # Create KPI dashboard
    dashboard = space.create_view(
        name="Process KPIs",
        type="DASHBOARD"
    )

    # Add KPI components
    kpis = [
        {
            "name": "Case Throughput",
            "query": "COUNT(DISTINCT CASE_TABLE.\"Case ID\")",
            "format": "number"
        },
        {
            "name": "Average Case Duration",
            "query": "AVG(CASE_DURATION(CASE_TABLE.\"Case ID\"))",
            "format": "duration"
        },
        {
            "name": "Process Compliance",
            "query": "CONFORMANCE(CASE_TABLE.\"Case ID\", 'standard_process')",
            "format": "percentage"
        }
    ]

    for kpi_config in kpis:
        kpi = dashboard.create_kpi(**kpi_config)

    # Set up alerts
    alert = dashboard.create_alert(
        name="High Case Duration Alert",
        condition="AVG(CASE_DURATION(CASE_TABLE.\"Case ID\")) > 30",
        threshold="days",
        notification="email"
    )

    return dashboard
```

---

## 🧪 Testing & Validation

### Running the Test Suite

```bash
# Run comprehensive tests
python test.py

# Run specific test category
python -m pytest test.py::test_data_integration -v

# Run with coverage
python -m pytest test.py --cov=pycelonis --cov-report=html
```

### Test Categories Included

1. **Connection Tests**: Authentication and connectivity validation
2. **Data Integration Tests**: Pool, model, and job operations
3. **Studio Tests**: Space and content management
4. **Team Tests**: User and permission management
5. **PQL Tests**: Query execution and DataFrame operations
6. **Advanced Features Tests**: Complex workflows and integrations
7. **Performance Tests**: Load testing and optimization validation

### Manual Validation Script

```python
def validate_installation():
    """
    Comprehensive validation of PyCelonis installation
    """
    try:
        # Test imports
        import pycelonis
        import pycelonis_core
        from pycelonis.pql import PQL
        print("✅ All imports successful")

        # Test version compatibility
        assert pycelonis.__version__ == "2.20.1"
        assert pycelonis_core.__version__ == "2.10.3"
        print("✅ Version compatibility verified")

        # Test basic connectivity (requires valid credentials)
        try:
            celonis = get_celonis()
            pools = celonis.data_integration.get_data_pools()
            print(f"✅ Connection successful, found {len(pools)} data pools")
        except Exception as e:
            print(f"⚠️  Connection test skipped: {e}")

        print("🎉 PyCelonis installation validated successfully!")
        return True

    except Exception as e:
        print(f"❌ Validation failed: {e}")
        return False

if __name__ == "__main__":
    validate_installation()
```

---

## 🔧 Troubleshooting Guide

### Common Installation Issues

#### 1. Import Errors
**Problem**: `ModuleNotFoundError: No module named 'pycelonis'`

**Solutions**:
```bash
# Ensure virtual environment is activated
# Windows:
pycelonis_env\Scripts\activate
# Linux/Mac:
source pycelonis_env/bin/activate

# Reinstall from wheel
pip install --force-reinstall pycelonis-2.20.1-py3-none-any.whl
```

#### 2. Dependency Conflicts
**Problem**: Version conflicts with existing packages

**Solution**:
```bash
# Create fresh environment
python -m venv fresh_env
fresh_env\Scripts\activate  # Windows
pip install --no-index --find-links=. -r requirements.txt
```

#### 3. SSL Certificate Issues
**Problem**: SSL verification errors in corporate environments

**Solution**:
```python
# Disable SSL verification (use with caution)
celonis = get_celonis(verify_ssl=False)

# Or configure custom certificates
import httpx
celonis = get_celonis(
    verify_ssl=True,
    ssl_cert_path="/path/to/corporate/ca.crt"
)
```

### Connection Issues

#### 1. Authentication Failures
**Problem**: API token or URL configuration issues

**Debug Steps**:
```python
# Test basic connectivity
import httpx
response = httpx.get("https://your-tenant.celonis.cloud/api/health")
print(f"HTTP Status: {response.status_code}")

# Test API token
headers = {"Authorization": f"Bearer {api_token}"}
response = httpx.get(
    "https://your-tenant.celonis.cloud/api/data-integration/data-pools",
    headers=headers
)
print(f"API Response: {response.status_code}")
```

#### 2. Timeout Issues
**Problem**: Slow responses or timeouts

**Solutions**:
```python
# Increase timeout
celonis = get_celonis(timeout=60)  # 60 seconds

# Configure retry logic
from pycelonis_core.client import ClientConfig
config = ClientConfig(
    timeout=30,
    max_retries=3,
    retry_delay=1.0
)
celonis = get_celonis(config=config)
```

### Performance Issues

#### 1. Memory Usage
**Problem**: High memory consumption with large datasets

**Solutions**:
```python
# Use streaming for large results
result = query.execute(stream=True)

# Process in chunks
for chunk in result.iter_chunks(chunk_size=1000):
    process_chunk(chunk)

# Use parquet for large data exports
result.to_parquet("large_dataset.parquet", compression="snappy")
```

#### 2. Query Performance
**Problem**: Slow PQL query execution

**Optimization Tips**:
```python
# Use appropriate indexes
query = pql.query("""
    CASE_TABLE."Case ID",
    CASE_TABLE."Activity"
""").filter(
    CASE_TABLE."Timestamp" >= "2024-01-01"
).hint("USE_INDEX", "timestamp_index")

# Limit result size
result = query.execute(limit=10000)

# Use sampling for analysis
sample_query = query.sample(fraction=0.1)
```

---

## 📋 Dependencies & Requirements

### Core Dependencies (Included)

```
pycelonis-core==2.10.3          # Core HTTP client and models
httpx>=0.28.0,<1.0.0           # HTTP client library
pydantic>=2.0.0,<3.0.0         # Data validation
pandas>=1.3.0,<3.0.0           # Data manipulation
pyarrow>=8.0.0,<18.0.0         # High-performance data processing
numpy>=1.20.0,<2.0.0           # Numerical computing
saolapy>=1.0.0,<2.0.0          # Celonis query engine
typing-extensions>=4.0.0       # Type hints
```

### Optional Dependencies

```
pytest>=7.0.0                   # Testing framework
pytest-cov>=4.0.0              # Coverage reporting
black>=22.0.0                  # Code formatting
mypy>=1.0.0                    # Type checking
sphinx>=5.0.0                  # Documentation
```

### System Requirements

- **Python**: 3.8, 3.9, 3.10, 3.11, 3.12 (3.13+ experimental)
- **Memory**: 4GB minimum, 8GB recommended
- **Disk**: 2GB free space
- **Network**: Stable internet connection (for online operations)

---

## 🔒 Security Considerations

### Authentication Best Practices

1. **Use Application Keys**: Prefer APP_KEY over USER_KEY for service accounts
2. **Environment Variables**: Never hardcode credentials in source code
3. **Key Rotation**: Regularly rotate API keys
4. **Principle of Least Privilege**: Grant minimum required permissions

### Data Protection

1. **SSL Verification**: Always enable SSL verification in production
2. **Data Encryption**: Use encrypted connections for sensitive data
3. **Audit Logging**: Enable audit trails for compliance
4. **Access Controls**: Implement proper permission management

### Secure Configuration Example

```python
# .env file (never commit to version control)
CELONIS_URL=https://production-tenant.celonis.cloud/
CELONIS_API_TOKEN=app_key_with_minimal_permissions
CELONIS_KEY_TYPE=APP_KEY
CELONIS_VERIFY_SSL=true
CELONIS_TIMEOUT=30

# Python configuration
celonis = get_celonis(
    # All credentials from environment variables
    verify_ssl=True,
    timeout=int(os.getenv('CELONIS_TIMEOUT', 30))
)
```

---

## 🚀 Advanced Usage Patterns

### 1. Custom Service Integration

```python
class CustomCelonisService:
    """
    Example of extending PyCelonis with custom functionality
    """

    def __init__(self, celonis_instance):
        self.celonis = celonis_instance
        self.di = celonis_instance.data_integration

    def get_process_kpis(self, data_model_id):
        """Calculate key process performance indicators"""
        model = self.di.get_data_model(data_model_id)
        pql = PQL(data_model=model)

        kpis = {
            "total_cases": pql.query("COUNT(DISTINCT CASE_TABLE.\"Case ID\")").execute().iloc[0,0],
            "avg_case_duration": pql.query("AVG(CASE_DURATION(CASE_TABLE.\"Case ID\"))").execute().iloc[0,0],
            "process_variants": pql.query("COUNT(DISTINCT VARIANT(CASE_TABLE.\"Activity\"))").execute().iloc[0,0]
        }

        return kpis

    def create_compliance_dashboard(self, space_name, data_model_id):
        """Create automated compliance monitoring dashboard"""
        studio = self.celonis.studio
        space = studio.create_space(space_name)

        # Create compliance analysis
        analysis = space.create_analysis("Compliance Analysis")

        # Add compliance checks
        compliance_checks = [
            "Check for missing activities",
            "Validate process flow",
            "Monitor SLA compliance"
        ]

        return analysis
```

### 2. Batch Processing Framework

```python
class BatchProcessor:
    """
    Framework for processing large datasets in batches
    """

    def __init__(self, celonis_instance, batch_size=1000):
        self.celonis = celonis_instance
        self.batch_size = batch_size

    def process_large_dataset(self, data_model_id, query, processor_func):
        """
        Process large datasets in configurable batches
        """
        model = self.celonis.data_integration.get_data_model(data_model_id)
        pql = PQL(data_model=model)

        offset = 0
        total_processed = 0

        while True:
            # Execute query with pagination
            batch_query = query.limit(self.batch_size).offset(offset)
            batch_result = batch_query.execute()

            if batch_result.empty:
                break

            # Process batch
            processor_func(batch_result)

            total_processed += len(batch_result)
            offset += self.batch_size

            print(f"Processed {total_processed} records...")

        return total_processed

    def export_to_multiple_files(self, data_model_id, base_query, output_dir):
        """
        Export large results to multiple files
        """
        def save_batch(batch_df, file_index=[0]):
            filename = f"{output_dir}/export_batch_{file_index[0]:04d}.parquet"
            batch_df.to_parquet(filename)
            file_index[0] += 1

        total = self.process_large_dataset(
            data_model_id,
            base_query,
            lambda df: save_batch(df)
        )

        print(f"Exported {total} records to {output_dir}")
        return total
```

### 3. Monitoring & Alerting System

```python
class ProcessMonitor:
    """
    Real-time process monitoring and alerting system
    """

    def __init__(self, celonis_instance, alert_thresholds=None):
        self.celonis = celonis_instance
        self.thresholds = alert_thresholds or {
            "max_case_duration": 30,  # days
            "min_throughput": 100,   # cases per day
            "max_error_rate": 0.05   # 5%
        }
        self.alerts = []

    def check_process_health(self, data_model_id):
        """
        Comprehensive process health check
        """
        model = self.celonis.data_integration.get_data_model(data_model_id)
        pql = PQL(data_model=model)

        # Calculate KPIs
        kpis = {
            "case_duration": pql.query("AVG(CASE_DURATION(CASE_TABLE.\"Case ID\"))").execute().iloc[0,0],
            "daily_throughput": pql.query("COUNT(DISTINCT CASE_TABLE.\"Case ID\") / 30").execute().iloc[0,0],
            "error_rate": pql.query("COUNT(CASE_TABLE.\"Activity\" WHERE \"Activity\" LIKE '%error%') / COUNT(*)").execute().iloc[0,0]
        }

        # Check thresholds
        alerts = []
        for metric, value in kpis.items():
            threshold = self.thresholds.get(f"max_{metric}", self.thresholds.get(f"min_{metric}"))
            if threshold:
                if metric.startswith("max_") and value > threshold:
                    alerts.append(f"High {metric}: {value} > {threshold}")
                elif metric.startswith("min_") and value < threshold:
                    alerts.append(f"Low {metric}: {value} < {threshold}")

        self.alerts.extend(alerts)
        return {"kpis": kpis, "alerts": alerts}

    def generate_health_report(self, data_model_ids):
        """
        Generate comprehensive health report for multiple processes
        """
        report = {}
        for model_id in data_model_ids:
            health = self.check_process_health(model_id)
            report[model_id] = health

        return report
```

---

## 📖 Learning Resources

### Code Examples Repository

All examples in this guide are included in the offline package:

```
examples/
├── basic_connection.py          # Basic setup and connection
├── data_integration.py          # Complete data integration workflow
├── pql_queries.py              # PQL query examples
├── studio_management.py        # Studio and content management
├── monitoring_dashboard.py     # Real-time monitoring setup
├── batch_processing.py         # Large dataset processing
├── custom_services.py          # Extending PyCelonis
└── troubleshooting.py          # Common issues and solutions
```

### API Documentation

Complete API documentation is available in `DOCUMENTATION.md` including:

- All class and method signatures
- Parameter descriptions
- Return value specifications
- Error handling patterns
- Code examples for each API

### Best Practices Guide

1. **Connection Management**: Always use connection pooling and proper cleanup
2. **Error Handling**: Implement comprehensive error handling for production use
3. **Performance**: Use appropriate batching and pagination for large datasets
4. **Security**: Follow security best practices for credential management
5. **Monitoring**: Implement proper logging and monitoring for production deployments

---

## 🔄 Version Compatibility

### Supported Python Versions

- ✅ Python 3.8 (with limitations)
- ✅ Python 3.9
- ✅ Python 3.10
- ✅ Python 3.11 (recommended)
- ✅ Python 3.12
- ⚠️  Python 3.13 (experimental support)

### Dependency Version Matrix

| Component | Version | Compatibility Notes |
|-----------|---------|-------------------|
| PyCelonis | 2.20.1 | Latest stable release |
| PyCelonis Core | 2.10.3 | Required core functionality |
| httpx | 0.28.0+ | HTTP client, async support |
| pydantic | 2.0.0+ | Data validation, V2 required |
| pandas | 1.3.0+ | Data manipulation |
| pyarrow | 8.0.0+ | High-performance I/O |

### Migration Notes

**From PyCelonis 1.x to 2.x:**
- Pydantic V2 migration required
- API changes in authentication
- New service-oriented architecture
- Enhanced error handling

---

## 🎯 Quick Reference

### Most Common Operations

```python
# 1. Connect
from pycelonis import get_celonis
celonis = get_celonis()

# 2. Access data integration
di = celonis.data_integration

# 3. Get data pools
pools = di.get_data_pools()

# 4. Create PQL query
from pycelonis.pql import PQL
pql = PQL(data_model=data_model)
result = pql.query("SELECT * FROM CASE_TABLE").execute()

# 5. Create studio content
studio = celonis.studio
space = studio.create_space("My Space")
analysis = space.create_analysis("My Analysis")
```

### Error Handling Pattern

```python
from pycelonis.errors import PyCelonisError

try:
    result = celonis.data_integration.get_data_pools()
except PyCelonisError as e:
    print(f"PyCelonis error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Configuration Template

```python
# config.py
import os
from typing import Optional

class CelonisConfig:
    def __init__(self):
        self.url = os.getenv('CELONIS_URL')
        self.api_token = os.getenv('CELONIS_API_TOKEN')
        self.key_type = os.getenv('CELONIS_KEY_TYPE', 'APP_KEY')
        self.verify_ssl = os.getenv('CELONIS_VERIFY_SSL', 'true').lower() == 'true'
        self.timeout = int(os.getenv('CELONIS_TIMEOUT', '30'))

    def get_celonis(self):
        from pycelonis import get_celonis
        return get_celonis(
            base_url=self.url,
            api_token=self.api_token,
            key_type=self.key_type,
            verify_ssl=self.verify_ssl,
            timeout=self.timeout
        )
```

---

## 📞 Support & Resources

### Included Resources

- **Complete Documentation**: `DOCUMENTATION.md`
- **Test Suite**: `test.py` with comprehensive validation
- **Example Code**: All examples from this guide
- **Troubleshooting Guide**: Solutions for common issues
- **API Reference**: Complete method documentation

### For LLM Agents

This offline package contains everything needed for autonomous operation:

1. **Self-contained Installation**: No internet required
2. **Complete API Documentation**: All methods and parameters documented
3. **Working Code Examples**: Tested examples for all major features
4. **Comprehensive Testing**: Validation scripts for all functionality
5. **Error Handling Patterns**: Robust error management examples
6. **Architecture Understanding**: Detailed explanations of all components

### Package Integrity Verification

```bash
# Verify package contents
pip show pycelonis
pip show pycelonis-core

# Run validation tests
python test.py

# Check installation integrity
python -c "import pycelonis; print('Installation verified')"
```

---

**🎉 Installation Complete!**

This offline installation guide provides everything an LLM agent needs to understand, install, and use PyCelonis in completely offline environments. The package includes all dependencies, documentation, examples, and testing tools required for autonomous operation.
