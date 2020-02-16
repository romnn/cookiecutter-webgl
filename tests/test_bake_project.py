import datetime
import importlib.util
import json
import os
import shlex
import subprocess
from contextlib import contextmanager

from ruamel.yaml import YAML
from click.testing import CliRunner
from cookiecutter.utils import rmtree


yaml = YAML()
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir_path, "../cookiecutter.json")) as cookiecutter_config_file:
    default_package_name = (
        json.load(cookiecutter_config_file)
        .get("project_name", "Python Package Template")
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
    )


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(str(dirpath))
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        try:
            return subprocess.check_call(shlex.split(command))
        except subprocess.CalledProcessError as e:
            return e.returncode


def check_output_inside_dir(command, dirpath):
    """Run a command from inside a given directory, returning the command output"""
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    project_path = str(result.project)
    project_slug = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, project_slug)
    return project_path, project_slug, project_dir


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "package.json" in found_toplevel_files
        assert "tsconfig.json" in found_toplevel_files
        assert "webpack.config.js" in found_toplevel_files
        assert "index.html" in found_toplevel_files
        assert "README.md" in found_toplevel_files
        assert "src" in found_toplevel_files


def test_year_compute_in_license_file(cookies):
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project.join("LICENSE")
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read()


def test_optional_pre_commit_linting(cookies):
    with bake_in_temp_dir(cookies) as result:
        package_json_file_path = result.project.join("package.json")
        config = json.loads(package_json_file_path.read())
        assert config["husky"]["hooks"] == {"pre-commit": "yarn lint"}

    # Disable lint pre commit hook
    with bake_in_temp_dir(
        cookies, extra_context=dict(pre_commit_linting="no")
    ) as result:
        package_json_file_path = result.project.join("package.json")
        config = json.loads(package_json_file_path.read())
        assert config["husky"]["hooks"] == {}


def test_treat_linter_warnings_as_errors(cookies):
    with bake_in_temp_dir(cookies) as result:
        package_json_file_path = result.project.join("package.json")
        config = json.loads(package_json_file_path.read())
        assert "--max-warnings=0" in config["scripts"]["lint"]

    # Disable treat_linter_warnings_as_errors
    with bake_in_temp_dir(
        cookies, extra_context=dict(treat_lint_warnings_as_errors="no")
    ) as result:
        package_json_file_path = result.project.join("package.json")
        config = json.loads(package_json_file_path.read())
        assert "--max-warnings=-1" in config["scripts"]["lint"]
