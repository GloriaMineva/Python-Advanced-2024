user_data = list(input())
# reversed_user_data = user_data[::-1]
# print(reversed_user_data)
reversed_stack = ''
while user_data:
    reversed_stack += user_data.pop()
print(reversed_stack)
