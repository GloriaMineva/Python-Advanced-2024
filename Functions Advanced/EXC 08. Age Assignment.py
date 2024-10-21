def age_assignment(*args, **kwargs) -> str:
    result = []
    for person in args:
        result.append(f'{person} is {kwargs[person[0]]} years old.')
    return '\n'.join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))