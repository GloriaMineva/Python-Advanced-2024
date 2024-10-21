liters_remaining = int(input())
people_queue = []
while True:
    current_name = input()
    if current_name == 'Start':
        break
    people_queue.append(current_name)
while True:
    command = input()
    if command == 'End':
        print(f'{liters_remaining} liters left')
        break
    if 'refill' in command:
        liters_to_add = int(command.split(' ')[1])
        liters_remaining += liters_to_add
    else:
        command = int(command)
        if liters_remaining >= command:
            print(f'{people_queue[0]} got water')
            liters_remaining -= command
            people_queue.pop(0)
        else:
            print(f'{people_queue[0]} must wait')
            people_queue.pop(0)


