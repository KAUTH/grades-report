#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2020 KAUTH
"""

import os
import setuptools
import sys

here = os.path.abspath(os.path.dirname(__file__))
about = {}

requirements = ["markdown", "click>=7.1.2"]
test_requirements = ["pytest>=3"]

# 'setup.py publish' shortcut.
if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()

with open(os.path.join(here, "grades_report", "__version__.py"), "r") as f:
    exec(f.read(), about)

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="grades-report",
    version=about["__version__"],
    author="KAUTH",
    author_email="konpap1996@hotmail.com",
    url="https://github.com/KAUTH/grades-report",
    description="Get info and stats about grades",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=setuptools.find_packages(),
    # "include_package_data" allows files to be copied at install time to the
    # package’s folder inside site-packages
    include_package_data=True,
    install_requires=requirements,
    # Link: https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Education",
    ],
    tests_require=test_requirements,
    python_requires=">=3.7",
    zip_safe=False,
    project_urls={
        "Source": "https://github.com/KAUTH/grades-report"
    },
    entry_points={
        "console_scripts": ["grades-report=grades_report.cli:cli"],
    },
)
