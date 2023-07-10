# strongPasswordDetection.py

import re

def is_strong_password(password):
    passwordRegex = re.compile(r'''(
        (?=.*\d)        # Positive lookahead assertion that checks if there's at least one digit ahead.
        (?=.*[a-z])     # Positive lookahead assertion that checks if there's at least one lowercase letter ahead.
        (?=.*[A-Z])     # Positive lookahead assertion that checks if there's at least one uppercase letter ahead.
        .{8,}           # Matches any character except newlines, and requires a minimum of 8 or more characters.
    )''', re.VERBOSE)

    if passwordRegex.match(password):
        return True
    else:
        return False
    
password = "Visual23"
print(is_strong_password(password))