"""Setup configuration for Villages Event Scraper."""

from setuptools import setup, find_packages
from pathlib import Path

# Read version from VERSION file
version_file = Path(__file__).parent / "VERSION"
with open(version_file, "r", encoding="utf-8") as fh:
    version = fh.read().strip()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="villages-event-scraper",
    version=version,
    author="Your Name",
    description="Fetch and format entertainment events from The Villages API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/villages-event-scraper",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "villages-events=villages_events:main",
        ],
    },
)
