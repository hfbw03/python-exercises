#! python3
# The 'text' variable is a dictionary that contains several pre-defined text snippets
# With each associated with a keyphrase.
text = {'agree': """Yes, I agree. That sounds fine to me.""",
# mclip.py - A multi-clipboard program

        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

# sys is needed for accessing command line arguments.
# pyperclip is needed for copying text to the clipboard.
import sys, pyperclip

# This block checks whether the user has provided a command line argument.
# If no argument is provided, the program prints a usage message and exits.
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

# If a command line argument is provided, the program retrieves it from 'sys.argv'.
keyphrase = sys.argv[1]

# The program checks whether the 'keyphrase' variable matches one of the 'text' dictionary.
# If it does, the corresponding value is copied to the clipboard using the copy function.
if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')

# If the 'keyphrase' variable doesn't match any of the dictionary's keys, print an error message.
else:
    print('There is no text for ' + keyphrase)