#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
=================================================
作者：[郭磊]
手机：[15210720528]
Email：[174000902@qq.com]
Github：https://github.com/guolei19850528/py3_brhk
=================================================
"""

import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="py3-brhk",
    version="1.0.1",
    description="The Python3 Brhk Library Developed By Guolei",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guolei19850528/py3_brhk",
    author="guolei",
    author_email="174000902@qq.com",
    license="MIT",
    keywors=["brhk", "天津博瑞皓科", "博瑞皓科", "智能音箱"],
    packages=setuptools.find_packages('./'),
    install_requires=[
        "requests",
        "addict",
        "retrying",
        "jsonschema",
        "diskcache",
        "redis",
    ],
    python_requires='>=3.0',
    zip_safe=False
)
