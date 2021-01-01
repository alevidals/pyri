import time
import unicodedata

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