from collections import defaultdict
def list_roman_emperors(*args, **kwargs):
    result = ''
    successful = defaultdict(int)
    unsuccessful = defaultdict(int)
    for name, status in args:
        status = bool(status)
        if status:
            successful[name] = 0
        else:
            unsuccessful[name] = 0
    for emperor, years in kwargs.items():
        years = int(years)
        if emperor in successful:
            successful[emperor] = years
        elif emperor in unsuccessful:
            unsuccessful[emperor] = years
    successful = sorted(successful.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    unsuccessful = sorted(unsuccessful.items(), key=lambda kvp: (kvp[1], kvp[0]))
    result += f'Total number of emperors: {len(successful) + len(unsuccessful)}\n'
    if successful:
        result += 'Successful emperors:\n'
        for key, value in successful:
            result += f"****{key}: {value}\n"
    if unsuccessful:
        result += 'Unsuccessful emperors:\n'
        for key_, value_ in unsuccessful:
            result += f"****{key_}: {value_}\n"

    return result


print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))