"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

def main():
    symbol = "*"
    password = get_password()
    while not is_valid_password(password):
        print("Invalid password!")
        password = get_password()
    print("Your {}-character password is valid: {}".format(len(password),password))

def get_password():
    print("Please enter a valid password")
    print("Your password must contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more special characters")
    print("\t1 or more numbers")
    password = input("> ")
    return password

def is_valid_password(password):
    valid_password = False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    if len(password) <= 0 :
        return False
    for char in password :
        if char.isdigit():
            count_digit += 1
        if char.islower():
            count_lower += 1
        if char.isupper():
            count_upper += 1
        if not char.isalnum():
            count_special += 1
        if count_upper >= 1 and count_lower >= 1 and count_digit >= 1 and count_special >= 1:
            valid_password = True
    return valid_password

main()