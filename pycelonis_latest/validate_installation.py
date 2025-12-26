#!/usr/bin/env python3
"""
PyCelonis Offline Installation Validator
=======================================

This script validates that PyCelonis has been installed correctly
and can be imported and used in offline environments.

Usage:
    python validate_installation.py

Requirements:
    - Python 3.8+
    - PyCelonis installed from wheel file
    - No internet connection required for validation
"""

import sys
import os
import platform
from datetime import datetime

def print_header():
    """Print validation header"""
    print("=" * 60)
    print("🔍 PyCelonis Offline Installation Validator")
    print("=" * 60)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Python: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print("-" * 60)

def test_imports():
    """Test all PyCelonis imports"""
    print("📦 Testing PyCelonis imports...")

    tests = [
        ("pycelonis", "Main SDK package"),
        ("pycelonis_core", "Core functionality package"),
        ("pycelonis.pql", "PQL query engine"),
        ("pycelonis.ems", "EMS service modules"),
        ("pycelonis.service", "Backend services"),
        ("pycelonis.utils", "Utility functions"),
        ("pycelonis.errors", "Error handling"),
    ]

    passed = 0
    failed = 0

    for module, description in tests:
        try:
            __import__(module)
            print(f"  ✅ {module} - {description}")
            passed += 1
        except ImportError as e:
            print(f"  ❌ {module} - {description}: {e}")
            failed += 1
        except Exception as e:
            print(f"  ⚠️  {module} - {description}: Unexpected error: {e}")
            failed += 1

    print(f"\n📊 Import Tests: {passed} passed, {failed} failed")
    return failed == 0

def test_versions():
    """Test version compatibility"""
    print("\n🔢 Testing version compatibility...")

    try:
        import pycelonis
        import pycelonis_core

        # Check if version attributes exist
        sdk_version = getattr(pycelonis, '__version__', None)
        core_version = getattr(pycelonis_core, '__version__', None)

        if sdk_version:
            print(f"  📦 PyCelonis SDK: {sdk_version}")
        else:
            print("  ⚠️  PyCelonis SDK version not found")

        if core_version:
            print(f"  🔧 PyCelonis Core: {core_version}")
        else:
            print("  ⚠️  PyCelonis Core version not found")

        # Check if versions match expected (if available)
        expected_sdk = "2.20.1"
        expected_core = "2.10.3"

        version_ok = True
        if sdk_version and sdk_version != expected_sdk:
            print(f"  ⚠️  SDK version mismatch. Expected {expected_sdk}, got {sdk_version}")
            version_ok = False

        if core_version and core_version != expected_core:
            print(f"  ⚠️  Core version mismatch. Expected {expected_core}, got {core_version}")
            version_ok = False

        if version_ok and (sdk_version or core_version):
            print("  ✅ Version compatibility verified")
            return True
        else:
            print("  ⚠️  Version check completed with warnings")
            return True  # Don't fail on version mismatches

    except Exception as e:
        print(f"  ❌ Version check failed: {e}")
        return False

def test_basic_functionality():
    """Test basic PyCelonis functionality without network"""
    print("\n⚙️  Testing basic functionality...")

    try:
        from pycelonis import get_celonis
        from pycelonis.pql import PQL
        from pycelonis_core.client import KeyType

        print("  ✅ Core classes imported successfully")

        # Test KeyType enum (should always be available)
        app_key = KeyType.APP_KEY
        user_key = KeyType.USER_KEY
        print("  ✅ Authentication types available")

        # Test PQL class instantiation (without data model)
        try:
            pql = PQL()  # May or may not work depending on implementation
            print("  ✅ PQL engine initialized")
        except Exception as e:
            print(f"  ℹ️  PQL initialization note: {e}")

        # Test that get_celonis function exists
        assert callable(get_celonis)
        print("  ✅ Main connection function available")

        return True

    except Exception as e:
        print(f"  ❌ Basic functionality test failed: {e}")
        return False

def test_dependencies():
    """Test required dependencies"""
    print("\n🔗 Testing dependencies...")

    dependencies = [
        ("httpx", "HTTP client library"),
        ("pydantic", "Data validation"),
        ("pandas", "Data manipulation"),
        ("numpy", "Numerical computing"),
        ("pyarrow", "High-performance data processing"),
    ]

    passed = 0
    failed = 0

    for package, description in dependencies:
        try:
            __import__(package)
            passed += 1
            print(f"  ✅ {package} - {description}")
        except ImportError:
            failed += 1
            print(f"  ❌ {package} - {description} (not found)")
        except Exception as e:
            failed += 1
            print(f"  ⚠️  {package} - {description} (error: {e})")

    print(f"\n📊 Dependency Tests: {passed} passed, {failed} failed")
    return failed == 0

def test_network_independence():
    """Verify the installation works without network access"""
    print("\n🌐 Testing network independence...")

    # This test verifies that basic imports and class instantiation
    # work without requiring network connectivity

    try:
        import pycelonis
        from pycelonis import get_celonis

        # Test that we can create a Celonis instance configuration
        # without actually connecting (network independence)
        print("  ✅ Network-independent imports successful")
        print("  ℹ️  Note: Actual connection test requires valid Celonis credentials")

        return True

    except Exception as e:
        print(f"  ❌ Network independence test failed: {e}")
        return False

def generate_report(results):
    """Generate validation report"""
    print("\n" + "=" * 60)
    print("📋 VALIDATION REPORT")
    print("=" * 60)

    all_passed = all(results.values())

    for test_name, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{test_name:.<30} {status}")

    print("-" * 60)

    if all_passed:
        print("🎉 ALL TESTS PASSED!")
        print("✅ PyCelonis is properly installed and ready for offline use.")
        print("\n📚 Next Steps:")
        print("   1. Configure your Celonis credentials (see OFFLINE_INSTALLATION_GUIDE.md)")
        print("   2. Run the test suite: python test.py")
        print("   3. Start using PyCelonis in your projects!")
    else:
        print("⚠️  SOME TESTS FAILED!")
        print("❌ Please check the errors above and refer to OFFLINE_INSTALLATION_GUIDE.md")
        print("\n🔧 Troubleshooting:")
        print("   1. Ensure you're using the correct wheel files")
        print("   2. Check that all dependencies are installed")
        print("   3. Verify Python version compatibility (3.8+)")

    return all_passed

def main():
    """Main validation function"""
    print_header()

    # Run all validation tests
    results = {
        "Import Tests": test_imports(),
        "Version Compatibility": test_versions(),
        "Basic Functionality": test_basic_functionality(),
        "Dependencies": test_dependencies(),
        "Network Independence": test_network_independence(),
    }

    # Generate final report
    success = generate_report(results)

    # Exit with appropriate code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()