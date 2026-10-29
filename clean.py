"""
Sign-up form, step 1: CLEAN

normalize_phone(raw) returns only the digits in raw.
If that leaves 11 digits that start with 1 (the US country code), drop the 1.
"""

# In:
# Out:


def normalize_phone(raw):
    return raw  # replace this line


# Warm-up tests (from memory, no notes)
print(normalize_phone("(718) 555-0142"))  # expected 7185550142
print(normalize_phone("718.555.0142"))    # expected 7185550142
print(normalize_phone("718 555 0142"))    # expected 7185550142
print(len(normalize_phone("")))           # expected 0

# Part 1 tests (uncomment when you get there)
# print(normalize_phone("+1 (718) 555-0142"))  # expected 7185550142
# Prediction (before your change):
# print(normalize_phone("1-347-555-0199"))     # expected 3475550199
# print(normalize_phone("212-555-01"))         # expected 21255501
