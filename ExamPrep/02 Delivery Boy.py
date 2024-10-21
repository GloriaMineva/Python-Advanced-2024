def enter_the_matrix(n: int):
    field = []
    for i in range(n):
        field.append(list(input()))
    return field


def visualiser(field):
    for current_row in field:
        print(''.join(current_row))


def starting_pos_finder(field: list):
    for i in range(ROWS):
        if 'B' in field[i]:
            row_ = i
            col_ = field[i].index('B')
    return row_, col_


def next_pos_calculator(row, col, command):
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }
    row = row + directions[command][0]
    rows_validator(row)
    col = col + directions[command][1]
    cols_validator(col)
    return row, col


def rows_validator(idx):
    if idx not in range(ROWS):
        print('The delivery is late. Order is canceled.')
        matrix[start_row][start_col] = ' '
        visualiser(matrix)
        exit()


def cols_validator(idx):
    if idx not in range(COLS):
        print('The delivery is late. Order is canceled.')
        matrix[start_row][start_col] = ' '
        visualiser(matrix)
        exit()


def movement(matrix, curr_row, curr_col, next_row, next_col):
    matrix[curr_row][curr_col] = '.'
    curr_row = next_row
    curr_col = next_col
    matrix[curr_row][curr_col] = 'B'
    return curr_row, curr_col


ROWS, COLS = list(map(int, input().split()))
matrix = enter_the_matrix(ROWS)
start_row, start_col = starting_pos_finder(matrix)
curr_row, curr_col = start_row, start_col
command = input()

while command:

    next_row, next_col = next_pos_calculator(curr_row, curr_col, command)
    print(next_row)
    if matrix[next_row][next_col] == 'A':
        curr_row, curr_col = movement(matrix, curr_row, curr_col, next_row, next_col)
        print('Pizza is delivered on time! Next order...')
    elif matrix[curr_row][curr_col] == '*':
        continue
    elif matrix[curr_row][curr_col] == 'P':
        curr_row, curr_col = movement(matrix, curr_row, curr_col, next_row, next_col)
        print('Pizza is collected. 10 minutes for delivery.')
    elif matrix[curr_row][curr_col] == '-':
        curr_row, curr_col = movement(matrix, curr_row, curr_col, next_row, next_col)
    command = input()
visualiser(matrix)