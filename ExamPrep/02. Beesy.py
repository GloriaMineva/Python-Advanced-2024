directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1)
}

SIZE = int(input())
matrix = []
bee_row = None
bee_col = None
energy = 15
nectar = 0
deaths_counter = 0
for i in range(SIZE):
    current_row = list(input())
    if 'B' in current_row:
        bee_row = i
        bee_col = current_row.index('B')
    matrix.append(current_row)


def index_validator(index):
    if index in range(SIZE):
        return index
    elif index < 0:
        return SIZE - 1
    elif index > SIZE - 1:
        return 0



while True:
    command = input()
    energy -= 1
    desired_row = bee_row + directions[command][0]
    new_row = index_validator(desired_row)
    desired_col = bee_col + directions[command][1]
    new_col = index_validator(desired_col)
    if matrix[new_row][new_col] == 'H':
        matrix[bee_row][bee_col] = '-'
        bee_row = new_row
        bee_col = new_col
        matrix[bee_row][bee_col] = 'B'
        if nectar >= 30:
            print(f'Great job, Beesy! The hive is full. Energy left: {energy}')
            break
        else:
            print('Beesy did not manage to collect enough nectar.')
            break
    elif matrix[new_row][new_col] == '-':
        matrix[bee_row][bee_col] = '-'
        bee_row = new_row
        bee_col = new_col
        matrix[bee_row][bee_col] = 'B'
    else:
        nectar += int(matrix[new_row][new_col])
        matrix[bee_row][bee_col] = '-'
        bee_row = new_row
        bee_col = new_col
        matrix[bee_row][bee_col] = 'B'
    if energy <= 0:
        if nectar >= 30 and deaths_counter == 0:
            energy += nectar - 30
            nectar -= energy
            deaths_counter += 1
        else:
            print('This is the end! Beesy ran out of energy.')
            break
for row in matrix:
    print(*row, sep='')



