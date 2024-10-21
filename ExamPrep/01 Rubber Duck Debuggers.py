from collections import deque
time_per_task = deque(map(int, input().split()))
number_of_task = list(map(int, input().split()))
rubber_ducks = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0
}
while time_per_task and number_of_task:
    current_time = time_per_task.popleft()
    current_number = number_of_task.pop()
    calculated_time = current_time * current_number
    if 0 <= calculated_time <= 60:
        rubber_ducks['Darth Vader Ducky'] += 1
    elif 61 <= calculated_time <= 120:
        rubber_ducks['Thor Ducky'] += 1
    elif 121 <= calculated_time <= 180:
        rubber_ducks['Big Blue Rubber Ducky'] += 1
    elif 181 <= calculated_time <= 240:
        rubber_ducks['Small Yellow Rubber Ducky'] += 1
    elif 241 <= calculated_time:
        time_per_task.append(current_time)
        number_of_task.append(current_number - 2)
print('Congratulations, all tasks have been completed! Rubber ducks rewarded:')
for key, value in rubber_ducks.items():
    print(f'{key}: {value}')