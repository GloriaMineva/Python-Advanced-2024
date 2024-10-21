robots_stack = list(input().split(';'))
hours, minutes, seconds = list(map(int, input().split(':')))
print(hours, minutes, seconds)
while True:
    product = input()
    if product == 'End':
        break
    seconds += 1
    if seconds > 59:
        minutes += 1
        seconds = 0
    if minutes > 59:
        hours += 1
        minutes = 0


