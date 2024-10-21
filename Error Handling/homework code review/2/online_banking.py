class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


pin_code, balance, age = [int(x) for x in input().split(", ")]

while True:
    command = input().split("#")
    action = command[0]

    if action == 'End':
        break

    if action == 'Send Money':
        money = int(command[1])

        if age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        if int(command[2]) != pin_code:
            raise PINCodeError("Invalid PIN code")

        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        if money <= balance:
            balance -= money
            print(f"Successfully sent {money:.2f} money to a friend")
            print(f"There is {balance:.2f} money left in the bank account")
        else:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
    elif action == 'Receive Money':
        money = int(command[1])
        salary = money / 2
        if salary < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")
        balance += salary
        print(f"{salary:.2f} money went straight into the bank account")
