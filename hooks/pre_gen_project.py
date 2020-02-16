import re
import sys
import subprocess

try:
    from npm_package_validator import valid_new_package
    from npm_package_validator.validate import validate_package
except ImportError:
    print("Installing npm-package-validator...")
    subprocess.check_output(
        "python3 -m pip install --no-cache-dir npm-package-validator", stderr=subprocess.STDOUT, shell=True
    )

    try:
        from npm_package_validator import valid_new_package
        from npm_package_validator.validate import validate_package
    except Exception:
        print("Failed to install npm-package-validator to validate package name.")
        print("Aborting")
        sys.exit(1)

package_name = "{{cookiecutter.project_slug}}"

errors, warnings = validate_package(package_name)
if not valid_new_package(package_name):
    print("ERROR: The project slug ({}) is not a valid npm package name.".format(package_name))
    for issue in errors + warnings:
        print("HINT: {}".format(issue))

    # Exit to cancel project creation
    sys.exit(1)