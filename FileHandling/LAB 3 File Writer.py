# file = open('my_first_file.txt', 'a')
# file.write('I just created my first file!')
# print(file.read())

with open('my_first_file.txt', 'w') as file:
    file.write('I just created my first file!')
    file.close()

print(file.closed)
print(file.read())
