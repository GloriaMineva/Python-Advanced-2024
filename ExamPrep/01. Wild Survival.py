from collections import deque
from math import ceil
bees = deque(int(x) for x in input().split())
enemies = [int(y) for y in input().split()]
while bees and enemies:
    current_bee = bees.popleft()
    current_enemy = enemies.pop()
    if current_bee < current_enemy * 7:
        new_enemy = ceil(((current_enemy * 7) - current_bee) / 7)
        enemies.append(new_enemy)
    elif current_bee > current_enemy * 7:
        new_bee = current_bee - current_enemy * 7
        bees.append(new_bee)
print('The final battle is over!')
if bees:
    print(f"Bee groups left: {', '.join(map(str, bees))}")
elif enemies:
    print(f"Bee-eater groups left: {', '.join(map(str, enemies))}")
else:
    print('But no one made it out alive!')