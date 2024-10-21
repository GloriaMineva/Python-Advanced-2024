from collections import deque

hazelnuts = 0
SIZE = int(input())
commands = deque(input().split(', '))
matrix = []
curr_row = None
curr_col = None
for i in range(SIZE):
    row = list(input())
    matrix.append(row)
    if 's' in row:
        curr_row = i
        curr_col = row.index('s')
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
while commands:
    move_direction = commands.popleft()
    desired_row = curr_row + directions[move_direction][0]
    desired_col = curr_col + directions[move_direction][1]
    if desired_row not in range(SIZE) or desired_col not in range(SIZE):
        print('The squirrel is out of the field.')
        break
    if matrix[desired_row][desired_col] == 't':
        print('Unfortunately, the squirrel stepped on a trap...')
        break
    elif matrix[desired_row][desired_col] == '*':
        curr_row = desired_row
        curr_col = desired_col
    elif matrix[desired_row][desired_col] == 'h':
        hazelnuts += 1
        if hazelnuts >= 3:
            print('Good job! You have collected all hazelnuts!')
            break
        matrix[curr_row][curr_col] = '*'
        curr_row = desired_row
        curr_col = desired_col
        matrix[curr_row][curr_col] = 's'
else:
    print('There are more hazelnuts to collect.')
print(f'Hazelnuts collected: {hazelnuts}')