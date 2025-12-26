# PyCelonis Offline Installation Package

## 📦 Complete Offline PyCelonis SDK Package

**Version**: 2.20.1 (PyCelonis) + 2.10.3 (PyCelonis Core)  
**Date**: December 26, 2025  
**Compatibility**: Python 3.8+ (Windows/Linux/macOS)

This package contains everything needed to install and use PyCelonis in completely offline environments. No internet connection required!

## 📁 Package Contents

```
pycelonis_offline_package/
├── pycelonis-2.20.1-py3-none-any.whl          # Main SDK wheel
├── pycelonis_core-2.10.3-py3-none-any.whl     # Core dependency wheel
├── OFFLINE_INSTALLATION_GUIDE.md             # Comprehensive setup guide
├── DOCUMENTATION.md                          # Complete API documentation
├── setup_offline.py                          # Automated installation script
├── validate_installation.py                  # Installation validator
├── test.py                                   # Comprehensive test suite
├── requirements.txt                          # All dependencies
├── setup.py                                  # Package configuration
├── README.md                                 # This file
└── source_code/                              # Complete source code
    ├── pycelonis/                           # Main SDK
    ├── pycelonis_core/                      # Core functionality
    └── [all modules...]                     # Complete codebase
```

## 🚀 Quick Start (Offline Installation)

### Option 1: Automated Setup (Recommended)

```bash
# Run the automated setup script
python setup_offline.py
```

The script will:
- ✅ Check Python version compatibility
- ✅ Create virtual environment
- ✅ Install PyCelonis from wheel files
- ✅ Validate installation
- ✅ Provide usage instructions

### Option 2: Manual Installation

```bash
# 1. Create virtual environment
python -m venv pycelonis_env

# 2. Activate environment
# Windows:
pycelonis_env\Scripts\activate
# Linux/Mac:
source pycelonis_env/bin/activate

# 3. Install from wheel files
pip install --no-index --find-links=. pycelonis-2.20.1-py3-none-any.whl
pip install --no-index --find-links=. pycelonis_core-2.10.3-py3-none-any.whl

# 4. Validate installation
python validate_installation.py
```

## 🔍 Validation

After installation, run the validator:

```bash
python validate_installation.py
```

This will check:
- ✅ All imports work correctly
- ✅ Version compatibility
- ✅ Basic functionality
- ✅ Dependencies availability
- ✅ Network independence

## 📚 Documentation

### For LLM Agents & Developers

1. **OFFLINE_INSTALLATION_GUIDE.md** - Complete setup and usage guide
   - Architecture explanations
   - Code examples for all features
   - Troubleshooting solutions
   - Advanced usage patterns

2. **DOCUMENTATION.md** - Detailed API reference
   - All classes and methods
   - Parameter specifications
   - Error handling patterns

3. **test.py** - Comprehensive test suite
   - 7 test categories covering all functionality
   - Error handling and edge cases
   - Performance validation

## 💡 Usage Examples

### Basic Connection

```python
from pycelonis import get_celonis

# Configure environment variables or pass directly
celonis = get_celonis(
    base_url="https://your-tenant.celonis.cloud/",
    api_token="your-api-token",
    key_type="APP_KEY"
)

# Access services
data_pools = celonis.data_integration.get_data_pools()
print(f"Found {len(data_pools)} data pools")
```

### PQL Query

```python
from pycelonis.pql import PQL

# Get data model
data_model = celonis.data_integration.get_data_model("your-model-id")

# Create query
pql = PQL(data_model=data_model)
result = pql.query("""
    CASE_TABLE."Case ID",
    COUNT(CASE_TABLE."Activity") as "Activities"
""").groupby(CASE_TABLE."Case ID").execute()

print(result.head())
```

## 🔧 Key Features

- **🔗 Complete SDK**: All PyCelonis functionality included
- **📊 Data Integration**: Pools, models, jobs, ETL operations
- **🎨 Studio**: Analytical content and workspace management
- **🔍 PQL Engine**: Process Query Language for data analysis
- **👥 Team Management**: User and permission handling
- **🔧 Backend Services**: Integration, package management, analytics
- **📈 Real-time Monitoring**: Process KPIs and alerting

