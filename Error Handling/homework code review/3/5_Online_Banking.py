class MoneyNotEnoughError(Exception):
    pass
class PINCodeError(Exception):
    pass
class UnderageTransactionError(Exception):
    pass
class MoneyIsNegativeError(Exception):
    pass


bank_account_details = input().split(", ")
pin_code, balance, age = int(bank_account_details[0]), float(bank_account_details[1]), int(bank_account_details[2])
min_required_age = 18
command = input()

while command != "End":
    action = command.split("#")
    if action[0] == "Send Money":
        money = float(action[1])
        pin = int(action[2])
        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        if pin != pin_code:
            raise PINCodeError("Invalid PIN code")
        if age < min_required_age:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
        print(f"Successfully sent {money:.2f} money to a friend")
        balance -= money
        print(f"There is {balance:.2f} money left in the bank account")
    elif action[0] == "Receive Money":
        money = float(action[1])
        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")
        money /= 2
        print(f"{money:.2f} money went straight into the bank account")

    command = input()