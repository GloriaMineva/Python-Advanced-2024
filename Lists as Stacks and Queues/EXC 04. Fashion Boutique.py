clothes_stack = list(map(int, input().split()))
capacity = int(input())
rack_counter = 1
current_rack = capacity
while clothes_stack:
    if clothes_stack[-1] <= current_rack:
        current_rack -= clothes_stack.pop()
    else:
        rack_counter += 1
        current_rack = capacity
        current_rack -= clothes_stack.pop()
print(rack_counter)