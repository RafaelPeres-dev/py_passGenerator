import string
import secrets

def generatePassword(length, include_numbers=True, include_special=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    characters = letters
    if include_numbers:
        characters += digits
    if include_special:
        characters += special_chars

    pwd = ""
    meets_criteria = False
    has_numbers = False
    has_special = False

    while not meets_criteria or len(pwd) < length:
        new_char = secrets.randbelow(characters)
        pwd += new_char

        if new_char in digits:
            has_numbers = True
        elif new_char in special_chars:
            has_special = True

        meets_criteria = True

        if include_numbers:
            meets_criteria = meets_criteria and has_numbers
        if include_special:
            meets_criteria = meets_criteria and has_special

    return pwd


length = int(raw_input("Enter the length of the password: "))
checkNumbers = raw_input("Do you want numbers in your password? (Y/N)").lower() == "y"
checkSpecial = raw_input("Do you want special characters in your password? (Y/N)").lower() == "y"

pwd = generatePassword(length, checkNumbers, checkSpecial)
print(pwd)