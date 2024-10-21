# from collections import deque
#
# kids_queue = deque(input().split())
# counter = int(input())
# turns = 0
#
# while len(kids_queue) > 1:
#     for i in range(counter - 1):
#         first_kid = kids_queue.popleft()
#         kids_queue.append(first_kid)
#     print(f'Removed {kids_queue.popleft()}')
# print(f'Last is {kids_queue.popleft()}')


from collections import deque

kids_queue = deque(input().split())
counter = int(input()) - 1

while len(kids_queue) > 1:
    kids_queue.rotate(-counter)
    print(f'Removed {kids_queue.popleft()}')
print(f'Last is {kids_queue.popleft()}')