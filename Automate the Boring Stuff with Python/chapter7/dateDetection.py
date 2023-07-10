# dateDetection.py - Program to detect dates in dd/mm/yyyy format.

import re

def is_valid_date(date_string):
    # Step 1: Create a regex for the date format.
    dateRegex = re.compile(r'''(
        (0[1-9]|[1-2][0-9]|3[0-1])      # day
        (\/)                            # separator
        (0[1-9]|[1][1-2])               # month
        (\/)                            # separator
        ([1-2]\d{3})                    # year
    )''', re.VERBOSE)

    # Step 2: Code to detect the validity of the date
    dateMatch = dateRegex.search(date_string)
    if dateMatch:
        # Extracting day, month, and year groups
        day = int(dateMatch.group(2))
        month = int(dateMatch.group(4))
        year = int(dateMatch.group(6))

        # Check if this year is leap year
        is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        # Define the number of days in each month
        month_days = {
            1: 31,                           # January
            2: 29 if is_leap_year else 28,  # February
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        # Check if the day, month, and year are within valid ranges.
        if(
            1 <= month <= 12 and
            1 <= day <= month_days[month] and
            1000 <= year <= 2999
        ):
            return True
    return False

date_string = "31/01/2023"
print(is_valid_date(date_string))