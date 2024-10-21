def fill_the_box(a, b, c, *args) -> str:
    volume = a * b * c
    cubes_left = 0
    for i in args[3:]:
        if i == 'Finish':
            if cubes_left > 0:
                return f'No more free space! You have {cubes_left} more cubes.'
            else:
                return f'There is free space in the box. You could put {volume} more cubes.'
        if volume >= i:
            volume -= i
        else:
            cubes_left += i - volume
            volume = 0


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))