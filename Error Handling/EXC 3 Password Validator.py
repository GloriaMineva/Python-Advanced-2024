class PasswordTooShortError(Exception):
    """Password must contain at least 8 characters"""
    pass


class PasswordTooCommonError(Exception):
    """Password must be a combination of digits, letters, and special characters"""
    pass


class PasswordNoSpecialCharactersError(Exception):
    """Password must contain at least 1 special character"""
    pass


class PasswordContainsSpacesError(Exception):
    """Password must not contain empty spaces"""
    pass


password = input()
special_chr_list = ("@", "*", "&", "%")
while password != 'Done':
    if len(password) < 8:
        raise PasswordTooShortError('Password must contain at least 8 characters')
    if password.isdigit() or password.isalpha() or all(el in special_chr_list for el in password):
        raise PasswordTooCommonError('Password must be a combination of digits, letters, and special characters')
    if not any(el in special_chr_list for el in password):
        raise PasswordNoSpecialCharactersError('Password must contain at least 1 special character')
    if ' ' in password:
        raise PasswordContainsSpacesError('Password must not contain empty spaces')
    print('Password is valid')
    password = input()

