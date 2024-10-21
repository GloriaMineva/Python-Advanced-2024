word = input()
try:
    number_from_user = int(input())
except ValueError:
    print('Invalid input data!Please try again.')
else:
    print(word * number_from_user)