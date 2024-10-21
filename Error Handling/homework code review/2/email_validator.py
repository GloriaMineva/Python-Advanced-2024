class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


email = input()

while email != 'End':

    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = email.split("@")

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain_info = '.' + domain.split(".")[-1]

    if domain_info not in f"{['.com', '.bg', '.net', '.org']}":
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    email = input()

    print("Email is valid")
