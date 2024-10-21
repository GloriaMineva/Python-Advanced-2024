from collections import deque
packages = [int(x) for x in input().split()]
curriers = deque(int(y) for y in input().split())
total_weight = 0
while packages and curriers:
    current_package = packages.pop()
    current_currier = curriers.popleft()
    if current_currier >= current_package:
        new_currier = current_currier - current_package * 2
        total_weight += current_package
        if new_currier > 0:
            curriers.append(new_currier)
    elif current_currier < current_package:
        new_package = current_package - current_currier
        packages.append(new_package)
        total_weight += current_currier
print(f'Total weight: {total_weight} kg')
if packages:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages))}")
elif curriers:
    print(f"Couriers are still on duty: {', '.join(map(str, curriers))} but there are no more packages to deliver.")
else:
    print('Congratulations, all packages were delivered successfully by the couriers today.')
