"""
Py2app setup for building RedLight macOS .app bundle.
Usage: python3 py2app_setup.py py2app
"""
from setuptools import setup

setup(
    name="RedLight",
    app=["redlight.py"],
    options={
        "py2app": {
            "packages": ["rumps", "Quartz"],
            "includes": ["rumps", "Quartz"],
        }
    },
    data_files=[],
)