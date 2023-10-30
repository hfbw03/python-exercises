# idiot.py

import pyinputplus as pyip

while True:
    prompt = 'Want to kmow how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)

    if response == 'no':
        break

print('Thank you, have a nice day.')