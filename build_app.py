#!/usr/bin/env python3
"""
Build script for RedLight macOS .app bundle.
Usage: python3 build_app.py
"""
import subprocess
import sys

# Remove install_requires temporarily for py2app and build
import setup

# Use py2applet-style approach: write a setup.cfg for py2app
with open("setup.cfg", "w") as f:
    f.write("[py2app]\n")

result = subprocess.run([
    sys.executable, "setup.py", "py2app",
    "--app", "RedLight",
    "--includes", "rumps,Quartz",
    "--packages", "rumps,Quartz",
], cwd="/Users/biohacker/.openclaw/workspace/research/tools/redlight-mac")

# Clean up
import os
for fn in ["setup.cfg", "build"]:
    if os.path.exists(fn):
        pass  # keep for now

if result.returncode == 0:
    print("\n✅ RedLight.app built at dist/RedLight.app")
else:
    print(f"\n❌ Build failed (code {result.returncode})")
    sys.exit(1)