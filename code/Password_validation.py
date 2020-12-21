# Password validation checks

def contains_digit_and_char(inputString):
    digit_check = any(char.isdigit() for char in inputString)
    alpha_check = any(char.isalpha() for char in inputString)
    if not digit_check:
        print("Password invalid, password must contain atleast 1 digit")
    if not alpha_check:
        print("Password invalid, password must contain atleast 1 letter")
    return digit_check and alpha_check


def length_check(inputString):
    length_valid = len(inputString) > 5
    if not length_valid:
        print("Password invalid, password must be longer than 5 characters")
    return length_valid


def case_check(inputString):
    lower_check = any(char.islower() for char in inputString)
    upper_check = any(char.isupper() for char in inputString)
    if not lower_check:
        print("Password invalid, password must contain atleast 1 lower case letter")
    if not upper_check:
        print("Password invalid, password must contain atleast 1 upper case letter")
    return lower_check and upper_check


def run_checks(inputString):
    return contains_digit_and_char(inputString) and length_check(inputString) and case_check(inputString)
