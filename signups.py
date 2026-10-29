"""
Sign-up form, step 4: the whole list

A food pantry's text-alert sign-up form collected these numbers.
Some people signed up twice, typing their number differently each time.
Some entries aren't valid phone numbers at all.

signup_report(entries) returns two things:
  - a dict: each clean, valid number -> how many times it was signed up
  - a list of the raw entries that weren't valid

Then print the formatted numbers that signed up more than once,
and how many different people signed up.

Expected output:
{'7185550142': 2, '3475550199': 2, '9295550100': 1}
['212-555-01', '718-555-O142']
Signed up twice: ['(718) 555-0142', '(347) 555-0199']
People: 3
"""

ALLOWED = "()-. +"

# --- Working versions of steps 1-3, so you can start here ---

def normalize_phone(raw):
    digits = ""
    for ch in raw:
        if ch.isdigit():
            digits += ch
    if len(digits) == 11 and digits[0] == "1":
        digits = digits[1:]
    return digits


def only_phone_chars(raw):
    for ch in raw:
        if not (ch.isdigit() or ch in ALLOWED):
            return False
    return True


def area_code_ok(digits):
    if digits[0] in "01":
        return False
    return True


def is_valid_phone(raw):
    if not only_phone_chars(raw):
        return False
    digits = normalize_phone(raw)
    if len(digits) != 10:
        return False
    return area_code_ok(digits)


def format_phone(digits):
    return "(" + digits[0:3] + ") " + digits[3:6] + "-" + digits[6:]


# --- Your code ---

signups = [
    "(718) 555-0142",
    "718.555.0142",
    "+1 347 555 0199",
    "347-555-0199",
    "212-555-01",
    "718-555-O142",
    "(929) 555 0100",
]

# In:
# Out:


def signup_report(entries):
    counts = {}
    invalid = []
    # your code here
    return counts, invalid


counts, invalid = signup_report(signups)
print(counts)
print(invalid)
