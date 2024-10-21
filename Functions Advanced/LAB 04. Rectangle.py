def rectangle(a, b):
    if type(a) != int or type(b) != int:
        return "Enter valid values!"

    def area():
        return a * b

    def perimeter():
        return 2 * (a + b)

    return f'Rectangle area: {area()}\nRectangle perimeter: {perimeter()}'


print(rectangle(2, 10))
