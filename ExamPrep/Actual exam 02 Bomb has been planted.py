from collections import deque
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
ROWS, COWS = [int(el) for el in input().split(', ')]
matrix = []
seconds = 16
for i in range(ROWS):
    row = list(input())
    if 'C' in row:
        start_row = i
        start_col = row.index('C')
    matrix.append(row)
curr_row = start_row
curr_col = start_col
while True:
    command = input()
    if command in directions:
        seconds -= 1
        des_row = directions[command][0] + curr_row
        des_col = directions[command][1] + curr_col
        if des_row in range(ROWS) and des_col in range(COWS):
            if matrix[des_row][des_col] == "*":
                curr_row = des_row
                curr_col = des_col
            elif matrix[des_row][des_col] == "B":
                curr_row = des_row
                curr_col = des_col
            elif matrix[des_row][des_col] == "T":
                matrix[des_row][des_col] = "*"
                print('Terrorists win!')
                break
            elif matrix[des_row][des_col] == "C":
                curr_row = des_row
                curr_col = des_col
    elif command == 'defuse':
        if not matrix[curr_row][curr_col] == 'B':
            seconds -= 2
        else:
            seconds -= 4
            if seconds >= 0:
                matrix[curr_row][curr_col] = 'D'
                print('Counter-terrorist wins!')
                print(f'Bomb has been defused: {seconds} second/s remaining.')
                break
            else:
                matrix[curr_row][curr_col] = 'X'
                print('Terrorists win!')
                print('Bomb was not defused successfully!')
                print(f'Time needed: {abs(seconds)} second/s.')
                break
    if seconds <= 0:
        print('Terrorists win!')
        print('Bomb was not defused successfully!')
        print(f'Time needed: 0 second/s.')
        break
for j in range(ROWS):
    print(''.join(matrix[j]))



