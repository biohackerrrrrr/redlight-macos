#!/usr/bin/env python3
"""
RedLight macOS - Port of RedLight for macOS
Pure red display filter using CoreGraphics gamma manipulation
"""

import Quartz
import rumps
import sys
from typing import Optional

class RedLightApp(rumps.App):
    def __init__(self):
        super(RedLightApp, self).__init__(
            "🔴 RED",
            icon=None,
            quit_button="Quit"
        )
        
        self.active = False
        self.original_gamma = {}
        
        # Menu items
        self.menu = [
            rumps.MenuItem("Toggle Red Filter", callback=self.toggle_filter),
            None,  # Separator
            rumps.MenuItem("About", callback=self.show_about)
        ]
        
        # Store original gamma ramps for all displays
        self.save_original_gamma()
        
    def save_original_gamma(self):
        """Save current gamma ramps for all displays"""
        max_displays = 16
        (err, active_displays, num_displays) = Quartz.CGGetActiveDisplayList(
            max_displays, None, None
        )
        
        if err != Quartz.kCGErrorSuccess:
            print(f"Error getting display list: {err}")
            return
        
        for display_id in active_displays[:num_displays]:
            # Get current gamma
            (err, red_min, red_max, red_gamma,
             green_min, green_max, green_gamma,
             blue_min, blue_max, blue_gamma) = Quartz.CGGetDisplayTransferByFormula(
                display_id, None, None, None, None, None, None, None, None, None
            )
            
            if err == Quartz.kCGErrorSuccess:
                self.original_gamma[display_id] = {
                    'red': (red_min, red_max, red_gamma),
                    'green': (green_min, green_max, green_gamma),
                    'blue': (blue_min, blue_max, blue_gamma)
                }
                print(f"Saved gamma for display {display_id}")
    
    def apply_red_filter(self):
        """Apply red-only filter to all displays"""
        max_displays = 16
        (err, active_displays, num_displays) = Quartz.CGGetActiveDisplayList(
            max_displays, None, None
        )
        
        if err != Quartz.kCGErrorSuccess:
            print(f"Error getting display list: {err}")
            return False
        
        success = True
        for display_id in active_displays[:num_displays]:
            # Red channel: normal (0.0 to 1.0, gamma 1.0)
            # Green/Blue channels: zero (0.0 to 0.0, gamma 1.0)
            err = Quartz.CGSetDisplayTransferByFormula(
                display_id,
                0.0, 1.0, 1.0,  # Red: min=0, max=1, gamma=1
                0.0, 0.0, 1.0,  # Green: min=0, max=0, gamma=1 (OFF)
                0.0, 0.0, 1.0   # Blue: min=0, max=0, gamma=1 (OFF)
            )
            
            if err != Quartz.kCGErrorSuccess:
                print(f"Error setting red filter on display {display_id}: {err}")
                success = False
            else:
                print(f"Applied red filter to display {display_id}")
        
        return success
    
    def restore_original_gamma(self):
        """Restore original gamma ramps"""
        success = True
        
        for display_id, gamma in self.original_gamma.items():
            red_min, red_max, red_gamma = gamma['red']
            green_min, green_max, green_gamma = gamma['green']
            blue_min, blue_max, blue_gamma = gamma['blue']
            
            err = Quartz.CGSetDisplayTransferByFormula(
                display_id,
                red_min, red_max, red_gamma,
                green_min, green_max, green_gamma,
                blue_min, blue_max, blue_gamma
            )
            
            if err != Quartz.kCGErrorSuccess:
                print(f"Error restoring gamma on display {display_id}: {err}")
                success = False
            else:
                print(f"Restored gamma for display {display_id}")
        
        return success
    
    @rumps.clicked("Toggle Red Filter")
    def toggle_filter(self, _):
        """Toggle red filter on/off"""
        if self.active:
            # Turn off - restore original
            if self.restore_original_gamma():
                self.active = False
                self.title = "⚪ OFF"
                rumps.notification(
                    "RedLight",
                    "Filter Disabled",
                    "Display restored to normal"
                )
            else:
                rumps.alert("Error", "Failed to restore display")
        else:
            # Turn on - apply red filter
            if self.apply_red_filter():
                self.active = True
                self.title = "🔴 RED"
                rumps.notification(
                    "RedLight",
                    "Filter Enabled",
                    "Red-only display filter active"
                )
            else:
                rumps.alert("Error", "Failed to apply red filter")
    
    @rumps.clicked("About")
    def show_about(self, _):
        """Show about dialog"""
        rumps.alert(
            "RedLight for macOS",
            "Version 1.0\n\n"
            "A pure red display filter for macOS.\n"
            "Blocks blue and green light for better sleep.\n\n"
            "Port of RedLight (Windows) by Michael Mawhinney\n"
            "macOS port: Cortana AI\n\n"
            "License: GPLv3"
        )
    
    def will_terminate(self):
        """Clean up when app terminates"""
        if self.active:
            self.restore_original_gamma()
        print("RedLight terminated")

if __name__ == "__main__":
    try:
        app = RedLightApp()
        app.run()
    except KeyboardInterrupt:
        print("\nShutting down RedLight...")
        sys.exit(0)
