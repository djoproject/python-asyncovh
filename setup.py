#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup


setup(
    name = "ovh",
    version = "0.4.2",
    setup_requires=['setuptools'],
    author = "Jean-Tiare Le Bigot",
    author_email = "jean-tiare.le-bigot@corp.ovh.com",
    description = "Official OVH.com API wrapper",
    license = "BSD",
    keywords = "ovh sdk rest",
    url = "http://api.ovh.com",
    packages = [
        "ovh",
        "ovh.vendor",
        "ovh.vendor.requests",
        "ovh.vendor.requests.packages",
        "ovh.vendor.requests.packages.urllib3",
        "ovh.vendor.requests.packages.urllib3.util",
        "ovh.vendor.requests.packages.urllib3.contrib",
        "ovh.vendor.requests.packages.urllib3.packages",
        "ovh.vendor.requests.packages.urllib3.packages.ssl_match_hostname",
        "ovh.vendor.requests.packages.chardet",
    ],
    package_data={
        'ovh.vendor.requests': ['*.pem'],
    },
    include_package_data=True,
    tests_require=[
        "coverage==3.7.1",
        "mock==1.0.1",
        "nose==1.3.3",
        "yanc==0.2.4",
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License"
        "Development Status :: 4 - Beta"
        "Intended Audience :: Developers"
        "Operating System :: OS Independent"
        "Programming Language :: Python"
        "Programming Language :: Python :: 2.6"
        "Programming Language :: Python :: 2.7"
        "Programming Language :: Python :: 3.2"
        "Programming Language :: Python :: 3.3"
        "Programming Language :: Python :: 3.4"
        "Programming Language :: Python :: 3.5"
        "Topic :: Software Development :: Libraries :: Python Modules"
        "Topic :: System :: Archiving :: Packaging"
    ],
)
