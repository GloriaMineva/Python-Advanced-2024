def even_odd(*args):
    command = args[-1]
    if command == 'even':
        return [el for el in args[0:-1] if el % 2 == 0]
    elif command == 'odd':
        return [el for el in args[0:-1] if el % 2 != 0]




print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))