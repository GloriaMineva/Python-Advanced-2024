def func_executor(*functions_tuple):
    result = []
    for name, args in functions_tuple:
        result.append(f'{name.__name__} - {name(*args)}')
    return '\n'.join(result)


def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
