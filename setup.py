#!/usr/bin/env python
from setuptools import find_packages
from setuptools import setup
import pathlib

package_name = "dbt-vertica_sprint1"
package_version = "1.0.4.0"
description = """The vertica adapter plugin for dbt (data build tool)"""

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

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
    ],
    extras_require={
        'dev': [
            'dbt-tests-adapter==1.3.0',
        ]
    }
)
