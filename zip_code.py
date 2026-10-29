"""
Step	Task
1. Predict the output.
2. Debug (The output is right for this ZIP code. Make the function follow its spec for any ZIP code).
3. Adjust (Some forms collect ZIP+4, like "11375-1234": 5 digits, a dash, then 4 digits. Accept those too).
4. Test (Change the ZIP code to "1137A". Predict, then run).
"""

# A ZIP code is valid when it is exactly 5 digits.
def is_valid_zip(zip_code):
    for ch in zip_code:
        if ch.isdigit() or "-":
            return True
        else:
            return False

print(is_valid_zip("11375"))
