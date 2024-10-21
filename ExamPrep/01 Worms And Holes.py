from collections import deque
worms = list(map(int, input().split()))
holes = deque(map(int, input().split()))
matches = 0
worms_start_count = len(worms)
while worms and holes:
    curr_worm = worms.pop()
    curr_hole = holes.popleft()
    if curr_worm == curr_hole:
        matches += 1
    elif curr_worm != curr_hole:
        curr_worm -= 3
        if curr_worm > 0:
            worms.append(curr_worm)
if matches > 0:
    print(f'Matches: {matches}')
else:
    print('There are no matches.')
if worms:
    print(f'Worms left: {", ".join(map(str, worms))}')
else:
    if matches == worms_start_count:
        print('Every worm found a suitable hole!')
    else:
        print('Worms left: none')
if holes:
    print(f'Holes left: {", ".join(map(str, holes))}')
else:
    print('Holes left: none')
