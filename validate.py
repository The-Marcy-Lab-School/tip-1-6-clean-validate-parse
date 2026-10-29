"""
Sign-up form, step 2: VALIDATE

A phone number is valid when:
  1. it has only digits and these characters: ( ) - . + and space
  2. after cleaning, it has exactly 10 digits
  3. the area code doesn't start with 0 or 1
"""

ALLOWED = "()-. +"


# A working cleaner, so you can start here even if clean.py isn't done.
def normalize_phone(raw):
    digits = ""
    for ch in raw:
        if ch.isdigit():
            digits += ch
    if len(digits) == 11 and digits[0] == "1":
        digits = digits[1:]
    return digits


# ---------------------------------------------------------------
# Part 2a: A teammate wrote these two helpers. Predict, then run.
# ---------------------------------------------------------------

def only_phone_chars(raw):
    for ch in raw:
        if ch.isdigit() or ch in ALLOWED:
            return True
        else:
            return False


def area_code_ok(digits):
    if digits[0] == "0" or "1":
        return False
    return True


print(only_phone_chars("(718) 555-0142"))     # expected True
# Prediction:
# Actual:
print(only_phone_chars("718-555-0142 cell"))  # expected False
# Prediction:
# Actual:
print(only_phone_chars("call me"))            # expected False
# Prediction:
# Actual:
print(only_phone_chars(""))                   # expected True (no bad characters)
# Prediction:
# Actual:
print(area_code_ok("7185550142"))             # expected True
# Prediction:
# Actual:
print(area_code_ok("0185550142"))             # expected False
# Prediction:
# Actual:

# Explanation (one sentence per helper):
#


# ---------------------------------------------------------------
# Part 2c: Your validator. Use normalize_phone and both helpers.
# ---------------------------------------------------------------

# In:
# Out:


def is_valid_phone(raw):
    return True  # replace this line


# print(is_valid_phone("(718) 555-0142"))     # expected True
# print(is_valid_phone("+1 347 555 0199"))    # expected True
# print(is_valid_phone("718-555-0142 cell"))  # expected False
# print(is_valid_phone("212-555-01"))         # expected False
# print(is_valid_phone("(018) 555-0142"))     # expected False
# print(is_valid_phone(""))                   # expected False
