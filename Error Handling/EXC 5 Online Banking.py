pin, balance, age = [int(el) for el in input().split(', ')]
command = input()


class MoneyNotEnoughError(Exception):
    """Insufficient funds for the requested transaction"""
    pass


class PINCodeError(Exception):
    """Invalid PIN code"""
    pass


class UnderageTransactionError(Exception):
    """You must be 18 years or older to perform online transactions"""
    pass


class MoneyIsNegativeError(Exception):
    """The amount of money cannot be a negative number"""
    pass


while command != 'End':
    if command.startswith('Send Money'):
        money = int(command.split('#')[1])
        current_pin = int(command.split('#')[2])
        if balance < money:
            raise MoneyNotEnoughError('Insufficient funds for the requested transaction')
        if current_pin != pin:
            raise PINCodeError('Invalid PIN code')
        if age < 18:
            raise UnderageTransactionError('You must be 18 years or older to perform online transactions')
        balance -= money
        print(f'Successfully sent {money:.2f} money to a friend')
        print(f'There is {balance:.2f} money left in the bank account')

    elif command.startswith('Receive Money'):
        salary = int(command.split('#')[1])
        if salary < 0:
            raise MoneyIsNegativeError('The amount of money cannot be a negative number')
        balance += salary / 2
        print(f'{(salary / 2):.2f} money went straight into the bank account')

    command = input()
