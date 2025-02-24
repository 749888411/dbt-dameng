#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

     https://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
"""

"""The setup script."""
import sys
from setuptools import setup, find_packages

# lockstep with dbt-core==1.1 which requires Python > 3.7.2
if sys.version_info < (3, 7, 0):
    print("Error: dbt-dameng does not support this version of Python.")
    print("Please upgrade to Python 3.7.1 or higher.")
    sys.exit(1)

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    "dbt-core==1.4.5",
    "dmPython==2.4.5",
]

test_requirements = [
    "dbt-tests-adapter==1.4.5",
    "pytest"
]

project_urls = {
    'Documentation': 'https://github.com/sqlking22/dbt-dameng',
    'Source': 'https://github.com/sqlking22/dbt-dameng',
    'Bug Tracker': 'https://github.com/sqlking22/dbt-dameng/issues',
    'CI': 'https://github.com/sqlking22/dbt-dameng/actions',
    "Release Notes": "https://github.com/sqlking22/dbt-dameng/releases"
}

package_name = "dbt-dameng"
package_version = "1.4.5"
description = """The dameng adapter plugin for dbt (data build tool)"""
url = 'https://github.com/sqlking22/dbt-dameng'

setup(
    author="sqlking22",
    python_requires='>=3.7.1',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    description=description,
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    name=package_name,
    packages=find_packages(),
    test_suite='tests',
    tests_require=test_requirements,
    url=url,
    project_urls=project_urls,
    version=package_version,
    zip_safe=False,
    package_data={
        'dbt': [
            'include/dameng/dbt_project.yml',
            'include/dameng/profile_template.yml',
            'include/dameng/macros/*.sql',
            'include/dameng/macros/**/**/*.sql'
        ]
    }
)
