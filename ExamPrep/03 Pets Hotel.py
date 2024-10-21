from collections import defaultdict
def accommodate_new_pets(capacity:int, weight_limit: float, *args):
    result = ''
    all_accommodated = True
    accommodated = defaultdict(int)
    for data in args:
        animal_type = data[0]
        curr_weight = float(data[1])
        if capacity > 0:
            if curr_weight <= weight_limit:
                capacity -= 1
                accommodated[animal_type] += 1
        else:
            all_accommodated = False
            break
    if all_accommodated:
        result += f'All pets are accommodated! Available capacity: {capacity}.\n'
    else:
        result += 'You did not manage to accommodate all pets!\n'
    result += "Accommodated pets:\n"
    sorted_accommodated = sorted(accommodated.items())
    for k, v in sorted_accommodated:
        result += f'{k}: {v}\n'
    return result


print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))






