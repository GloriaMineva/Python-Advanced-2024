numbers_dictionary = {}

while True:
    number_as_text = input()
    if number_as_text == 'Search':
        break
    number_as_string = number_as_text
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")

while True:
    number_as_text = input()
    if number_as_text == "Remove":
        break
    searched = number_as_text
    print(numbers_dictionary[searched])

while True:
    number_as_text = input()
    if number_as_text == 'End':
        break
    searched = number_as_text
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")

print(numbers_dictionary)
