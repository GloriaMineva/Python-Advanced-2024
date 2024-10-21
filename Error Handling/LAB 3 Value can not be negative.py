class ValueCanNotBeNegative(Exception):
    pass


for i in range(5):
    current_num = int(input())
    if current_num < 0 or current_num == -0:
        raise ValueCanNotBeNegative
