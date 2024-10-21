from collections import deque
contestants = deque(int(el) for el in input().split())
pies = [int(x) for x in input().split()]

while contestants and pies:
    current_contestant = contestants.popleft()
    current_pie = pies.pop()
    if current_contestant > current_pie:
        new_contestant = current_contestant - current_pie
        contestants.append(new_contestant)
    elif current_pie > current_contestant:
        new_pie = current_pie - current_contestant
        if new_pie == 1 and len(pies) > 0:
            pies[-1] += new_pie
        else:
            pies.append(new_pie)

if len(pies) == len(contestants) == 0:
    print('We have a champion!')
elif len(pies) > 0:
    print('Our contestants need to rest!')
    print(f"Pies left: {', '.join([str(j) for j in pies])}")
elif len(contestants) > 0:
    print('We will have to wait for more pies to be baked!')
    print(f"Contestants left: {', '.join([str(i) for i in contestants])}")