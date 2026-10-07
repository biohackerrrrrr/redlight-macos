# RedLight for macOS

🔴 **Pure red display filter for macOS** - Port of [RedLight](https://github.com/michaelmawhinney/redlight) for Windows

## What It Does

Applies a **true red-only display filter** (not a tint) that:
- Keeps red channel normal
- Blocks green and blue light completely
- Helps with sleep/circadian rhythm
- Reduces eye strain at night

## Installation

```bash
# Install dependencies
pip3 install rumps pyobjc-framework-Quartz

# Make executable
chmod +x redlight.py

# Run
./redlight.py
```

## Usage

**Menu bar app with one-click toggle:**

1. **Click menu bar icon** to toggle red filter on/off
2. **🔴 Red icon** = Filter active
3. **⚪ White icon** = Filter off

**Keyboard shortcut** (when app is focused):
- Cmd+Q to quit

## How It Works

Uses macOS CoreGraphics API to manipulate display gamma ramps:
- **Red channel:** Linear (0.0 → 1.0)
- **Green channel:** Zero (0.0 → 0.0)
- **Blue channel:** Zero (0.0 → 0.0)

Result: Everything displays in shades of red.

## Differences from Windows Version

**What's the same:**
- ✅ Pure red filter (no blue/green light)
- ✅ Toggle on/off from menu bar
- ✅ Minimal resource usage
- ✅ Automatic gamma restoration

**What's different:**
- ⚠️ No "Luma Red" mode yet (only Strict Red)
- ⚠️ No Windows Magnification API equivalent
- ✅ Uses macOS native CoreGraphics
- ✅ Python instead of C++ (easier to modify)

## Conflicts

May conflict with:
- **f.lux**
- **Night Shift**
- **Display calibration tools**

Disable these before using RedLight.

## Building Standalone App (Optional)

To create a standalone .app bundle:

```bash
pip3 install py2app
python3 setup.py py2app
```

## Troubleshooting

**Filter won't apply:**
- Check display permissions in System Settings → Privacy
- Disable Night Shift / f.lux
- Try running as: `sudo ./redlight.py`

**Stuck in red mode:**
```bash
# Reset all displays
python3 << 'EOF'
import Quartz
max_displays = 16
(err, displays, num) = Quartz.CGGetActiveDisplayList(max_displays, None, None)
for display_id in displays[:num]:
    Quartz.CGSetDisplayTransferByFormula(display_id,
        0.0, 1.0, 1.0,  # Red
        0.0, 1.0, 1.0,  # Green  
        0.0, 1.0, 1.0)  # Blue
EOF
```

## Credits

**Original RedLight (Windows):** Michael Mawhinney  
**macOS Port:** Cortana AI for biohacker  
**License:** GPLv3 (same as original)

## Why Red Light?

**Science:**
- Blue light suppresses melatonin production
- Red light has minimal impact on circadian rhythm
- Used in astronomy, military, emergency services
- Preserves night vision

**Use cases:**
- Late-night computer work
- Reading before bed
- Reducing sleep disruption
- Eye strain relief

---

**Status:** Working proof of concept  
**Version:** 1.0  
**Date:** 2026-08-03
