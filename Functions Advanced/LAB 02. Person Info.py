def get_info(name, town, age):
    return f'This is {name} from {town} and he is {age} years old'


info = {'name': 'glori', 'town':'sofia', 'age': 8}
print(get_info(**info))