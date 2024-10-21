from collections import deque
def accommodate(*args, **kwargs):
    guests = deque()
    rooms = {}
    successful_accommodations = {}
    non_accommodated = 0
    free_rooms = 0
    result = ''
    for i in args:
        guests.append(i)
    for k, v in kwargs.items():
        room_number = int(k[-3:])
        rooms[room_number] = v
    rooms = dict(sorted(rooms.items(), key=lambda kvp: (kvp[1], kvp[0])))
    while guests:
        guest = guests.popleft()
        for number, count in rooms.items():
            if guest <= count:
                successful_accommodations[number] = guest
                rooms[number] = 0
                break
        else:
            non_accommodated += guest
    for key, value in rooms.items():
        if not value == 0:
            free_rooms += 1
    if successful_accommodations:
        result += f'A total of {len(successful_accommodations)} accommodations were completed!\n'
        successful_accommodations = dict(sorted(successful_accommodations.items(), key=lambda kvp: kvp[0]))
        for i, j in successful_accommodations.items():
            result += f'<Room {i} accommodates {j} guests>\n'
    else:
        result += f'No accommodations were completed!\n'
    if non_accommodated > 0:
        result += f'Guests with no accommodation: {non_accommodated}\n'
    if free_rooms > 0:
        result += f'Empty rooms: {free_rooms}\n'
    return result




print(accommodate(10, 9, 8, room_307=6, room_802=5))