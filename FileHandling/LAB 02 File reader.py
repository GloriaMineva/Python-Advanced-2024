file_sum = 0
try:
    file = open('numbers.txt', 'r')
    lines = file.readlines()
    for line in lines:
        file_sum += int(line[:-1])
except FileNotFoundError:
    print('File not found')
print(file_sum)