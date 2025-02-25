class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


special_characters = ["@", "*", "&", "%"]

password = input()

while password != 'Done':

    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if password.isdigit() or password.isalpha():
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(char in special_characters for char in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    password = input()

print("Password is valid")