## 🛠️ System Requirements

- **Python**: 3.8, 3.9, 3.10, 3.11, 3.12 (3.13 experimental)
- **Memory**: 4GB minimum, 8GB recommended
- **Disk**: 2GB free space
- **Network**: None required for installation and basic usage

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   # Ensure virtual environment is activated
   # Reinstall if needed
   pip install --force-reinstall pycelonis-2.20.1-py3-none-any.whl
   ```

2. **Validation Failures**
   ```bash
   # Run detailed validation
   python validate_installation.py
   ```

3. **Permission Issues**
   ```bash
   # Run as administrator or use user installation
   pip install --user pycelonis-2.20.1-py3-none-any.whl
   ```

## 📞 Support

This offline package is self-contained and includes:

- ✅ Complete installation instructions
- ✅ Comprehensive documentation
- ✅ Working code examples
- ✅ Test suite for validation
- ✅ Troubleshooting guides
- ✅ All dependencies included

For additional support, refer to the included documentation files.

---

**🎯 Ready for Offline Use!**

This package provides everything needed for autonomous PyCelonis operation without internet access. Perfect for air-gapped environments, secure installations, and LLM agent usage.

## Installation

### From Source
```bash
# Install PyCelonis Core first
cd pycelonis_core
pip install -e .

# Install PyCelonis
cd ../pycelonis\ 2.20.1
pip install -e .
```

### Using Requirements
```bash
pip install -r requirements.txt
```

## Key Features

### 🔗 Core Functionality
- **Secure Authentication**: APP_KEY and USER_KEY support
- **Flexible Configuration**: Environment variables and direct parameters
- **Connection Management**: Automatic retries and SSL verification
- **Version Checking**: Automatic update notifications

### 📊 Data Integration
- **Data Pools**: Storage container management
- **Data Models**: Process model creation and management
- **Jobs & Tasks**: ETL job scheduling and execution
- **Table Operations**: Data manipulation and querying

### 🎨 Studio & Apps
- **Space Management**: Analytical workspace organization
- **Content Nodes**: Analysis and dashboard management
- **Application Development**: Custom app deployment

### 🔍 Process Query Language (PQL)
- **DataFrame API**: Pandas-like data manipulation
- **Query Building**: Programmatic PQL construction
- **Series Operations**: Column-based data processing

### 👥 Team & Permissions
- **User Management**: Team member administration
- **Permission Control**: Granular access management
- **Audit Trails**: Activity tracking

## API Structure

### Main Entry Point
```python
from pycelonis import get_celonis

celonis = get_celonis(
    base_url="https://your-tenant.celonis.cloud/",
    api_token="your-api-token",
    key_type="APP_KEY"
)
```

### Core Services
- `celonis.data_integration`: Data pool and model management
- `celonis.studio`: Analysis space and content management
- `celonis.apps`: Application deployment and management
- `celonis.team`: User and permission management

## Development Notes

### Dependencies
- **Python**: 3.8+ (tested with 3.13.7)
- **httpx**: >=0.28.0 for HTTP communication
- **pydantic**: >=2.0.0 for data validation
- **pandas**: Data manipulation
- **pyarrow**: High-performance data processing

### Build Information
- Built with setuptools
- Includes wheel distribution
- Compatible with pip installation

## Version History

### PyCelonis 2.20.1
- Enhanced PQL query performance
- Improved error handling
- Updated authentication methods
- Better compatibility with Python 3.13+

### PyCelonis Core 2.10.3
- Latest stable core functionality
- Improved HTTP client handling
- Enhanced error reporting
- ML Workbench integration updates

## Support

For issues or questions:
- Check the main PyCelonis documentation
- Review Celonis Community forums
- Contact Celonis support for enterprise issues

## License

This software is proprietary to Celonis SE. See individual package licenses for details.