mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
SIZE = int(input())
matrix = []
money = 100
gambler_row = None
gambler_col = None
for i in range(SIZE):
    curr_row = input()
    if 'G' in curr_row:
        gambler_row = i
        gambler_col = curr_row.index('G')
    matrix.append(list(curr_row))
command = input()


def matrix_printer(matrix):
    for row in matrix:
        print(''.join(row))


def index_validator(idx):
    if idx not in range(SIZE):
        print('Game over! You lost everything!')
        exit()


def movement(gambler_row, gambler_col, desired_row, desired_col):
    matrix[gambler_row][gambler_col] = '-'
    matrix[desired_row][desired_col] = 'G'
    gambler_row = desired_row
    gambler_col = desired_col
    return gambler_row, gambler_col


while command != 'end':
    desired_row = gambler_row + mapper[command][0]
    index_validator(desired_row)
    desired_col = gambler_col + mapper[command][1]
    index_validator(desired_col)
    if matrix[desired_row][desired_col] == 'J':
        money += 100000
        gambler_row, gambler_col = movement(gambler_row, gambler_col, desired_row, desired_col)
        print('You win the Jackpot!')
        print(f'End of the game. Total amount: {money}$')
        matrix_printer(matrix)
        exit()
    elif matrix[desired_row][desired_col] == 'W':
        money += 100
        gambler_row, gambler_col = movement(gambler_row, gambler_col, desired_row, desired_col)
    elif matrix[desired_row][desired_col] == 'P':
        money -= 200
        if money <= 0:
            print('Game over! You lost everything!')
            exit()
        gambler_row, gambler_col = movement(gambler_row, gambler_col, desired_row, desired_col)
    elif matrix[desired_row][desired_col] == '-':
        gambler_row, gambler_col = movement(gambler_row, gambler_col, desired_row, desired_col)
    command = input()
print(f'End of the game. Total amount: {money}$')
matrix_printer(matrix)
