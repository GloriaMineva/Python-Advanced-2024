class NameTooShortError(Exception):
    """ Name must be more than 4 characters """
    pass


class MustContainAtSymbolError(Exception):
    """ Email must contain @ """
    pass


class InvalidDomainError(Exception):
    """ Domain must be one of the following: .com, .bg, .org, .net """
    pass


domains_list = ['.com', '.bg', '.org', '.net']

while True:
    email = input()
    if email == 'End':
        break
    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')
    at_index = email.index('@')
    name = email[:at_index]
    dot_idx = email.index('.')
    domain = email[dot_idx:]
    if len(name) < 5:
        raise NameTooShortError('Name must be more than 4 characters')
    if domain not in domains_list:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
    print('Email is valid')
