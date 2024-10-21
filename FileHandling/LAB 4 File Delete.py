import os
try:
    os.remove('my_first_file.txt')
except FileNotFoundError:
    print('File already deleted!')
path = os.path.join("..", "di")