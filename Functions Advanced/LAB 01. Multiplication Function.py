def multiply(*args):
    multiplication_result = 1
    for el in args:
        multiplication_result *= el
    return multiplication_result


a = [1, 2, 3]

print(multiply(*a))
