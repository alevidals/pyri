import time
import unicodedata
from pynotifier import Notification

def use_pyri(pyri):
    while True:
        command = pyri.listen()
        if command is not None:
            pyri.analyze_command(command)

def slice_text(text, number, mode = 'pre', join_str = ' ', separator = ' '):
    if mode == 'pre':
        return join_str.join(text.split(separator)[number:])
    elif mode == 'app':
        return join_str.join(text.split(separator)[:number])
    else:
        return join_str.join(text.split(separator)[number])

def strip_accents_spain(string, accents=('COMBINING ACUTE ACCENT', 'COMBINING GRAVE ACCENT')):
    accents = set(map(unicodedata.lookup, accents))
    chars = [c for c in unicodedata.normalize('NFD', string) if c not in accents]
    return unicodedata.normalize('NFC', ''.join(chars))

def check_reminders(pyri):
    while True:
        print("I'm working...")
        pyri.check_reminders()
        time.sleep(1)

def make_notification(title, description, urgency = Notification.URGENCY_NORMAL, duration = 5):
    Notification(
        title=title,
        description=description,
        # icon_path='path/to/image/file/icon.png', # On Windows .ico is required, on Linux - .png
        duration=duration,                              # Duration in seconds
        urgency=urgency
    ).send()