#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate the lines and add stars.
lines = text.split('\n')

# Loop through all indexes in 'lines' and add a star to each string in it.
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

# Join the lines together with line breaks.
text = '\n'.join(lines)

pyperclip.copy(text)