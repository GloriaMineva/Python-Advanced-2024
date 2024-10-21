from functools import reduce


def operate(operator, *args):

    def add():
        return reduce(lambda a, b: a + b, args)

    def subtract():
        return reduce(lambda a, b: a - b, args)

    def multiply():
        return reduce(lambda a, b: a * b, args)

    def divide():
        return reduce(lambda a, b: a / b if b != 0 else None, args)

    mapper = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }

    return mapper[operator]()
    # if operator == '+':
    #     return add()
    # elif operator == '-':
    #     return subtract()
    # elif operator == '*':
    #     return multiply()
    # elif operator == '/':
    #     return divide()


print(operate("-", 1, 2, 3))
