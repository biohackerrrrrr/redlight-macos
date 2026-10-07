# RedLight for macOS

🔴 **Pure red display filter for macOS** — Port of [RedLight](https://github.com/michaelmawhinney/redlight) for Windows

Blocks **100% of blue and green light** from your screen. Just red. Zero melatonin suppression. Perfect for late-night work.

> ⚠️ **macOS only.** This uses macOS CoreGraphics APIs and will not work on Linux or Windows.

---

## Quick Install

### 🐍 pip (recommended)

```bash
pip3 install redlight-macos
redlight
```

### 📦 From source

```bash
git clone https://github.com/biohackerrrrrr/redlight-macos
cd redlight-macos
pip3 install -e .
redlight
```

### 🖱️ Double-click app (no terminal)

Download the latest `.app` bundle from **[Releases](https://github.com/biohackerrrrrr/redlight-macos/releases)**.

Or build it yourself:

```bash
pip3 install py2app
python3 setup.py py2app
open dist/RedLight.app
```

---

## Usage

**Menu bar app with one-click toggle:**

| State | Icon | Description |
|-------|------|-------------|
| ⚪ OFF | White icon | Normal display |
| 🔴 ON  | Red icon  | Red-only filter active |

1. Launch the app → look for the icon in your **menu bar**
2. **Click the icon** to toggle red filter on/off
3. **Cmd+Q** to quit

That's it. No config window, no sliders. One click.

---

## How It Works

Uses macOS **CoreGraphics API** to manipulate the display gamma ramps directly:

- **Red channel:** Normal (`0.0 → 1.0`)
- **Green channel:** Zero (`0.0 → 0.0`)
- **Blue channel:** Zero (`0.0 → 0.0`)

Everything on screen displays in shades of red. It's a hardware-level filter, not a software overlay — so it works across all apps, fullscreen video, lock screen, everything.

Original gamma ramps are saved on launch and restored when you toggle off or quit.

---

## Why Red Light?

Blue light at night **suppresses melatonin** and disrupts circadian rhythm. Red light has minimal impact.

| Use case | Why it helps |
|----------|-------------|
| Late-night coding | Stay productive without wrecking sleep |
| Reading before bed | Wind down naturally |
| Eye strain relief | Lower blue light = less digital eye fatigue |
| Military / astronomy | Doesn't break night-adapted vision |

Used by astronomers, submariners, and anyone who needs their screen at 3 AM without the sleep consequences.

---

## Building from Source

### Standalone .app bundle

```bash
pip3 install py2app
python3 setup.py py2app
open dist/RedLight.app
```

The resulting `.app` is fully self-contained — no Python or dependencies required on the target machine. Ready to zip and share.

### One-file executable (optional)

```bash
pip3 install pyinstaller
pyinstaller --onefile --windowed redlight.py
open dist/redlight
```

---

## Troubleshooting

**Filter won't apply:**
- **macOS 14+ (Sonoma/Sequoia):** Grant Accessibility permissions in **System Settings → Accessibility → Display → Allow apps to control display settings**
- Disable **Night Shift** / **f.lux** / display calibration tools — they conflict
- Try running from terminal to see error output

**Stuck in red mode (shouldn't happen, but just in case):**

```bash
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

**App doesn't appear in menu bar:**
- Check that `rumps` and `pyobjc-framework-Quartz` are installed
- Run from terminal: `python3 redlight.py`

---

## Dependencies

- **Python 3.8+**
- [rumps](https://github.com/jacebrowning/rumps) — macOS menu bar framework
- [pyobjc-framework-Quartz](https://github.com/ronaldoussoren/pyobjc) — macOS CoreGraphics bindings

---

## Credits

| Part | By |
|------|----|
| **Original RedLight (Windows)** | Michael Mawhinney |
| **macOS Port** | Cortana AI / [@biohacker](https://x.com/biohacker) |
| **License** | GPLv3 (same as original) |

---

## License

GNU General Public License v3.0 — see [LICENSE](./LICENSE).

---

**Status:** Working proof of concept · Version 1.0.0  
**Date:** 2026-10-07