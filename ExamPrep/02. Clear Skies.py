mapper = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1)
}

SIZE = int(input())
field = []
armor = 300
enemy_count = 4
jet_row = None
jet_col = None
for i in range(SIZE):
    current_row = input()
    field.append(list(current_row))
    if 'J' in current_row:
        jet_col = current_row.index('J')
        jet_row = i

while armor > 0:
    command = input()
    field[jet_row][jet_col] = '-'
    jet_row += mapper[command][0]
    jet_col += mapper[command][1]
    if field[jet_row][jet_col] == 'R':
        armor = 300
    elif field[jet_row][jet_col] == 'E':
        enemy_count -= 1
        field[jet_row][jet_col] = 'J'
        if enemy_count == 0:
            print('Mission accomplished, you neutralized the aerial threat!')
            for row in range(SIZE):
                print(''.join(field[row]))
            exit()
        armor -= 100

else:
    print(f'Mission failed, your jetfighter was shot down! Last coordinates [{jet_row}, {jet_col}]!')
    for row in range(SIZE):
        print(''.join(field[row]))


