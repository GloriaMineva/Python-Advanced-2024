from collections import deque

cups = deque(int(x) for x in input().split())
bottles = deque(map(int, input().split()))
wasted_water = 0
while len(cups) > 0 and len(bottles) > 0:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()
    if current_cup <= current_bottle:
        wasted_water += current_bottle - current_cup
    else:
        current_cup -= current_bottle
        while current_cup > 0 and bottles:
            current_bottle = bottles.pop()
            if current_cup <= current_bottle:
                wasted_water += current_bottle - current_cup
                break
            else:
                current_cup -= current_bottle
if cups:
    print('Cups: ', end='')
    print(*cups)
if bottles:
    print('Bottles: ', end='')
    print(*bottles)
print(f'Wasted litters of water: {wasted_water}')
