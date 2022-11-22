#!/usr/bin/env python
from setuptools import find_packages
from setuptools import setup
import pathlib
import os
import re


HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()


def _get_plugin_version_dict():
    _version_path = os.path.join(HERE, "dbt", "adapters", "vertica", "__version__.py")
    _semver = r"""(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)"""
    _pre = r"""((?P<prekind>a|b|rc)(?P<pre>\d+))?"""
    _version_pattern = fr"""version\s*=\s*["']{_semver}{_pre}["']"""
    with open(_version_path) as f:
        match = re.search(_version_pattern, f.read().strip())
        if match is None:
            raise ValueError(f"invalid version at {_version_path}")
        return match.groupdict()

def _get_dbt_core_version():
    parts = _get_plugin_version_dict()
    minor = "{major}.{minor}.0".format(**parts)
    pre = parts["prekind"] + "1" if parts["prekind"] else ""
    return f"{minor}{pre}"


package_name = "dbt-vertica_sprint1"
package_version = "1.3.0"
description = """The vertica adapter plugin for dbt (data build tool)"""
dbt_core_version = _get_dbt_core_version()

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=README,
    long_description_content_type='text/markdown',
    license='MIT',
    author='Matthew Carter (original), Andrew Hedengren, Andy Reagan',
    author_email='shilpa.chandrashekar15@gmail.com, sachin.thakur9614@gmail.com',
    url='https://github.com/Sachin-Thakur/dbt-vertica-3x/',
    packages=find_packages(),
    package_data={
        'dbt': [
            'include/vertica/dbt_project.yml',
            'include/vertica/macros/*.sql',
            'include/vertica/macros/adapters/*.sql',
            'include/vertica/macros/materializations/*.sql',
            'include/vertica/macros/materializations/models/incremental/*.sql',
            'include/vertica/macros/materializations/models/table/*.sql',
            'include/vertica/macros/materializations/models/view/*.sql',
            'include/vertica/macros/materializations/seeds/*.sql',
            'include/vertica/macros/materializations/snapshots/*.sql',
        ]
    },
    install_requires=[
        'dbt-core==1.3.0',
        'vertica-python>=1.1.0',
        'dbt-tests-adapter==1.3.0',
    ],
)
