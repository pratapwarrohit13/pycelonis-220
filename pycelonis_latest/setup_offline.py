#!/usr/bin/env python3
"""
PyCelonis Offline Setup Script
==============================

This script automates the offline installation of PyCelonis and its dependencies.

Usage:
    python setup_offline.py

Requirements:
    - Python 3.8+
    - Wheel files in the same directory
    - No internet connection required

The script will:
    1. Create/check virtual environment
    2. Install PyCelonis from wheel files
    3. Validate the installation
    4. Provide usage instructions
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def print_header():
    """Print setup header"""
    print("=" * 60)
    print("🚀 PyCelonis Offline Setup Script")
    print("=" * 60)
    print("This script will install PyCelonis in offline mode.")
    print("Make sure you have the wheel files in the current directory.")
    print("-" * 60)

def check_python_version():
    """Check Python version compatibility"""
    print("🐍 Checking Python version...")

    version = sys.version_info
    if version < (3, 8):
        print(f"❌ Python {version.major}.{version.minor} is not supported.")
        print("   Please use Python 3.8 or higher.")
        return False
    elif version >= (3, 13):
        print(f"⚠️  Python {version.major}.{version.minor} - experimental support")
    else:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - compatible")

    return True

def check_wheel_files():
    """Check for required wheel files"""
    print("\n📦 Checking for wheel files...")

    required_files = [
        "pycelonis-2.20.1-py3-none-any.whl",
        "pycelonis_core-2.10.3-py3-none-any.whl"
    ]

    missing_files = []
    for filename in required_files:
        if os.path.exists(filename):
            print(f"  ✅ {filename}")
        else:
            print(f"  ❌ {filename} (missing)")
            missing_files.append(filename)

    if missing_files:
        print(f"\n❌ Missing required files: {', '.join(missing_files)}")
        print("   Please ensure all wheel files are in the current directory.")
        return False

    return True

def create_virtual_environment():
    """Create virtual environment if it doesn't exist"""
    print("\n🏠 Setting up virtual environment...")

    venv_path = Path("pycelonis_env")

    if venv_path.exists():
        print("  ℹ️  Virtual environment already exists")
        return True

    try:
        print("  📁 Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", "pycelonis_env"],
                      check=True, capture_output=True)

        print("  ✅ Virtual environment created successfully")
        return True

    except subprocess.CalledProcessError as e:
        print(f"  ❌ Failed to create virtual environment: {e}")
        return False

def activate_and_install():
    """Activate virtual environment and install packages"""
    print("\n⚙️  Installing PyCelonis...")

    # Determine activation script path
    if platform.system() == "Windows":
        activate_script = "pycelonis_env\\Scripts\\activate"
        pip_cmd = "pycelonis_env\\Scripts\\pip.exe"
    else:
        activate_script = "pycelonis_env/bin/activate"
        pip_cmd = "pycelonis_env/bin/pip"

    if not os.path.exists(pip_cmd):
        print(f"  ❌ Pip not found at {pip_cmd}")
        print("   Virtual environment may not have been created properly.")
        return False

    try:
        # Install packages using pip
        print("  📦 Installing pycelonis-core...")
        subprocess.run([
            pip_cmd, "install", "--no-index", "--find-links=.",
            "pycelonis_core-2.10.3-py3-none-any.whl"
        ], check=True, capture_output=True)

        print("  📦 Installing pycelonis...")
        subprocess.run([
            pip_cmd, "install", "--no-index", "--find-links=.",
            "pycelonis-2.20.1-py3-none-any.whl"
        ], check=True, capture_output=True)

        print("  ✅ PyCelonis installed successfully")
        return True

    except subprocess.CalledProcessError as e:
        print(f"  ❌ Installation failed: {e}")
        print(f"   Error output: {e.stderr.decode() if e.stderr else 'None'}")
        return False

def run_validation():
    """Run the validation script"""
    print("\n🔍 Running installation validation...")

    # Determine python executable path
    if platform.system() == "Windows":
        python_cmd = "pycelonis_env\\Scripts\\python.exe"
    else:
        python_cmd = "pycelonis_env/bin/python"

    if not os.path.exists(python_cmd):
        print(f"  ❌ Python executable not found at {python_cmd}")
        return False

    try:
        # Run validation script
        result = subprocess.run([
            python_cmd, "validate_installation.py"
        ], capture_output=True, text=True)

        # Print validation output
        print(result.stdout)

        if result.returncode == 0:
            print("  ✅ Validation completed successfully")
            return True
        else:
            print("  ❌ Validation failed")
            if result.stderr:
                print(f"   Error: {result.stderr}")
            return False

    except Exception as e:
        print(f"  ❌ Validation script failed to run: {e}")
        return False

def print_usage_instructions():
    """Print usage instructions"""
    print("\n" + "=" * 60)
    print("🎉 INSTALLATION COMPLETE!")
    print("=" * 60)
    print("\n📚 Usage Instructions:")
    print("1. Activate the virtual environment:")
    if platform.system() == "Windows":
        print("   pycelonis_env\\Scripts\\activate")
    else:
        print("   source pycelonis_env/bin/activate")

    print("\n2. Start using PyCelonis in your Python scripts:")
    print("   from pycelonis import get_celonis")
    print("   celonis = get_celonis()")

    print("\n3. For detailed usage examples, see:")
    print("   - OFFLINE_INSTALLATION_GUIDE.md")
    print("   - DOCUMENTATION.md")

    print("\n4. Run the test suite to verify functionality:")
    print("   python test.py")

    print("\n5. For help and troubleshooting:")
    print("   python validate_installation.py")

    print("\n🔗 Useful Files:")
    print("   • OFFLINE_INSTALLATION_GUIDE.md - Complete setup and usage guide")
    print("   • DOCUMENTATION.md - Detailed API documentation")
    print("   • test.py - Comprehensive test suite")
    print("   • validate_installation.py - Installation validator")

def main():
    """Main setup function"""
    print_header()

    # Run setup steps
    steps = [
        ("Python Version Check", check_python_version),
        ("Wheel Files Check", check_wheel_files),
        ("Virtual Environment", create_virtual_environment),
        ("Package Installation", activate_and_install),
        ("Installation Validation", run_validation),
    ]

    results = []
    for step_name, step_func in steps:
        result = step_func()
        results.append((step_name, result))
        if not result:
            break

    # Print results summary
    print("\n" + "=" * 60)
    print("📋 SETUP SUMMARY")
    print("=" * 60)

    all_success = True
    for step_name, success in results:
        status = "✅ SUCCESS" if success else "❌ FAILED"
        print(f"{step_name:.<30} {status}")
        if not success:
            all_success = False

    if all_success:
        print_usage_instructions()
        print("\n🚀 Ready to use PyCelonis!")
        return 0
    else:
        print("\n❌ Setup failed. Please check the errors above.")
        print("   Refer to OFFLINE_INSTALLATION_GUIDE.md for troubleshooting.")
        return 1

if __name__ == "__main__":
    sys.exit(main())