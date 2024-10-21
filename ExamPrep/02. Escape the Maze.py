directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1)
}

SIZE = int(input())
maze = []
health = 100
player_row = None
player_col = None
for i in range(SIZE):
    current_row = input()
    if 'P' in current_row:
        player_row = i
        player_col = current_row.index('P')
    maze.append(list(current_row))
while True:
    command = input()
    desired_row = player_row + directions[command][0]
    desired_col = player_col + directions[command][1]
    if desired_row in range(SIZE) and desired_col in range(SIZE):
        maze[player_row][player_col] = '-'
        player_row = desired_row
        player_col = desired_col
        if maze[player_row][player_col] == 'H':
            health += 15
            if health > 100:
                health = 100
        elif maze[player_row][player_col] == 'M':
            health -= 40
            if health <= 0:
                maze[player_row][player_col] = 'P'
                print('Player is dead. Maze over!')
                print('Player\'s health: 0 units')
                break
        elif maze[player_row][player_col] == 'X':
            maze[player_row][player_col] = 'P'
            print('Player escaped the maze. Danger passed!')
            print(f'Player\'s health: {health} units')
            break
        maze[player_row][player_col] = 'P'
for row in maze:
    print(*row, sep='')