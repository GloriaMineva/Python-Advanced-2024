directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
def enter_the_matrix(SIZE):
    matrix = []
    for i in range(SIZE):
        row = list(input())
        if 'S' in row:
            curr_row = i
            curr_col = row.index('S')
        matrix.append(row)
    return matrix, curr_row, curr_col


def draw_matrix():
    for row in matrix:
        print(''.join(row))


SIZE = int(input())
tons = 0
matrix, curr_row, curr_col = enter_the_matrix(SIZE)
command = input()


def idx_validator(idx):
    if idx in range(SIZE):
        return idx
    elif idx >= SIZE:
        return idx - SIZE
    elif idx < 0:
        return SIZE + idx


def movement(matrix, curr_row, curr_col, desired_row, desired_col):
    matrix[curr_row][curr_col] = '-'
    curr_row = desired_row
    curr_col = desired_col
    matrix[curr_row][curr_col] = 'S'
    return curr_row, curr_col


while command != 'collect the nets':
    desired_row = curr_row + directions[command][0]
    desired_row = idx_validator(desired_row)
    desired_col = curr_col + directions[command][1]
    desired_col = idx_validator(desired_col)
    if matrix[desired_row][desired_col] == '-':
        curr_row, curr_col = movement(matrix, curr_row, curr_col, desired_row, desired_col)
    elif matrix[desired_row][desired_col] == 'W':
        curr_row, curr_col = movement(matrix, curr_row, curr_col, desired_row, desired_col)
        print(f'You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the '
              f'ship: [{curr_row},{curr_col}]')
        exit()
    else:
        tons += int(matrix[desired_row][desired_col])
        curr_row, curr_col = movement(matrix, curr_row, curr_col, desired_row, desired_col)
    command = input()
if tons >= 20:
    print('Success! You managed to reach the quota!')
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - tons} tons of fish more.")
if tons > 0:
    print(f'Amount of fish caught: {tons} tons.')
draw_matrix()