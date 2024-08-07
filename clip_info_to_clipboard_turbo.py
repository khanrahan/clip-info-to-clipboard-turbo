"""
Script Name: Clip Info to Clipboard Turbo
Written by: Kieran Hanrahan

Script Version: 1.0.0
Flame Version: 2023.2

URL: http://github.com/khanrahan/clip-info-to-clipboard-turbo

Creation Date: 08.06.24
Update Date: 08.06.24

Acknowledgements:

    Thanks to Andy Milkis and his clip-info-to-clipboard script.  My turbo script
    just removes the UI window.

Description:

    Copy selected clip info to clipboard.  The details copied are clip name, frame rate,
    clip duration, first frame timecode, and last frame timecode.

Menus:

    Right-click on clip in Media Panel --> Copy... --> Clip Info to Clipboard Turbo

To Install:

    Copy script into /opt/Autodesk/shared/python/
"""

import flame
from PySide2 import QtWidgets

TITLE = 'Clip Info to Clipboard Turbo'
VERSION_INFO = (1, 0, 0,)
VERSION = '.'.join([str(num) for num in VERSION_INFO])
TITLE_VERSION = f'{TITLE} v{VERSION}'
MESSAGE_PREFIX = '[PYTHON]'


def message(string):
    """Print message to shell window and append global MESSAGE_PREFIX."""
    print(' '.join([MESSAGE_PREFIX, string]))


def get_clip_info(clip):
    """Return a formatted string containing the specific details of clip info."""
    frame_rate = clip.frame_rate
    duration = clip.duration.frame
    tc_in = clip.start_time.get_value()
    tc_out = tc_in + (duration - 1)

    clip_name = 'Clip Name: ' + clip.name.get_value()
    frame_rate = 'Frame Rate: ' + str(frame_rate)
    clip_dur = 'Clip Duration: ' + str(duration)
    first_frame = 'First Frame TC: ' + tc_in.timecode
    last_frame = 'Last Frame TC: ' + tc_out.timecode

    clip_info = clip_name + ' ' * 5 + \
                frame_rate + ' ' * 5 + \
                clip_dur + ' ' * 5 + \
                first_frame + ' ' * 5 + \
                last_frame

    return clip_info


def copy_to_clipboard(text):
    """Self explanitory.  Only takes a string."""
    qt_app_instance = QtWidgets.QApplication.instance()
    qt_app_instance.clipboard().setText(text)


def process_selection(selection):
    """The main function."""
    message(TITLE_VERSION)
    message(f'Script called from {__file__}')

    results = []

    for clip in selection:
        results.append(get_clip_info(clip))

    copy_to_clipboard('\n'.join(results))
    message('Copied to clipboard!')


def scope_clip(selection):
    """Determine if selection is only Clips or Sequences."""
    return all(isinstance(item, flame.PyClip) for item in selection)


def get_media_panel_custom_ui_actions():
    """Python hook to add right click menu item."""
    return [{
            'name': 'Copy...',
            'actions': [{
                    'name': TITLE,
                    'isVisible': scope_clip,
                    'execute': process_selection,
                    'minimumVersion': '2020',
                    'maximumVersion': '2023.1'
            }]
    },
    {
            'hierarchy': [],
            'name': 'Copy...',
            'actions': [{
                    'name': TITLE,
                    'isVisible': scope_clip,
                    'execute': process_selection,
                    'minimumVersion': '2023.2'
           }]
    }]
