counter = int(input())
stack_numbers = []
for i in range(counter):
    query = input()
    if query == '2':
        if len(stack_numbers) > 0:
            stack_numbers.pop()
    elif query == '3':
        if len(stack_numbers) > 0:
            print(max(stack_numbers))
    elif query == '4':
        if len(stack_numbers) > 0:
            print(min(stack_numbers))
    else:
        number_to_add = int(query[2:])
        stack_numbers.append(number_to_add)
while len(stack_numbers) > 1:
    print(stack_numbers.pop(), end=', ')
print(stack_numbers.pop(), end='')
