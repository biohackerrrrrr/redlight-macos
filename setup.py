"""
RedLight for macOS
Pure red display filter using CoreGraphics gamma manipulation.
"""
from setuptools import setup

setup(
    name="redlight-macos",
    version="1.0.0",
    description="Pure red display filter for macOS — blocks blue and green light for better sleep",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="biohackerrrrrr",
    author_email="oran@biohacker.com",
    url="https://github.com/biohackerrrrrr/redlight-macos",
    py_modules=["redlight"],
    python_requires=">=3.8",
    install_requires=[
        "rumps>=0.4.0",
        "pyobjc-framework-Quartz>=10.0",
    ],
    entry_points={
        "console_scripts": [
            "redlight=redlight:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: MacOS X",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    license="GPLv3",
)