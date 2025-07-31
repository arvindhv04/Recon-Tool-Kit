#!/usr/bin/env python3
"""
Setup script for Recon-Tool-Kit
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="recon-tool-kit",
    version="2.0.0",
    author="Recon-Tool-Kit Team",
    author_email="",
    description="Enhanced Network Reconnaissance Tool for cybersecurity professionals",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Security",
        "Topic :: System :: Networking :: Monitoring",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "recon-tool-kit=main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="security, reconnaissance, network, scanning, cybersecurity, penetration-testing",
    project_urls={
        "Bug Reports": "",
        "Source": "",
        "Documentation": "",
    },
) 