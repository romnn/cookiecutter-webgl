import re
import sys
import subprocess

try:
    from npm_package_validator import valid_new_package
    from npm_package_validator.validate import validate_package
except (ImportError, ModuleNotFoundError):
    print("Installing npm_package_validator...")
    subprocess.check_output(
        "pip install --no-cache-dir npm_package_validator", stderr=subprocess.STDOUT, shell=True
    )

    try:
        from npm_package_validator import valid_new_package
        from npm_package_validator.validate import validate_package
    except Exception:
        print("Failed to install npm_package_validator to validate package name.")
        print("Aborting")
        sys.exit(1)

package_name = "{{cookiecutter.project_slug}}"

errors, warnings = validate_package(package_name)
if not valid_new_package(package_name):
    print(f"ERROR: The project slug ({package_name}) is not a valid npm package name.")
    for issue in errors + warnings:
        print(f"HINT: {issue}")

    # Exit to cancel project creation
    sys.exit(1)