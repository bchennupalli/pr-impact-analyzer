# setup.py
from setuptools import setup, find_packages

setup(
    name="pr-impact-analyzer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "networkx",
        "jinja2",
    ],
    entry_points={
        "console_scripts": [
            "pr-impact-analyzer=pr_impact_analyzer.cli:main",
        ],
    },
    author="Your Name",
    description="Analyze PR impact on APIs and modules",
    license="MIT",
    keywords="git pr impact analyzer code graph",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
