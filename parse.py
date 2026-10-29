"""
Sign-up form, step 3: PARSE

The input is an already clean, valid 10-digit number.

format_phone(digits) returns it the way people read it:
    format_phone("7185550142")  ->  "(718) 555-0142"

parse_phone(digits) returns its three named parts:
    parse_phone("3475550199")  ->  {"area": "347", "exchange": "555", "line": "0199"}
"""

# In:
# Out:


def format_phone(digits):
    return digits  # replace this line


def parse_phone(digits):
    return {}  # replace this line


print(format_phone("7185550142"))  # expected (718) 555-0142
print(parse_phone("3475550199"))   # expected {'area': '347', 'exchange': '555', 'line': '0199'}
