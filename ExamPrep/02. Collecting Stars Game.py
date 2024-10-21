directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1)
}
SIZE = int(input())
field = []
stars = 2
player_row = None
player_col = None
for i in range(SIZE):
    current_row = input().split()
    if 'P' in current_row:
        player_row = i
        player_col = current_row.index('P')
    field.append(current_row)
while stars < 10:
    direction = input()
    desired_row = player_row + directions[direction][0]
    desired_col = player_col + directions[direction][1]
    if desired_row not in range(SIZE) or desired_col not in range(SIZE):
        field[player_row][player_col] = '.'
        player_row = 0
        player_col = 0
        if field[0][0] == '*':
            stars += 1
        field[player_row][player_col] = 'P'
    else:
        if field[desired_row][desired_col] == '*':
            stars += 1
            field[player_row][player_col] = '.'
            player_row = desired_row
            player_col = desired_col
            field[player_row][player_col] = 'P'
        elif field[desired_row][desired_col] == '#':
            stars -= 1
            if stars <= 0:
                print('Game over! You are out of any stars.')
                break
        elif field[desired_row][desired_col] == '.':
            field[player_row][player_col] = '.'
            player_row = desired_row
            player_col = desired_col
            field[player_row][player_col] = 'P'

else:
    print('You won! You have collected 10 stars.')
print(f'Your final position is [{player_row}, {player_col}]')
for row in field:
    print(*row, sep=' ')


