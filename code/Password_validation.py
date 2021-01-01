# Password validation checks


def contains_digit_and_char(input_string):
    digit_check = any(char.isdigit() for char in input_string)
    alpha_check = any(char.isalpha() for char in input_string)
    if not digit_check:
        print("Password invalid, password must contain at least 1 digit")
    if not alpha_check:
        print("Password invalid, password must contain at least 1 letter")
    return digit_check and alpha_check


def length_check(input_string):
    length_valid = len(input_string) > 5
    if not length_valid:
        print("Password must be at least 6 characters")
    return length_valid


def case_check(input_string):
    lower_check = any(char.islower() for char in input_string)
    upper_check = any(char.isupper() for char in input_string)
    if not lower_check:
        print("Password invalid, password must contain at least 1 lower case letter")
    if not upper_check:
        print("Password invalid, password must contain at least 1 upper case letter")
    return lower_check and upper_check


def run_checks(input_string):
    return contains_digit_and_char(input_string) and length_check(input_string) and case_check(input_string)
