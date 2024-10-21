def softuni_students(*args, **kwargs):
    result = ''
    valid_students = {}
    invalid_students = set()
    for data in args:
        id, name = data
        if id not in kwargs:
            invalid_students.add(name)
        else:
            valid_students[name] = kwargs[id]
    sorted_valid_students = sorted(valid_students.items(), key=lambda kvp: kvp[0])
    sorted_invalid_students = sorted(invalid_students)
    for k, v in sorted_valid_students:
        result += f'*** A student with the username {k} has successfully finished the course {v}!\n'
    if invalid_students:
        result += f"!!! Invalid course students: {', '.join(sorted_invalid_students)}"
    return result


print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))





