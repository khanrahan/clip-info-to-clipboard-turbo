# Clip Info to Clipboard Turbo

Plugin for [Autodesk Flame software](http://www.autodesk.com/products/flame).

Thanks to Andy Milkis and his clip-info-to-clipboard script.  This turbo script just removes the UI window.
Copy clip name, framerate, duration, in point timecode, and out point timecode to the clipboard.

## Compatibility
|Script Version|Flame Version|
|---|---|
|v2.X.X|Flame 2025 and newer|
|v1.X.X|Flame 2023.3.2 up to 2024.2|

## Installation

### Flame 2025 and newer
To make available to all users on the workstation, copy `clip_info_to_clipboard_turbo.py` to `/opt/Autodesk/shared/python`

For specific users, copy `clip_info_to_clipboard_turbo.py` to the appropriate path below...
|Platform|Path|
|---|---|
|Linux|`/home/<user_name>/flame/python`|
|Mac|`/Users/<user_name>/Library/Preferences/Autodesk/flame/python`|

### Flame 2023.3.2 up to 2024.2
To make available to all users on the workstation, copy `clip_info_to_clipboard_turbo.py` to `/opt/Autodesk/shared/python`

For specific users, copy `clip_info_to_clipboard_turbo.py` to `/opt/Autodesk/user/<user name>/python`

### Last Step
Finally, inside of Flame, go to Flame (fish) menu `->` Python `->` Rescan Python Hooks

## Menus
- Right-click a selected folder in the MediaHub `->` Navigate... `->` Path Translator

## Acknowledgements
Andy Milkis of [logik.tv](http://www.logik.tv)
