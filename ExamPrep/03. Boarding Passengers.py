def boarding_passengers(capacity: int, *data):
    to_be_boarded = []
    boarded = {}
    all_boarded = True
    for passenger in data:
        to_be_boarded.append(passenger)
    for el in to_be_boarded:
        count = int(el[0])
        benefit = el[1]
        if capacity >= count:
            capacity -= count
            if benefit not in boarded:
                boarded[benefit] = 0
            boarded[benefit] += count
        else:
            all_boarded = False
    result = ''
    result += 'Boarding details by benefit plan:\n'
    boarded = dict(sorted(boarded.items(), key=lambda kvp: (-kvp[1], kvp[0])))
    for k,v in boarded.items():
        result += f'## {k}: {v} guests\n'
    if all_boarded and capacity == 0:
        result += 'All passengers are successfully boarded!'
    elif not all_boarded and capacity > 0:
        result += f'Partial boarding completed. Available capacity: {capacity}.'
    elif not all_boarded and capacity==0:
        result += 'Boarding unsuccessful. Cruise ship at full capacity.'
    return result


print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))