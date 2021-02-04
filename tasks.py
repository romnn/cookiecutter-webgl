"""Development tasks for the cookiecutter template project"""

import webbrowser
import platform
from invoke import task
from pathlib import Path

Path().expanduser()

ROOT_DIR = Path(__file__).parent
TEST_DIR = ROOT_DIR.joinpath("tests")


@task
def test(c):
    """
    Run tests
    """
    c.run("pipenv run pytest")


@task
def generate(c):
    """
    Generate a default template
    """
    c.run("pipenv run cookiecutter {} --no-input".format(ROOT_DIR))
